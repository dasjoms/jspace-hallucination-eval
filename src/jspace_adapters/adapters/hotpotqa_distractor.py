"""
Adapter: HotpotQA-distractor (multi-hop, closed-book).

Dataset: hotpotqa/hotpot_qa, config distractor, split validation.
Schema: id, question, answer, type, level, supporting_facts, context.
The context and supporting_facts fields are intentionally DISCARDED:
this is closed-book multi-hop; the model must reason from parametric knowledge.
"""

from __future__ import annotations

from ..base import DatasetAdapter, JspaceExample


class HotpotQADistractorAdapter(DatasetAdapter):
    dataset_id = "hotpotqa_distractor"
    repo = "hotpotqa/hotpot_qa"
    config = "distractor"
    split = "validation"
    task_family = "multi_hop_factual"
    answer_format = "short_freeform"
    prompt_template_id = "short_answer_v1"
    max_new_tokens = 16
    expected_failure_mode = "multi_hop_intermediate_uncertainty"
    supports_short_answer = True
    supports_multiple_choice = False

    def extract_example(self, raw: dict, *, index: int) -> JspaceExample:
        ans = raw.get("answer")
        aliases = [ans] if isinstance(ans, str) and ans.strip() else []
        return JspaceExample(
            example_id="",
            source_example_id=str(raw.get("id") or f"idx_{index}"),
            question=raw["question"],
            aliases=aliases,
            metadata={
                "dataset_index": index,
                # Difficulty stratification: do workspace features differ
                # between comparison-type and bridge-type? easy vs hard?
                "hotpotqa_type": raw.get("type"),
                "hotpotqa_level": raw.get("level"),
                "n_supporting_facts": len(raw.get("supporting_facts", [])),
            },
        )
