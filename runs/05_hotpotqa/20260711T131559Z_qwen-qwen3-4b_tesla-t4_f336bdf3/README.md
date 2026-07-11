# J-Space Run: 01_hallucination_detection

Run ID: `20260711T131559Z_qwen-qwen3-4b_tesla-t4_f336bdf3`

## Purpose

Hallucination detection via J-space state. Implements H.1 and H.3 on the `hotpotqa_distractor` dataset (task family: `multi_hop_factual`).

## Model and runtime

- Model: `Qwen/Qwen3-4B`
- dtype: `torch.bfloat16`
- Lens: `qwen3-4b/jlens/Salesforce-wikitext/Qwen3-4B_jacobian_lens.pt`
- GPU: `Tesla T4`

## Dataset

- Dataset ID: `hotpotqa_distractor`
- Repo: `hotpotqa/hotpot_qa`
- Config: `distractor`
- Split: `validation`
- Prompt template: `short_answer_v1`
- Max new tokens: `16`
- Expected failure mode: `multi_hop_intermediate_uncertainty`

## Summary

| item | value |
| --- | --- |
| model | Qwen/Qwen3-4B |
| run_mode | full |
| dataset_id | hotpotqa_distractor |
| dataset_role | dev |
| n_processed | 2000 |
| n_primary_included | 1880 |
| accuracy_primary | 0.1473404255319149 |
| wrong_rate_primary | 0.8526595744680852 |
| llm_judge_calls | 494 |
| analysis_status_primary | completed |
| conclusion_status | supports_H_C_or_no_signal |
| conclusion | Workspace features did not improve prediction over output confidence under the primary label regime in this run. The single-feature `workspace_noise_score` AUC is 0.704 with CI [0.673, 0.734]; CI overlaps baseline upper bound (0.694), so the parsimonious claim is not statistically distinguishable either. |


## Label regimes

| label_regime | n | n_correct | n_wrong | accuracy |
| --- | --- | --- | --- | --- |
| strict | 2000 | 47 | 1953 | 0.0235 |
| expanded_deterministic | 2000 | 232 | 1768 | 0.116 |
| primary_with_llm_judge | 1880 | 277 | 1603 | 0.1473404255319149 |
| high_quality_primary | 1877 | 277 | 1600 | 0.14757591901971231 |


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
