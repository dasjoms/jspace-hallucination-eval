"""
Adapter: TriviaQA-rc.nocontext (the original baseline).

Dataset: mandarjoshi/trivia_qa, config rc.nocontext, split validation.
Schema: question, question_id, question_source, entity_pages, search_results,
         answer (nested dict with value, aliases, normalized_aliases,
         human_answers, matched_wiki_entity_name, ...)
"""

from __future__ import annotations

from ..base import DatasetAdapter, JspaceExample


class TriviaQARcNoContextAdapter(DatasetAdapter):
    dataset_id = "triviaqa_rc_nocontext"
    repo = "mandarjoshi/trivia_qa"
    config = "rc.nocontext"
    split = "validation"
    task_family = "closed_book_factual_short"
    answer_format = "short_alias"
    prompt_template_id = "short_answer_v1"
    max_new_tokens = 16
    expected_failure_mode = "parametric_recall_uncertainty"
    supports_short_answer = True
    supports_multiple_choice = False

    def extract_example(self, raw: dict, *, index: int) -> JspaceExample:
        q = raw["question"]
        ans = raw["answer"]   # nested dict
        aliases: list[str] = []
        for sub in [
            "value",
            "aliases",
            "normalized_aliases",
            "human_answers",
            "matched_wiki_entity_name",
            "normalized_matched_wiki_entity_name",
        ]:
            v = ans.get(sub)
            if isinstance(v, str):
                aliases.append(v)
            elif isinstance(v, (list, tuple)):
                aliases.extend(x for x in v if isinstance(x, str))
        return JspaceExample(
            example_id="",
            source_example_id=str(raw.get("question_id") or f"idx_{index}"),
            question=q,
            aliases=aliases,
            metadata={
                "dataset_index": index,
                "question_source": raw.get("question_source"),
            },
        )
