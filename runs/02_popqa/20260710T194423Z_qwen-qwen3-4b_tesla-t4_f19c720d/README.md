# J-Space Run: 01_hallucination_detection

Run ID: `20260710T194423Z_qwen-qwen3-4b_tesla-t4_f19c720d`

## Purpose

Hallucination detection via J-space state. Implements H.1 and H.3 on the `popqa` dataset (task family: `closed_book_factual_long_tail`).

## Model and runtime

- Model: `Qwen/Qwen3-4B`
- dtype: `torch.bfloat16`
- Lens: `qwen3-4b/jlens/Salesforce-wikitext/Qwen3-4B_jacobian_lens.pt`
- GPU: `Tesla T4`

## Dataset

- Dataset ID: `popqa`
- Repo: `akariasai/PopQA`
- Config: `default`
- Split: `test`
- Prompt template: `short_answer_v1`
- Max new tokens: `12`
- Expected failure mode: `long_tail_parametric_recall`

## Summary

| item | value |
| --- | --- |
| model | Qwen/Qwen3-4B |
| run_mode | full |
| dataset_id | popqa |
| dataset_role | dev |
| n_processed | 2000 |
| n_primary_included | 1969 |
| accuracy_primary | 0.09395632300660234 |
| wrong_rate_primary | 0.9060436769933977 |
| llm_judge_calls | 190 |
| analysis_status_primary | completed |
| conclusion_status | supports_H_C_or_no_signal |
| conclusion | Workspace features did not improve prediction over output confidence under the primary label regime in this run. The single-feature `workspace_noise_score` AUC is 0.839 with CI [0.807, 0.869]; CI overlaps baseline upper bound (0.850), so the parsimonious claim is not statistically distinguishable either. |


## Label regimes

| label_regime | n | n_correct | n_wrong | accuracy |
| --- | --- | --- | --- | --- |
| strict | 2000 | 45 | 1955 | 0.0225 |
| expanded_deterministic | 2000 | 177 | 1823 | 0.0885 |
| primary_with_llm_judge | 1969 | 185 | 1784 | 0.09395632300660234 |
| high_quality_primary | 1968 | 185 | 1783 | 0.09400406504065041 |


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
