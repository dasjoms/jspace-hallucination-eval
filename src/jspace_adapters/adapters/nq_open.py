"""
Adapter: NQ-Open (Natural Questions, open-domain short answer).

Dataset: google-research-datasets/nq_open, config nq_open, split validation.
Schema: question, answer (list of strings, each <= 5 tokens per the original
         NQ-Open construction).
"""

from __future__ import annotations

from ..base import DatasetAdapter, JspaceExample


class NQOpenAdapter(DatasetAdapter):
    dataset_id = "nq_open"
    repo = "google-research-datasets/nq_open"
    config = "nq_open"
    split = "validation"
    task_family = "closed_book_factual_short"
    answer_format = "short_alias"
    prompt_template_id = "short_answer_v1"
    max_new_tokens = 16
    expected_failure_mode = "parametric_recall_uncertainty"
    supports_short_answer = True
    supports_multiple_choice = False

    def extract_example(self, raw: dict, *, index: int) -> JspaceExample:
        return JspaceExample(
            example_id="",
            source_example_id=f"nq_open_{index}",
            question=raw["question"],
            aliases=[x for x in raw.get("answer", []) if isinstance(x, str)],
            metadata={"dataset_index": index},
        )
