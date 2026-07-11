# J-Space Run: 01_hallucination_detection

Run ID: `20260711T153533Z_qwen-qwen3-4b_tesla-t4_c2a84052`

## Purpose

Hallucination detection via J-space state. Implements H.1 and H.3 on the `gsm8k` dataset (task family: `numeric_reasoning_short`).

## Model and runtime

- Model: `Qwen/Qwen3-4B`
- dtype: `torch.bfloat16`
- Lens: `qwen3-4b/jlens/Salesforce-wikitext/Qwen3-4B_jacobian_lens.pt`
- GPU: `Tesla T4`

## Dataset

- Dataset ID: `gsm8k`
- Repo: `openai/gsm8k`
- Config: `main`
- Split: `test`
- Prompt template: `numeric_v1`
- Max new tokens: `200`
- Expected failure mode: `multi_step_arithmetic_failure`

## Summary

| item | value |
| --- | --- |
| model | Qwen/Qwen3-4B |
| run_mode | full |
| dataset_id | gsm8k |
| dataset_role | dev |
| n_processed | 1319 |
| n_primary_included | 1269 |
| accuracy_primary | 0.22537431048069345 |
| wrong_rate_primary | 0.7746256895193065 |
| llm_judge_calls | 348 |
| analysis_status_primary | completed |
| conclusion_status | supports_H_B_or_redundant |
| conclusion | Workspace features did not materially improve over output confidence under the primary label regime; signals may be redundant for this model/dataset. The single-feature `workspace_noise_score` AUC is 0.744 with CI [0.714, 0.775]; CI overlaps baseline upper bound (0.836), so the parsimonious claim is not statistically distinguishable either. |


## Label regimes

| label_regime | n | n_correct | n_wrong | accuracy |
| --- | --- | --- | --- | --- |
| strict | 1319 | 251 | 1068 | 0.19029567854435178 |
| expanded_deterministic | 1319 | 259 | 1060 | 0.19636087945413191 |
| primary_with_llm_judge | 1269 | 286 | 983 | 0.22537431048069345 |
| high_quality_primary | 1268 | 286 | 982 | 0.22555205047318613 |


## Key artefacts

- `AGENT_BRIEF.md`
- `FULL_REPORT.md`
- `datasets/dataset_manifest.json`
- `datasets/questions.jsonl`
- `generations/generations.jsonl`
- `scans/workspace_aggregate_features.csv`
- `scans/workspace_layer_features.csv`
- `metrics/per_example_metrics.csv`
- `metrics/auc_scores.csv`
- `metrics/auc_bootstrap_ci.csv`
- `metrics/auc_permutation_sanity.csv`
- `metrics/quadrant_analysis.csv`
- `examples/confident_wrong_noisy.md`
- `examples/confident_wrong_clean_blindspots.md`

## Caveats

- Correctness labels are automatic alias-based labels and may be noisy.
- Full vocabulary logits and residual streams are not saved by default.
- Workspace noise is measured with top-50 entropy over selected workspace layers.
- CSV readers should use `keep_default_na=False` if exact string values such as "None" matter; JSONL files are authoritative for text fields.
