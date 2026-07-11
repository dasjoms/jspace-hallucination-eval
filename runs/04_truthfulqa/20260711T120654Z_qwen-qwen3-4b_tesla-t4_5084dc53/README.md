# J-Space Run: 01_hallucination_detection

Run ID: `20260711T120654Z_qwen-qwen3-4b_tesla-t4_5084dc53`

## Purpose

Hallucination detection via J-space state. Implements H.1 and H.3 on the `truthfulqa_gen` dataset (task family: `adversarial_truthfulness_short`).

## Model and runtime

- Model: `Qwen/Qwen3-4B`
- dtype: `torch.bfloat16`
- Lens: `qwen3-4b/jlens/Salesforce-wikitext/Qwen3-4B_jacobian_lens.pt`
- GPU: `Tesla T4`

## Dataset

- Dataset ID: `truthfulqa_gen`
- Repo: `truthfulqa/truthful_qa`
- Config: `generation`
- Split: `validation`
- Prompt template: `short_answer_v1`
- Max new tokens: `32`
- Expected failure mode: `imitative_misconception_hallucination`

## Summary

| item | value |
| --- | --- |
| model | Qwen/Qwen3-4B |
| run_mode | full |
| dataset_id | truthfulqa_gen |
| dataset_role | dev |
| n_processed | 814 |
| n_primary_included | 748 |
| accuracy_primary | 0.08689839572192513 |
| wrong_rate_primary | 0.9131016042780749 |
| llm_judge_calls | 184 |
| analysis_status_primary | completed |
| conclusion_status | supports_H_B_or_redundant |
| conclusion | Workspace features did not materially improve over output confidence under the primary label regime; signals may be redundant for this model/dataset. The single-feature `workspace_noise_score` AUC is 0.617 with CI [0.534, 0.691]; CI overlaps baseline upper bound (0.803), so the parsimonious claim is not statistically distinguishable either. |


## Label regimes

| label_regime | n | n_correct | n_wrong | accuracy |
| --- | --- | --- | --- | --- |
| strict | 814 | 13 | 801 | 0.01597051597051597 |
| expanded_deterministic | 814 | 41 | 773 | 0.05036855036855037 |
| primary_with_llm_judge | 748 | 65 | 683 | 0.08689839572192513 |
| high_quality_primary | 748 | 65 | 683 | 0.08689839572192513 |


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
