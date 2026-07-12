"""
jspace_adapters.labelling — Answer normalization and deterministic matching.

This module contains the dataset-independent labelling helpers, copied and
lightly cleaned from the 02 notebook. The helpers here are deterministic:
they do not call the model. The LLM-judge orchestration stays in the
notebook because it needs the loaded model.

Public API:
  - normalize_answer(s)
  - token_f1(pred, gold)
  - original_text_variants(values)
  - expand_text_variants(values)
  - safe_contains_match(pred_norms, alias_norms)
  - fuzzy_match(pred_norms, alias_norms, threshold)
  - deterministic_label(prediction, aliases)
  - deterministic_label_mc(prediction, example)               [NEW]
  - deterministic_label_with_prefix(prediction, example)     [NEW]
"""

from __future__ import annotations

import re
import string
import unicodedata
import urllib.parse
from collections import Counter
from difflib import SequenceMatcher
from typing import Any

# The exact set of punctuation we strip during normalization, lifted from
# the 02 notebook. Includes curly quotes because TriviaQA / NQ-Open frequently
# contain them in aliases.
TRIVIAQA_PUNCT_EXCLUDE = set(
    string.punctuation
    + "".join(["\u2018", "\u2019", "\u00b4", "`", "\u201c", "\u201d"])
)


# ---------------------------------------------------------------------------
# URL / Unicode / case normalization
# ---------------------------------------------------------------------------

def url_unquote_repeated(s: str, max_rounds: int = 3) -> str:
    """Decode %XX sequences repeatedly. Stops when the string stops changing.

    TriviaQA has aliases like "30%20Rock" that decode to "30 Rock".
    """
    out = str(s)
    for _ in range(max_rounds):
        nxt = urllib.parse.unquote(out)
        if nxt == out:
            break
        out = nxt
    return out


def normalize_answer(s: Any) -> str:
    """TriviaQA/SQuAD-like normalization.

    - Lowercase.
    - Replace underscores with spaces.
    - Strip the configured punctuation set (incl. curly quotes).
    - Drop English articles a/an/the.
    - Collapse whitespace.
    """
    if s is None:
        return ""
    s = unicodedata.normalize("NFKC", url_unquote_repeated(str(s)))
    s = s.replace("_", " ").lower()
    s = "".join(ch if ch not in TRIVIAQA_PUNCT_EXCLUDE else " " for ch in s)
    s = re.sub(r"\b(a|an|the)\b", " ", s)
    return " ".join(s.split()).strip()


# ---------------------------------------------------------------------------
# Token-level F1 (SQuAD-style)
# ---------------------------------------------------------------------------

def token_f1(pred: str, gold: str) -> float:
    """Token F1 between predicted and gold strings, after normalization."""
    pred_toks = normalize_answer(pred).split()
    gold_toks = normalize_answer(gold).split()
    if len(pred_toks) == 0 and len(gold_toks) == 0:
        return 1.0
    if len(pred_toks) == 0 or len(gold_toks) == 0:
        return 0.0
    common = Counter(pred_toks) & Counter(gold_toks)
    num_same = sum(common.values())
    if num_same == 0:
        return 0.0
    precision = num_same / len(pred_toks)
    recall = num_same / len(gold_toks)
    return 2 * precision * recall / (precision + recall)


# ---------------------------------------------------------------------------
# Variant generation (used to build the alias set the labeler matches against)
# ---------------------------------------------------------------------------

def add_variant(variants: list[dict], value: Any, source: str) -> None:
    """Append (value, source) to variants if it normalizes to a non-empty string.

    Variants are dicts with keys: raw, normalized, source.
    """
    if value is None:
        return
    raw = str(value).strip()
    if not raw:
        return
    norm = normalize_answer(raw)
    if not norm:
        return
    variants.append({"raw": raw, "normalized": norm, "source": source})


def plausible_split_part(part: str) -> bool:
    """Used to gate slash/or/parenthetical splits.

    A split is only used if every part normalizes to a string of length >= 3
    that contains at least one alphabetic character. This avoids splitting
    "U.S.A" or "N/A" or "1/2" into garbage.
    """
    norm = normalize_answer(part)
    return len(norm) >= 3 and any(ch.isalpha() for ch in norm)


