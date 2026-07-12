"""
Adapter: GSM8K (grade-school math word problems).

Dataset: openai/gsm8k, config main, split test.
Schema: question, answer (string ending in '#### <number>').

Special handling:
  - Extract the gold number from the '#### N' line.
  - max_new_tokens=200 (NOT 16!) to allow the model to compute internally
    before producing the final 'Answer: N' line. See plan §0.2.
  - full_solution preserved in metadata for the LLM-judge fallback and
    selected-example reports.
"""

from __future__ import annotations

import re

from ..base import DatasetAdapter, JspaceExample


_GSM8K_GOLD_RE = re.compile(r"####\s*([-+]?[\d.,]+)")


class GSM8KAdapter(DatasetAdapter):
    dataset_id = "gsm8k"
    repo = "openai/gsm8k"
    config = "main"
    split = "test"
    task_family = "numeric_reasoning_short"
    answer_format = "numeric"
    prompt_template_id = "numeric_v1"
    max_new_tokens = 200
    expected_failure_mode = "multi_step_arithmetic_failure"
    supports_short_answer = True
    supports_multiple_choice = False

    def extract_example(self, raw: dict, *, index: int) -> JspaceExample:
        ans = raw.get("answer", "")
        gold: str | None = None
        if isinstance(ans, str):
            m = _GSM8K_GOLD_RE.search(ans)
            if m:
                # Strip thousands separators for canonical form.
                gold = m.group(1).replace(",", "")
        if gold is None and isinstance(ans, str):
            # Last resort: take whatever is after the last '####'
            gold = ans.split("####")[-1].strip()
        return JspaceExample(
            example_id="",
            source_example_id=f"gsm8k_test_{index}",
            question=raw["question"],
            aliases=[gold] if gold else [],
            metadata={
                "dataset_index": index,
                "full_solution": ans,
            },
        )
