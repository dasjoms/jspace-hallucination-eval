"""
jspace_adapters.base — Core data structures and abstract base class.

This module defines:
  - JspaceExample: the unified per-example record the main experiment loop sees.
  - DatasetAdapter: the abstract base class for all per-dataset adapters.

Both are dataset-agnostic. Per-dataset adapters live in jspace_adapters.adapters.*.
"""

from __future__ import annotations

import json
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Iterator


# ---------------------------------------------------------------------------
# Utility helpers (small, used by adapters)
# ---------------------------------------------------------------------------

def safe_slug(text: str, max_len: int = 80) -> str:
    """Lowercase + replace non-alphanumeric + collapse dashes; for filenames/ids."""
    text = str(text).lower().replace("/", "-").replace(".", "p")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:max_len].strip("-") or "unknown"


def utc_now_iso() -> str:
    """ISO-8601 UTC timestamp with Z suffix, no microseconds."""
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# JspaceExample — the unified per-example record
# ---------------------------------------------------------------------------

@dataclass
class JspaceExample:
    """One example, post-adapter, ready for the experiment loop.

    The main loop iterates over JspaceExamples. The adapter handles all
    dataset-specific field extraction; the loop never touches raw HF records.
    """

    # Identity
    example_id: str = ""                       # assigned by select_deduplicated
    source_example_id: str = ""               # dataset's native id

    # Content
    question: str = ""
    aliases: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    # For MC datasets only (None for short-answer datasets)
    choices: list[dict] | None = None          # [{"label": "A", "text": "..."}, ...]
    correct_choice_label: str | None = None
    correct_choice_text: str | None = None

    def to_dict(self) -> dict:
        """Serializable form (for JSONL dumps)."""
        return asdict(self)

    def has_multiple_choice(self) -> bool:
        return self.choices is not None and len(self.choices) > 0

    def is_numeric(self) -> bool:
        return self.metadata.get("task_family") == "numeric_reasoning_short"

    def wants_prefix_match(self) -> bool:
        return bool(self.metadata.get("allow_prefix_match", False))


# ---------------------------------------------------------------------------
# DatasetAdapter — abstract base class
# ---------------------------------------------------------------------------

class DatasetAdapter(ABC):
    """One concrete dataset's adapter.

    Subclasses must override:
      - All class attributes (dataset_id, repo, config, split, ...)
      - extract_example()

    The base class wires up load(), build_prompt(), parse_generation(), and
    the manifest dictionary, all of which delegate to the prompt_template
    registry and labelling helpers.
    """

    # ---- Required class attributes (subclasses set these) ----
    dataset_id: str = ""
    repo: str = ""
    config: str | None = None
    split: str = ""
    task_family: str = ""
    answer_format: str = ""
    prompt_template_id: str = ""
    max_new_tokens: int = 16
    expected_failure_mode: str = ""
    supports_short_answer: bool = True
    supports_multiple_choice: bool = False

    # ---- State (set by load()) ----
    examples: list[JspaceExample] = field(default_factory=list)  # type: ignore[assignment]

    # ---- Required methods ----
    @abstractmethod
    def extract_example(self, raw: dict, *, index: int) -> JspaceExample:
        """Convert one raw HF example into a JspaceExample."""
        ...

    # ---- Provided methods ----
    def load(self, *, n: int, seed: int) -> None:
        """Load the dataset, dedup, sample n examples. Sets self.examples.

        Subclasses normally do not override this.
        """
        from datasets import load_dataset
        from .selection import select_deduplicated
        ds = load_dataset(self.repo, self.config, split=self.split)
        raw = list(ds)
        self.examples = select_deduplicated(
            raw, self.extract_example, n=n, seed=seed,
            dataset_id=self.dataset_id,
        )

    def iter_examples(self) -> Iterator[JspaceExample]:
        yield from self.examples

    def build_prompt(self, example: JspaceExample) -> str:
        """Build the prompt text using this adapter's prompt_template_id.

        For MC datasets, the template needs the choices list. This is passed
        via the example's .choices attribute.
        """
        from .prompt_templates import get_template
        return get_template(self.prompt_template_id).build(example)

    def parse_generation(self, raw_text: str) -> str | None:
        """Parse the model's raw generated text into a clean answer.

        Returns None if the parser cannot extract a usable answer
        (e.g. no letter in MC output, no number in numeric output).
        """
        from .prompt_templates import get_template
        return get_template(self.prompt_template_id).parse(raw_text)

    def manifest_dict(self, *, n: int, seed: int) -> dict:
        """Build the dataset_manifest.json payload."""
        from datasets import load_dataset
        try:
            ds = load_dataset(self.repo, self.config, split=self.split)
            n_total = len(ds)
        except Exception:
            n_total = None
        m = {
            "dataset_id": self.dataset_id,
            "repo": self.repo,
            "config": self.config,
            "split": self.split,
            "task_family": self.task_family,
            "answer_format": self.answer_format,
            "prompt_template_id": self.prompt_template_id,
            "max_new_tokens": self.max_new_tokens,
            "n_total_in_split": n_total,
            "n_requested": n,
            "random_seed": seed,
            "expected_failure_mode": self.expected_failure_mode,
            "supports_short_answer": self.supports_short_answer,
            "supports_multiple_choice": self.supports_multiple_choice,
        }
        # Optional: prefix-match (TruthfulQA)
        if any(ex.wants_prefix_match() for ex in self.examples[:5]):
            m["allow_prefix_match"] = True
        return m

    def smoke_test(self, n: int = 3) -> dict:
        """Run n examples through the deterministic labeler using the
        gold alias as the prediction. Verifies the adapter+labeler wiring.

        Does NOT call a real model. The purpose is to verify schema wiring,
        not the model.
        """
        from .labelling import (
            deterministic_label,
            deterministic_label_mc,
            deterministic_label_with_prefix,
        )
        from .prompt_templates import get_template

        results: list[dict] = []
        n_pass = 0
        for ex in self.examples[:n]:
            # Simulate prediction as the gold answer.
            if ex.has_multiple_choice():
                sim_pred = ex.correct_choice_label or "A"
                det = deterministic_label_mc(sim_pred, ex)
            elif ex.wants_prefix_match():
                sim_pred = (ex.aliases[0] if ex.aliases else "x")
                det = deterministic_label_with_prefix(sim_pred, ex)
            else:
                sim_pred = (ex.aliases[0] if ex.aliases else "x")
                det = deterministic_label(sim_pred, ex.aliases)

            ok = bool(det.get("deterministic_correct"))
            n_pass += int(ok)
            results.append({
                "example_id": ex.example_id,
                "question": ex.question[:60],
                "aliases": ex.aliases[:3],
                "choices": ex.choices,
                "predicted": sim_pred,
                "label_source": det.get("deterministic_label_source"),
                "correct": ok,
            })
        return {
            "dataset_id": self.dataset_id,
            "n": len(results),
            "n_pass": n_pass,
            "pass_rate": (n_pass / len(results)) if results else None,
            "examples": results,
        }