def original_text_variants(values, *, role: str = "alias_original") -> list[dict]:
    """Original / non-expanded variants for the STRICT label regime.

    Only includes the provided string and a URL-decoded copy when decoding
    changes the text. Does NOT split slash/or/parenthetical aliases.
    """
    variants: list[dict] = []
    for value in values:
        if value is None:
            continue
        raw0 = str(value).strip()
        if not raw0:
            continue
        add_variant(variants, raw0, f"{role}:original")
        raw = url_unquote_repeated(raw0)
        if raw != raw0:
            add_variant(variants, raw, f"{role}:url_unquote")
    out: list[dict] = []
    seen: set[str] = set()
    for v in variants:
        if v["normalized"] not in seen:
            out.append(v)
            seen.add(v["normalized"])
    return out


def expand_text_variants(values, *, role: str = "alias") -> list[dict]:
    """Generate deterministic answer variants without mutating original data.

    Conservative expansions:
      - URL-decode the raw alias
      - Split on "/" if 1 < n_parts <= 3 and all parts are plausible
      - Split on " or " (case-insensitive) under the same constraint
      - Strip parenthetical disambiguators like "(film)" / "(song)" / etc.
      - Split on ";" or "|" under the same constraint
    """
    variants: list[dict] = []
    for value in values:
        if value is None:
            continue
        raw0 = str(value).strip()
        if not raw0:
            continue
        raw = url_unquote_repeated(raw0)
        add_variant(variants, raw0, f"{role}:original")
        if raw != raw0:
            add_variant(variants, raw, f"{role}:url_unquote")

        if "/" in raw and not re.search(r"https?://", raw, flags=re.I):
            parts = [p.strip() for p in raw.split("/")]
            if 1 < len(parts) <= 3 and all(plausible_split_part(p) for p in parts):
                for p in parts:
                    add_variant(variants, p, f"{role}:slash_part")
                add_variant(variants, " ".join(parts), f"{role}:slash_joined")

        if re.search(r"\s+or\s+", raw, flags=re.I):
            parts = re.split(r"\s+or\s+", raw, flags=re.I)
            if 1 < len(parts) <= 3 and all(plausible_split_part(p) for p in parts):
                for p in parts:
                    add_variant(variants, p, f"{role}:or_part")

        m = re.match(
            r"^(.+?)\s*\((disambiguation|film|song|musical|tv series|novel|book|album)\)\s*$",
            raw, flags=re.I,
        )
        if m and plausible_split_part(m.group(1)):
            add_variant(variants, m.group(1), f"{role}:parenthetical_strip")

        if any(sep in raw for sep in [";", "|"]):
            parts = re.split(r"[;|]", raw)
            if 1 < len(parts) <= 4 and all(plausible_split_part(p) for p in parts):
                for p in parts:
                    add_variant(variants, p, f"{role}:list_part")

    out: list[dict] = []
    seen: set[str] = set()
    for v in variants:
        if v["normalized"] not in seen:
            out.append(v)
            seen.add(v["normalized"])
    return out


# ---------------------------------------------------------------------------
# Containment / fuzzy matching
# ---------------------------------------------------------------------------

def safe_contains_match(pred_norms: list[str], alias_norms: list[str]):
    """Token-boundary phrase containment match.

    Returns (matched: bool, info: dict | None). Skips very short strings
    (< 4 chars) to avoid spurious "the"/"of"/"in" matches.
    """
    for p in pred_norms:
        for a in alias_norms:
            if not p or not a:
                continue
            if len(p) < 4 and len(a) < 4:
                continue
            if len(p) >= 4 and re.search(rf"(^|\s){re.escape(p)}($|\s)", a):
                return True, {"prediction": p, "alias": a, "direction": "prediction_in_alias"}
            if len(a) >= 4 and re.search(rf"(^|\s){re.escape(a)}($|\s)", p):
                return True, {"prediction": p, "alias": a, "direction": "alias_in_prediction"}
    return False, None


def fuzzy_match(pred_norms: list[str], alias_norms: list[str], threshold: float = 0.92):
    """SequenceMatcher ratio. Returns (matched, info).

    Note: fuzzy matches are NOT auto-accepted by default in
    deterministic_label; they trigger the LLM-judge path in the notebook.
    """
    best = {"ratio": 0.0, "prediction": None, "alias": None}
    for p in pred_norms:
        for a in alias_norms:
            if len(p) < 4 or len(a) < 4:
                continue
            ratio = SequenceMatcher(None, p, a).ratio()
            if ratio > best["ratio"]:
                best = {"ratio": ratio, "prediction": p, "alias": a}
    return best["ratio"] >= threshold, best


# ---------------------------------------------------------------------------
# Prediction-side helpers
# ---------------------------------------------------------------------------

