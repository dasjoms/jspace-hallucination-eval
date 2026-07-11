# J-Space Run: 01_hallucination_detection

Run ID: `20260710T065857Z_qwen-qwen3-4b_tesla-t4_80fb3ced`

## Purpose

Hallucination detection via J-space state. Implements H.1 and H.3 on the `triviaqa_rc_nocontext` dataset (task family: `closed_book_factual_short`).

## Model and runtime

- Model: `Qwen/Qwen3-4B`
- dtype: `torch.bfloat16`
- Lens: `qwen3-4b/jlens/Salesforce-wikitext/Qwen3-4B_jacobian_lens.pt`
- GPU: `Tesla T4`

## Dataset

- Dataset ID: `triviaqa_rc_nocontext`
- Repo: `mandarjoshi/trivia_qa`
- Config: `rc.nocontext`
- Split: `validation`
- Prompt template: `short_answer_v1`
- Max new tokens: `16`
- Expected failure mode: `parametric_recall_uncertainty`

## Summary

| item | value |
| --- | --- |
| model | Qwen/Qwen3-4B |
| run_mode | full |
| dataset_id | triviaqa_rc_nocontext |
| dataset_role | dev |
| n_processed | 2000 |
| n_primary_included | 1955 |
| accuracy_primary | 0.35038363171355497 |
| wrong_rate_primary | 0.649616368286445 |
| llm_judge_calls | 430 |
| analysis_status_primary | completed |
| conclusion_status | supports_H_A_ci_distinguishable |
| conclusion | Combined workspace + confidence features improved AUC over output confidence with non-overlapping 95% bootstrap CIs under the primary label regime, supporting complementary J-space signal. The single-feature `workspace_noise_score` AUC is 0.755 with CI [0.734, 0.777], entirely above the baseline CI's upper bound (0.655) — a cleaner statistical claim than the combined_compact delta. |


## Label regimes

| label_regime | n | n_correct | n_wrong | accuracy |
| --- | --- | --- | --- | --- |
| strict | 2000 | 169 | 1831 | 0.0845 |
| expanded_deterministic | 2000 | 652 | 1348 | 0.326 |
| primary_with_llm_judge | 1955 | 685 | 1270 | 0.35038363171355497 |
| high_quality_primary | 1945 | 685 | 1260 | 0.35218508997429304 |


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
