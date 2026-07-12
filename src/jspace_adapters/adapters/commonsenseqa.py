"""
Adapter: CommonsenseQA (5-way multiple-choice commonsense).

Dataset: tau/commonsense_qa, config default, split validation.
Schema: id, question, question_concept, choices, answerKey.
"""

from __future__ import annotations

from ..base import DatasetAdapter, JspaceExample


class CommonsenseQAAdapter(DatasetAdapter):
    dataset_id = "commonsenseqa"
    repo = "tau/commonsense_qa"
    config = "default"
    split = "validation"
    task_family = "multiple_choice_commonsense"
    answer_format = "mc_letter"
    prompt_template_id = "mc_letter_v1"
    max_new_tokens = 4
    expected_failure_mode = "commonsense_choice_ambiguity"
    supports_short_answer = False
    supports_multiple_choice = True

    def extract_example(self, raw: dict, *, index: int) -> JspaceExample:
        ch = raw["choices"]   # {"label": [...], "text": [...]}
        labels = ch["label"]
        texts = ch["text"]
        choices = [{"label": lab, "text": txt} for lab, txt in zip(labels, texts)]
        ak = raw.get("answerKey")
        correct_text = None
        if isinstance(ak, str):
            for lab, txt in zip(labels, texts):
                if lab == ak:
                    correct_text = txt
                    break
        return JspaceExample(
            example_id="",
            source_example_id=str(raw.get("id") or f"idx_{index}"),
            question=raw["question"],
            aliases=[correct_text] if correct_text else [],
            choices=choices,
            correct_choice_label=ak,
            correct_choice_text=correct_text,
            metadata={
                "dataset_index": index,
                "question_concept": raw.get("question_concept"),
            },
        )
