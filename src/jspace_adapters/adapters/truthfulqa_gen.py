"""
Adapter: TruthfulQA-generation (adversarial misconception QA).

Dataset: truthfulqa/truthful_qa, config generation, split validation.
Schema: type, category, question, best_answer, correct_answers, incorrect_answers, source.

Special handling:
  - best_answer is the canonical single-alias target (human-curated short form).
  - correct_answers are paraphrases / longer qualified responses; preserved in
    metadata for the LLM-judge path.
  - allow_prefix_match=True triggers the prefix-match labeler regime.
  - incorrect_answers preserved for confusion-matrix analysis.
  - 32 max_new_tokens because aliases are ~50 chars.
"""

from __future__ import annotations

from ..base import DatasetAdapter, JspaceExample


class TruthfulQAGenAdapter(DatasetAdapter):
    dataset_id = "truthfulqa_gen"
    repo = "truthfulqa/truthful_qa"
    config = "generation"
    split = "validation"
    task_family = "adversarial_truthfulness_short"
    answer_format = "sentence"
    prompt_template_id = "short_answer_v1"
    max_new_tokens = 32
    expected_failure_mode = "imitative_misconception_hallucination"
    supports_short_answer = True
    supports_multiple_choice = False

    def extract_example(self, raw: dict, *, index: int) -> JspaceExample:
        ba = raw.get("best_answer")
        if not isinstance(ba, str) or not ba.strip():
            ca = raw.get("correct_answers", [])
            ba = next((x for x in ca if isinstance(x, str) and x.strip()), "")
        aliases = [ba] if ba else []
        correct_full = [
            x for x in raw.get("correct_answers", [])
            if isinstance(x, str) and x != ba
        ]
        incorrect = [
            x for x in raw.get("incorrect_answers", [])
            if isinstance(x, str)
        ]
        return JspaceExample(
            example_id="",
            source_example_id=str(raw.get("question", "")[:50]) or f"idx_{index}",
            question=raw["question"],
            aliases=aliases,
            metadata={
                "dataset_index": index,
                "type": raw.get("type"),
                "category": raw.get("category"),
                "source": raw.get("source"),
                "correct_answers_full": correct_full,
                "incorrect_answers": incorrect,
                # Flag the labelling layer to allow first-N-word prefix matches.
                # See plan §6.4 and the locked decision in §0.1 of the plan.
                "allow_prefix_match": True,
            },
        )