def prediction_variants(prediction: str):
    """Build the set of normalized forms the prediction can take.

    Strips common prefixes (The answer is:, Answer:, It is, It's) and any
    surrounding quotes, then runs the standard expand_text_variants.
    """
    vals: list[str] = []
    pred = "" if prediction is None else str(prediction).strip()
    vals.append(pred)
    vals.append(re.sub(r"^(the\s+answer\s+is|answer\s*:|it\s+is|it's)\s+", "", pred, flags=re.I).strip())
    if pred.startswith('"') and pred.endswith('"'):
        vals.append(pred.strip('"'))
    return expand_text_variants(vals, role="prediction")


# ---------------------------------------------------------------------------
# Main deterministic labeler
# ---------------------------------------------------------------------------

def deterministic_label(prediction: str, aliases: list[str]) -> dict:
    """Score a prediction against an alias set.

    Returns a dict with the same shape the 02 notebook expects so the rest
    of the pipeline (LLM-judge path, per-example metrics) is unchanged.
    """
    original_alias_variants = original_text_variants(aliases, role="alias_original_only")
    expanded_alias_variants = expand_text_variants(aliases, role="alias")
    pred_variants = prediction_variants(prediction)
    original_alias_norms = [v["normalized"] for v in original_alias_variants]
    expanded_alias_norms = [v["normalized"] for v in expanded_alias_variants]
    pred_norms = [v["normalized"] for v in pred_variants]
    primary_pred_norm = pred_norms[0] if pred_norms else normalize_answer(prediction)

    # Safety assertion: strict variants must not include expansion-derived sources.
    expanded_sources = [
        v for v in original_alias_variants
        if any(tag in v.get("source", "") for tag in [
            "slash_part", "or_part", "list_part", "parenthetical_strip", "slash_joined"
        ])
    ]
    if expanded_sources:
        raise AssertionError(
            f"Strict alias variants contain expanded sources: {expanded_sources[:3]}"
        )

    strict_exact = any(primary_pred_norm == a for a in original_alias_norms)
    expanded_exact = any(p == a for p in pred_norms for a in expanded_alias_norms)
    contains_ok, contains_info = safe_contains_match(pred_norms, expanded_alias_norms)
    fuzzy_suggested, fuzzy_info = fuzzy_match(pred_norms, expanded_alias_norms, threshold=0.92)
    f1s = [token_f1(primary_pred_norm, a) for a in expanded_alias_norms] or [0.0]
    f1_max = float(max(f1s))

    deterministic_correct = bool(strict_exact or expanded_exact or contains_ok)
    if strict_exact:
        source, quality = "strict_exact", "high"
    elif expanded_exact:
        source, quality = "expanded_exact", "high"
    elif contains_ok:
        source, quality = "safe_contains", "medium"
    else:
        source, quality = "deterministic_no_match", "high"

    alias_has_alternative_sep = any(
        ("/" in str(a) or re.search(r"\s+or\s+", str(a), flags=re.I))
        for a in aliases
    )
    return {
        "normalized_prediction": primary_pred_norm,
        "original_alias_variants": original_alias_variants,
        "expanded_alias_variants": expanded_alias_variants,
        "prediction_variants": pred_variants,
        "normalized_aliases": expanded_alias_norms,
        "strict_correct": bool(strict_exact),
        "expanded_exact_correct": bool(expanded_exact),
        "safe_contains_correct": bool(contains_ok),
        "safe_contains_info": contains_info,
        "fuzzy_suggested": bool(fuzzy_suggested),
        "fuzzy_auto_accept": False,
        "fuzzy_info": fuzzy_info,
        "deterministic_correct": deterministic_correct,
        "deterministic_label_source": source,
        "deterministic_label_quality": quality,
        "token_f1_max": f1_max,
        "alias_has_alternative_sep": bool(alias_has_alternative_sep),
    }


# ---------------------------------------------------------------------------
# New: deterministic_label_with_prefix (TruthfulQA, see plan §6.4)
# ---------------------------------------------------------------------------

