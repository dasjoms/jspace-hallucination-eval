# J-Space Run: 01_hallucination_detection

Run ID: `20260710T212032Z_qwen-qwen3-4b_tesla-t4_e5b70040`

## Purpose

Hallucination detection via J-space state. Implements H.1 and H.3 on the `nq_open` dataset (task family: `closed_book_factual_short`).

## Model and runtime

- Model: `Qwen/Qwen3-4B`
- dtype: `torch.bfloat16`
- Lens: `qwen3-4b/jlens/Salesforce-wikitext/Qwen3-4B_jacobian_lens.pt`
- GPU: `Tesla T4`

## Dataset

- Dataset ID: `nq_open`
- Repo: `google-research-datasets/nq_open`
- Config: `nq_open`
- Split: `validation`
- Prompt template: `short_answer_v1`
- Max new tokens: `16`
- Expected failure mode: `parametric_recall_uncertainty`

## Summary

| item | value |
| --- | --- |
| model | Qwen/Qwen3-4B |
| run_mode | full |
| dataset_id | nq_open |
| dataset_role | dev |
| n_processed | 2000 |
| n_primary_included | 1810 |
| accuracy_primary | 0.20939226519337018 |
| wrong_rate_primary | 0.7906077348066298 |
| llm_judge_calls | 614 |
| analysis_status_primary | completed |
| conclusion_status | supports_H_C_or_no_signal |
| conclusion | Workspace features did not improve prediction over output confidence under the primary label regime in this run. The single-feature `workspace_noise_score` AUC is 0.718 with CI [0.691, 0.746]; CI overlaps baseline upper bound (0.747), so the parsimonious claim is not statistically distinguishable either. |


## Label regimes

| label_regime | n | n_correct | n_wrong | accuracy |
| --- | --- | --- | --- | --- |
| strict | 2000 | 34 | 1966 | 0.017 |
| expanded_deterministic | 2000 | 303 | 1697 | 0.1515 |
| primary_with_llm_judge | 1810 | 379 | 1431 | 0.20939226519337018 |
| high_quality_primary | 1807 | 379 | 1428 | 0.2097399003873824 |


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
