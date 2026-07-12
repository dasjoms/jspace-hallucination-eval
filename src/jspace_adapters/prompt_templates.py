"""
jspace_adapters.prompt_templates — The 3 prompt templates for the first sweep.

Each template is a (builder, parser) pair registered by template_id. The
adapter declares which template_id to use; the main loop never picks.

Public API:
  - get_template(template_id) -> PromptTemplate
  - list_template_ids() -> list[str]
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from .base import JspaceExample


# ---------------------------------------------------------------------------
# Parser implementations
# ---------------------------------------------------------------------------

def parse_short_answer(raw_text: str) -> str:
    """For short_answer_v1: return the first non-empty line, stripped of
    common prefixes and trailing punctuation.
    """
    text = (raw_text or "").strip()
    if not text:
        return ""
    text = text.splitlines()[0] if text.splitlines() else text
    text = re.sub(
        r"^(the\s+answer\s+is|answer\s*:|it\s+is|it's)\s+",
        "", text, flags=re.IGNORECASE,
    ).strip()
    return text.strip().strip(" .,:;!?\\\"'`\u201c\u201d\u2018\u2019()[]{}")


_MC_LETTER_RE = re.compile(r"\b([A-E])\b", re.IGNORECASE)


def parse_mc_letter(raw_text: str) -> str | None:
    """For mc_letter_v1: return the first A-E letter found in the text, or
    None. Common prefixes are stripped first.
    """
    if not raw_text:
        return None
    s = raw_text.strip()
    s = re.sub(r"^(the\s+answer\s+is|answer\s*:|it\s+is|it's)\s+", "", s, flags=re.I).strip()
    m = _MC_LETTER_RE.search(s)
    return m.group(1).upper() if m else None


_ANSWER_PREFIX_RE = re.compile(r"(?im)^\s*answer\s*:\s*(.+)$")
_NUM_RE = re.compile(r"[-+]?\d[\d,]*(?:\.\d+)?")


def _normalize_number(s: str) -> str:
    """Strip thousands separators; treat 42.0 and 42 as the same canonical form."""
    s = s.replace(",", "")
    if "." in s:
        try:
            f = float(s)
            if f == int(f):
                return str(int(f))
            return s
        except ValueError:
            return s
    return s


def parse_numeric(raw_text: str) -> str | None:
    """For numeric_v1: extract the final number on the 'Answer: ...' line,
    or fall back to the last number anywhere in the response.
    """
    text = (raw_text or "").strip()
    if not text:
        return None
    lines = text.splitlines()
    for line in reversed(lines):
        m = _ANSWER_PREFIX_RE.search(line)
        if m:
            tail = m.group(1).strip()
            nums = _NUM_RE.findall(tail)
            if nums:
                return _normalize_number(nums[-1])
    nums = _NUM_RE.findall(text)
    if nums:
        return _normalize_number(nums[-1])
    return None


# ---------------------------------------------------------------------------
# Builder implementations
# ---------------------------------------------------------------------------

def build_short_answer(example: JspaceExample, *, tokenizer=None) -> str:
    """short_answer_v1: 'Reply with only the short answer. Question: {q}'"""
    user_content = (
        "You are answering a trivia question. Reply with only the short answer. "
        "Do not explain.\n\n"
        f"Question: {example.question}"
    )
    if tokenizer is not None:
        try:
            messages = [{"role": "user", "content": user_content}]
            return tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            # Tokenizer doesn't support enable_thinking kwarg
            return tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        except Exception:
            return user_content + "\nAnswer: "
    return user_content + "\nAnswer: "


def build_mc_letter(example: JspaceExample, *, tokenizer=None) -> str:
    """mc_letter_v1: 'Reply with only the letter (A, B, C, D, E). ...'"""
    choices = example.choices or []
    if not choices:
        # Defensive fallback: build a short_answer prompt.
        return build_short_answer(example, tokenizer=tokenizer)
    letters = [c["label"] for c in choices]
    options = "\n".join(f"{c['label']}) {c['text']}" for c in choices)
    user_content = (
        f"You are answering a multiple-choice question. "
        f"Reply with only the letter of the correct answer ({', '.join(letters)}). "
        f"Do not explain.\n\n"
        f"Question: {example.question}\n{options}"
    )
    if tokenizer is not None:
        try:
            messages = [{"role": "user", "content": user_content}]
            return tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            return tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        except Exception:
            return user_content + "\nAnswer: "
    return user_content + "\nAnswer: "


def build_numeric(example: JspaceExample, *, tokenizer=None) -> str:
    """numeric_v1: 'Solve in your head, then reply with only the final number
    on the last line prefixed with "Answer: ".'"""
    user_content = (
        "You are answering a grade-school math word problem. "
        "Solve it step by step in your head, then reply with only the final number "
        "on the last line, prefixed with \"Answer: \". Do not explain.\n\n"
        f"Question: {example.question}"
    )
    if tokenizer is not None:
        try:
            messages = [{"role": "user", "content": user_content}]
            return tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            return tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        except Exception:
            return user_content + "\nAnswer: "
    return user_content + "\nAnswer: "


# ---------------------------------------------------------------------------
# Template registry
# ---------------------------------------------------------------------------

@dataclass
class PromptTemplate:
    template_id: str
    description: str
    build: Callable[[JspaceExample], str]
    parse: Callable[[str], Any]               # returns str | str | None depending on template
    answer_extraction_policy: str
    max_new_tokens_recommended: int


TEMPLATES: dict[str, PromptTemplate] = {
    "short_answer_v1": PromptTemplate(
        template_id="short_answer_v1",
        description="Short free-form answer (TriviaQA, NQ-Open, PopQA, HotpotQA, TruthfulQA).",
        build=build_short_answer,
        parse=parse_short_answer,
        answer_extraction_policy="first_line_strip_prefixes_v1",
        max_new_tokens_recommended=16,
    ),
    "mc_letter_v1": PromptTemplate(
        template_id="mc_letter_v1",
        description="Multiple-choice letter answer (CommonsenseQA, ARC, MMLU).",
        build=build_mc_letter,
        parse=parse_mc_letter,
        answer_extraction_policy="first_letter_A_to_Z_v1",
        max_new_tokens_recommended=4,
    ),
    "numeric_v1": PromptTemplate(
        template_id="numeric_v1",
        description="Numeric answer with 'Answer: <N>' prefix on last line (GSM8K).",
        build=build_numeric,
        parse=parse_numeric,
        answer_extraction_policy="last_line_answer_prefix_then_last_number_v1",
        max_new_tokens_recommended=200,
    ),
}


def get_template(template_id: str) -> PromptTemplate:
    if template_id not in TEMPLATES:
        raise KeyError(
            f"Unknown prompt template {template_id!r}. "
            f"Available: {sorted(TEMPLATES.keys())}"
        )
    return TEMPLATES[template_id]


def list_template_ids() -> list[str]:
    return sorted(TEMPLATES.keys())