def deterministic_label_with_prefix(prediction: str, example) -> dict:
    """TruthfulQA-friendly deterministic labeler.

    Runs the standard deterministic_label first. If that says no-match,
    AND the example.metadata has allow_prefix_match=True, AND the first
    1 or 2 normalized words of the prediction appear as a prefix of any
    alias (after normalization), accept it.

    The 1-2 word length and the >= 4 normalized char length filter prevent
    spurious matches on articles ("the", "a") and very short predictions.
    """
    base = deterministic_label(prediction, example.aliases)
    if base["deterministic_correct"]:
        base["label_regime"] = "strict"  # marker; even if base matched, we used strict
        return base
    if not example.metadata.get("allow_prefix_match", False):
        base["label_regime"] = "strict"
        return base
    pred_tokens = normalize_answer(prediction).split()
    if not pred_tokens:
        base["label_regime"] = "strict"
        return base
    for n_words in (1, 2):
        if len(pred_tokens) < n_words:
            continue
        pred_prefix = " ".join(pred_tokens[:n_words])
        if len(pred_prefix) < 4:
            continue
        for alias in example.aliases:
            alias_tokens = normalize_answer(alias).split()
            if len(alias_tokens) < n_words:
                continue
            alias_prefix = " ".join(alias_tokens[:n_words])
            if pred_prefix == alias_prefix:
                base["strict_correct"] = True
                base["deterministic_correct"] = True
                base["deterministic_label_source"] = f"prefix_match_n{n_words}"
                base["deterministic_label_quality"] = "medium"
                base["prefix_match_n_words"] = n_words
                base["label_regime"] = "prefix_match"
                return base
    base["label_regime"] = "strict"
    return base


# ---------------------------------------------------------------------------
# New: deterministic_label_mc (CommonsenseQA, see plan §6.3)
# ---------------------------------------------------------------------------

# Match a single letter A-E (case-insensitive) anywhere in the parsed output.
_MC_LETTER_RE = re.compile(r"\b([A-E])\b", re.IGNORECASE)


def parse_mc_letter(raw_text: str) -> str | None:
    """Extract the first A-E letter from a model's raw text output.

    Strips common prefixes (The answer is:, Answer:, It is) first. Returns
    None if no letter is found.
    """
    if not raw_text:
        return None
    s = raw_text.strip()
    s = re.sub(r"^(the\s+answer\s+is|answer\s*:|it\s+is|it's)\s+", "", s, flags=re.I).strip()
    m = _MC_LETTER_RE.search(s)
    return m.group(1).upper() if m else None


def deterministic_label_mc(prediction: str | None, example) -> dict:
    """Score a multiple-choice prediction against an example.

    The prediction is the model's raw text output (or a pre-extracted letter).
    We try (in order):
      1. Parse the first A-E letter.
      2. If that fails, normalize the prediction and check exact match
         against the correct choice text.
    """
    correct_letter = example.correct_choice_label
    valid_letters = {c["label"] for c in (example.choices or [])}
    correct_text = example.correct_choice_text or ""

    pred_letter = None
    if prediction:
        # If the prediction is already a single letter, use it directly.
        s = prediction.strip()
        if len(s) <= 4 and s.upper() in valid_letters:
            pred_letter = s.upper()
        else:
            pred_letter = parse_mc_letter(prediction)

    if pred_letter is not None and pred_letter in valid_letters:
        is_correct = (pred_letter == correct_letter)
        return _mc_result(
            pred_letter, example,
            source="mc_letter_exact" if is_correct else "mc_letter_mismatch",
            is_correct=is_correct,
        )

    # Fallback: did the model output the choice text directly?
    if prediction and correct_text and normalize_answer(prediction) == normalize_answer(correct_text):
        return _mc_result(
            correct_letter, example, source="mc_text_match", is_correct=True
        )

    return _mc_result(
        pred_letter, example,
        source="mc_no_letter" if pred_letter is None else "mc_letter_mismatch",
        is_correct=False,
    )


def _mc_result(pred_letter, example, *, source: str, is_correct: bool) -> dict:
    """Build the result dict for deterministic_label_mc. Mirrors the
    field set that deterministic_label returns, so downstream code can
    treat MC and short-answer examples uniformly.
    """
    correct_text = example.correct_choice_text or ""
    return {
        # Match fields
        "strict_correct": is_correct,
        "expanded_exact_correct": is_correct,
        "safe_contains_correct": is_correct,
        "deterministic_correct": is_correct,
        "deterministic_label_source": source,
        "deterministic_label_quality": "high",
        "token_f1_max": 1.0 if is_correct else 0.0,
        "alias_has_alternative_sep": False,
        # MC-specific fields
        "predicted_letter": pred_letter,
        "correct_letter": example.correct_choice_label,
        "correct_text": correct_text,
        # Pad to match deterministic_label shape (so the rest of the pipeline
        # can call .get() without crashing if it touches these).
        "normalized_prediction": pred_letter or "",
        "original_alias_variants": [],
        "expanded_alias_variants": [],
        "prediction_variants": [],
        "normalized_aliases": [normalize_answer(correct_text)] if correct_text else [],
        "fuzzy_suggested": False,
        "fuzzy_auto_accept": False,
        # Label regime marker for the main loop
        "label_regime": "mc_letter",
    }
