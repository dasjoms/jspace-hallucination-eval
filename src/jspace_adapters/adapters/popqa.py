"""
Adapter: PopQA (long-tail entity-centric QA).

Dataset: akariasai/PopQA, config default, split test.
Schema: id, subj, prop, obj, subj_id, prop_id, obj_id, s_aliases, o_aliases,
         s_uri, o_uri, s_wiki_title, o_wiki_title, s_pop, o_pop,
         question, possible_answers (string-encoded JSON list).
"""

from __future__ import annotations

import json

from ..base import DatasetAdapter, JspaceExample


class PopQAAdapter(DatasetAdapter):
    dataset_id = "popqa"
    repo = "akariasai/PopQA"
    config = "default"
    split = "test"
    task_family = "closed_book_factual_long_tail"
    answer_format = "short_alias"
    prompt_template_id = "short_answer_v1"
    max_new_tokens = 12
    expected_failure_mode = "long_tail_parametric_recall"
    supports_short_answer = True
    supports_multiple_choice = False

    def extract_example(self, raw: dict, *, index: int) -> JspaceExample:
        q = raw["question"]
        pa = raw.get("possible_answers", [])
        if isinstance(pa, str):
            try:
                pa = json.loads(pa)
            except json.JSONDecodeError:
                pa = [pa]
        aliases = [x for x in pa if isinstance(x, str)]
        return JspaceExample(
            example_id="",
            source_example_id=str(raw.get("id") or f"idx_{index}"),
            question=q,
            aliases=aliases,
            metadata={
                "dataset_index": index,
                "subj": raw.get("subj"),
                "prop": raw.get("prop"),
                "obj": raw.get("obj"),
                # Subject popularity (Wikipedia page-views) is the key
                # meta-analysis feature: stratify by popularity to test
                # whether J-space noise tracks memorization likelihood.
                "s_pop": raw.get("s_pop"),
                "o_pop": raw.get("o_pop"),
                "s_wiki_title": raw.get("s_wiki_title"),
                "o_wiki_title": raw.get("o_wiki_title"),
            },
        )
