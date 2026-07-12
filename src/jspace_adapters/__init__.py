"""
jspace_adapters — Dataset adapter registry for the J-Space hallucination experiment.

Public API:
  - get_adapter(dataset_id) -> DatasetAdapter instance
  - list_adapter_ids() -> list[str]
  - ADAPTERS: dict mapping dataset_id -> DatasetAdapter instance
  - re-export: JspaceExample, DatasetAdapter for convenience

Importable from a notebook:
  >>> import sys
  >>> sys.path.insert(0, "/content/drive/MyDrive/J-Space_Artifacts/_shared/utils")
  >>> from jspace_adapters import get_adapter, list_adapter_ids
"""

from __future__ import annotations

from .base import DatasetAdapter, JspaceExample
from . import labelling
from . import prompt_templates
from . import selection
from .adapters import (
    triviaqa_rc_nocontext,
    popqa,
    nq_open,
    truthfulqa_gen,
    hotpotqa_distractor,
    gsm8k,
    commonsenseqa,
)


# Re-export the adapter classes for type access
__all__ = [
    "DatasetAdapter",
    "JspaceExample",
    "get_adapter",
    "list_adapter_ids",
    "ADAPTERS",
    "labelling",
    "prompt_templates",
    "selection",
]


def _build_registry() -> dict[str, DatasetAdapter]:
    """Construct the ADAPTERS dict. Done lazily so that module import is fast."""
    return {
        cls.dataset_id: cls()
        for cls in [
            triviaqa_rc_nocontext.TriviaQARcNoContextAdapter,
            popqa.PopQAAdapter,
            nq_open.NQOpenAdapter,
            truthfulqa_gen.TruthfulQAGenAdapter,
            hotpotqa_distractor.HotpotQADistractorAdapter,
            gsm8k.GSM8KAdapter,
            commonsenseqa.CommonsenseQAAdapter,
        ]
    }


ADAPTERS: dict[str, DatasetAdapter] = _build_registry()


def get_adapter(dataset_id: str) -> DatasetAdapter:
    if dataset_id not in ADAPTERS:
        raise KeyError(
            f"Unknown dataset_id {dataset_id!r}. "
            f"Available: {sorted(ADAPTERS.keys())}"
        )
    return ADAPTERS[dataset_id]


def list_adapter_ids() -> list[str]:
    return sorted(ADAPTERS.keys())
