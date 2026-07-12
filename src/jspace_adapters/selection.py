"""
jspace_adapters.selection — Dataset-independent example selection.

Public API:
  - select_deduplicated(raw_examples, extract_fn, *, n, seed, dataset_id)
"""

from __future__ import annotations

import random
from typing import Callable

from .base import JspaceExample, safe_slug
from .labelling import normalize_answer


def select_deduplicated(
    raw_examples: list,
    extract_fn: Callable[[dict, int], JspaceExample],
    *,
    n: int,
    seed: int,
    dataset_id: str,
    dedup_by_source_id: bool = True,
    dedup_by_normalized_question: bool = True,
) -> list[JspaceExample]:
    """Generic selection: dedup, drop empty, sample n.

    Mirrors the 02 notebook's selection loop (§5) but is dataset-agnostic.
    Each JspaceExample gets a stable run-local example_id assigned here, so
    the adapter doesn't need to know about run-local id conventions.
    """
    rng = random.Random(seed)
    seen_src: set[str] = set()
    seen_q: set[str] = set()
    kept: list[JspaceExample] = []
    for i, raw in enumerate(raw_examples):
        try:
            ex = extract_fn(raw, index=i)
        except Exception as e:
            # Defensive: skip examples that crash the adapter, with a warning
            # printed to stderr.
            import sys
            print(
                f"⚠️  {dataset_id} adapter: extract_example(idx={i}) failed: "
                f"{type(e).__name__}: {e}",
                file=sys.stderr,
            )
            continue
        if not ex.question or not ex.question.strip():
            continue
        if not ex.aliases and not ex.has_multiple_choice():
            continue
        sid = ex.source_example_id or f"idx_{i}"
        nq = normalize_answer(ex.question)
        if dedup_by_source_id and sid in seen_src:
            continue
        if dedup_by_normalized_question and nq in seen_q:
            continue
        seen_src.add(sid)
        seen_q.add(nq)
        # Assign a stable run-local example_id.
        ex.example_id = f"ex_{len(kept):05d}_{safe_slug(sid, 40)}"
        # Also embed the dataset id for cross-dataset meta-analysis.
        ex.metadata.setdefault("dataset_id", dataset_id)
        kept.append(ex)
    if len(kept) <= n:
        return kept
    return rng.sample(kept, n)
