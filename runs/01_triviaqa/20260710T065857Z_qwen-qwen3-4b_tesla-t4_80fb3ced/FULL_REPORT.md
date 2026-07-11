# Full Report — Hallucination Detection via J-Space State

## Research question

Do J-space activation patterns at answer time predict factual-answer correctness beyond output confidence?

## Configuration

```json
{
  "EXPERIMENT_ID": "01_hallucination_detection",
  "EXPERIMENT_NAME": "Hallucination Detection via J-Space State",
  "NOTEBOOK_VERSION": "2.2.1",
  "ARTIFACT_SCHEMA_VERSION": "jspace_artifacts_v1",
  "DATASET_ID": "triviaqa_rc_nocontext",
  "DATASET_ROLE": "dev",
  "MODEL_NAME": "Qwen/Qwen3-4B",
  "MODEL_DTYPE": "auto",
  "PREFITTED_LENS_REPO": "neuronpedia/jacobian-lens",
  "ALLOW_FALLBACK_FIT": false,
  "RUN_MODE": "full",
  "N_EXAMPLES_PILOT": 50,
  "N_EXAMPLES_FULL": 2000,
  "RANDOM_SEED": 42,
  "SAVE_EVERY": 10,
  "MAX_SEQ_LEN": 512,
  "WORKSPACE_LAYER_FRAC_START": 0.35,
  "WORKSPACE_LAYER_FRAC_END": 0.99,
  "MID_WORKSPACE_FRAC_START": 0.45,
  "MID_WORKSPACE_FRAC_END": 0.75,
  "LATE_WORKSPACE_FRAC_START": 0.75,
  "LATE_WORKSPACE_FRAC_END": 0.99,
  "LATE_LATE_WORKSPACE_FRAC_START": 0.85,
  "LATE_LATE_WORKSPACE_FRAC_END": 0.99,
  "COMMITMENT_LOOKBACK_LAYERS": 3,
  "LAYER_L33_TARGET_LAYER": 33,
  "LAYER_L34_TARGET_LAYER": 34,
  "LAYER_STRIDE": 1,
  "FEATURE_TOP_K": 50,
  "TOP_TOKENS_TO_SAVE": 5,
  "COMPUTE_FULL_WORKSPACE_ENTROPY": false,
  "COMPUTE_FULL_WORKSPACE_PROBS": false,
  "PIN_LENS_TO_GPU": "auto",
  "USE_LLM_LABEL_JUDGE": true,
  "LABEL_JUDGE_MAX_NEW_TOKENS": 192,
  "LABEL_JUDGE_CONFIDENCE_THRESHOLD": 0.85,
  "LABEL_JUDGE_F1_THRESHOLD": 0.5,
  "LABEL_JUDGE_ACCEPT_CONFIDENCES": [
    "high",
    "medium"
  ],
  "LABEL_JUDGE_REJECT_AMBIGUOUS_FROM_PRIMARY": true,
  "EXCLUDE_TEMPORAL_UNSTABLE_FROM_PRIMARY": true,
  "TEMPORAL_UNSTABLE_REGEX": "\\b(current|currently|today|recently|this year|latest)\\b",
  "FUZZY_AUTO_ACCEPT": false,
  "FUZZY_MATCH_THRESHOLD": 0.92,
  "LLM_JUDGE_SKIP_HIGH_CONF_WRONG": false,
  "CV_FOLDS": 5,
  "HIGH_CONFIDENCE_QUANTILE": 0.5,
  "NOISY_WORKSPACE_QUANTILE": 0.5,
  "MIN_CLASS_COUNT_FOR_CV": 5,
  "SELECTED_EXAMPLES_PER_BUCKET": 10,
  "BOOTSTRAP_N": 1000,
  "PERMUTATION_N": 500,
  "USE_GOOGLE_DRIVE": true,
  "MOUNT_GOOGLE_DRIVE": true,
  "DRIVE_ARTIFACT_ROOT": "/content/drive/MyDrive/J-Space_Artifacts",
  "LOCAL_ARTIFACT_ROOT": "J-Space_Artifacts",
  "SOURCE_NOTEBOOK_PATH": null,
  "SAVE_NOTEBOOK_COPY": true,
  "STORE_FULL_PROMPTS": true,
  "STORE_FULL_OUTPUTS": true,
  "STORE_SELECTED_EXAMPLES_TEXT": true,
  "VERBOSE_EXAMPLES": true,
  "USE_DISPLAY_FILTERS": false,
  "FILTER_SPECIAL_TOKENS": true,
  "FILTER_WHITESPACE_ONLY": true,
  "FILTER_PUNCTUATION_ONLY": true,
  "FILTER_NONPRINTABLE": true,
  "N_EXAMPLES": 2000,
  "artifact_storage_note": "google_drive"
}
```

## Dataset

- Dataset ID: `triviaqa_rc_nocontext`
- Repo: `mandarjoshi/trivia_qa`
- Config: `rc.nocontext`
- Split: `validation`
- Task family: `closed_book_factual_short`
- Prompt template: `short_answer_v1`

```json
{
  "dataset_id": "triviaqa_rc_nocontext",
  "repo": "mandarjoshi/trivia_qa",
  "config": "rc.nocontext",
  "split": "validation",
  "task_family": "closed_book_factual_short",
  "answer_format": "short_alias",
  "prompt_template_id": "short_answer_v1",
  "max_new_tokens": 16,
  "n_total_in_split": 17944,
  "n_requested": 2000,
  "random_seed": 42,
  "expected_failure_mode": "parametric_recall_uncertainty",
  "supports_short_answer": true,
  "supports_multiple_choice": false,
  "n_kept_after_dedup": 2000,
  "n_selected": 2000,
  "examples_with_aliases": 2000,
  "examples_with_choices": 0,
  "run_mode": "full",
  "dataset_role": "dev"
}
```

## Aggregate summary

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


## Descriptive statistics

| feature | mean_correct | mean_wrong | std_correct | std_wrong | cohen_d_wrong_minus_correct |
| --- | --- | --- | --- | --- | --- |
| first_content_token_prob | 0.6645332817939946 | 0.6200606253206871 | 0.21878459709164197 | 0.22103515778625676 | -0.20192049881679566 |
| sequence_content_logprob_mean | -0.2545998236669857 | -0.3241863682417865 | 0.11133615117003373 | 0.1583488141961784 | -0.48451405740372366 |
| workspace_noise_score | 1.1513351565276442 | 1.8696835299069485 | 0.7064222657075494 | 0.7502548741286855 | 0.9770778247416331 |
| late_entropy_topk_mean | 1.132159492471322 | 1.7258093481228312 | 0.5995704093326117 | 0.6695692439269256 | 0.9190803497479266 |
| late_effective_concepts_topk_mean | 4.764716604711163 | 8.878403663928076 | 3.5853680055527937 | 5.613213749910937 | 0.8231455643620591 |
| late_top1_dominance_topk_mean | 0.6656883017697038 | 0.5251861647633088 | 0.1603330664470123 | 0.1683401378148614 | -0.8485459445115402 |
| late_top1_margin_mean | 2.1300182481751824 | 1.5081631397637796 | 1.377205729723195 | 0.9553121191790896 | -0.5545928103908107 |
| late_distinct_top1_count | 3.372262773722628 | 4.184251968503937 | 1.4590276506067257 | 1.4420470300976547 | 0.5607595055576728 |
| late_top1_churn_rate | 0.39103232533889465 | 0.5134983127109111 | 0.23876476852608047 | 0.23030698100674082 | 0.5249201182456548 |
| late_top5_jaccard_adjacent_mean | 0.5249788966681562 | 0.44201082007606185 | 0.1563655327215789 | 0.13356114417630868 | -0.5844248047953258 |


## Predictive AUC results

| label_regime | feature_set | features | roc_auc | roc_auc_per_fold_std | n_folds_with_both_classes | pr_auc | n_splits | n | n_wrong |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.5410080823684151 | 0.05140188559558839 | 5 | 0.9352875440692288 | 5 | 2000 | 1831 |
| strict | workspace_noise_single | ['workspace_noise_score'] | 0.7261818969166782 | 0.06443091763765824 | 5 | 0.9628907626645641 | 5 | 2000 | 1831 |
| strict | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7124796809710476 | 0.06422716121046924 | 5 | 0.9606906687966589 | 5 | 2000 | 1831 |
| strict | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7538480928389764 | 0.06700950432729151 | 5 | 0.9659774454820571 | 5 | 2000 | 1831 |
| strict | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7075320176189814 | 0.05922020576024254 | 5 | 0.9602363282748516 | 5 | 2000 | 1831 |
| strict | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7499280956828325 | 0.06481894230159052 | 5 | 0.9661148718775856 | 5 | 2000 | 1831 |
| strict | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7261818969166782 | 0.06443091763765824 | 5 | 0.9628907626645641 | 5 | 2000 | 1831 |
| strict | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7690885764237863 | 0.05744319736497048 | 5 | 0.9675299864335555 | 5 | 2000 | 1831 |
| strict | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.6854145728237229 | 0.06223929687317372 | 5 | 0.9566216256193267 | 5 | 2000 | 1831 |
| strict | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.6806414188256813 | 0.05837069977120982 | 5 | 0.9549799633746513 | 5 | 2000 | 1831 |
| strict | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7373698855024738 | 0.062272814855374656 | 5 | 0.9600460532816546 | 5 | 2000 | 1831 |
| strict | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7417617042454248 | 0.05723621030251929 | 5 | 0.9608817747443925 | 5 | 2000 | 1831 |
| strict | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5606856278620342 | 0.02443228820193187 | 5 | 0.9388473812003807 | 5 | 2000 | 1831 |
| strict | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7771547865653651 | 0.05198834490130932 | 5 | 0.970346352981512 | 5 | 2000 | 1831 |
| expanded_deterministic | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.6162117019533597 | 0.024187223398491848 | 5 | 0.7806450291293816 | 5 | 2000 | 1348 |
| expanded_deterministic | workspace_noise_single | ['workspace_noise_score'] | 0.7569689701625675 | 0.020940160183371748 | 5 | 0.8524439582940004 | 5 | 2000 | 1348 |
| expanded_deterministic | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7519240046603921 | 0.02061057664688941 | 5 | 0.8502981995310736 | 5 | 2000 | 1348 |
| expanded_deterministic | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7657584060002547 | 0.01889223003392468 | 5 | 0.8490962491523661 | 5 | 2000 | 1348 |
| expanded_deterministic | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7631904116072892 | 0.012888773667762827 | 5 | 0.8602934733485134 | 5 | 2000 | 1348 |
| expanded_deterministic | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7734453223134478 | 0.01619227414129733 | 5 | 0.858643553051438 | 5 | 2000 | 1348 |
| expanded_deterministic | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7569689701625675 | 0.020940160183371748 | 5 | 0.8524439582940004 | 5 | 2000 | 1348 |
| expanded_deterministic | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7703277748448052 | 0.017157903026152544 | 5 | 0.8544487376128314 | 5 | 2000 | 1348 |
| expanded_deterministic | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.7227112195299557 | 0.02360314659978491 | 5 | 0.8402274570055458 | 5 | 2000 | 1348 |
| expanded_deterministic | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7223823979173873 | 0.022589052275619952 | 5 | 0.8380924575344564 | 5 | 2000 | 1348 |
| expanded_deterministic | layer_l33_single | ['layer_l33_entropy_topk'] | 0.744877664706632 | 0.029002940057344034 | 5 | 0.8355265604456186 | 5 | 2000 | 1348 |
| expanded_deterministic | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7492945695508911 | 0.02734740036392766 | 5 | 0.8354756122556728 | 5 | 2000 | 1348 |
| expanded_deterministic | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5178052920937176 | 0.02541319644138478 | 5 | 0.6975243290770359 | 5 | 2000 | 1348 |
| expanded_deterministic | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7681204602137227 | 0.018986793741707378 | 5 | 0.8587496356211162 | 5 | 2000 | 1348 |
| primary_with_llm_judge | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.6303293292717973 | 0.016238210636711686 | 5 | 0.7720407765994259 | 5 | 1955 | 1270 |
| primary_with_llm_judge | workspace_noise_single | ['workspace_noise_score'] | 0.7549939651704121 | 0.025003372426997024 | 5 | 0.8406123523877909 | 5 | 1955 | 1270 |
| primary_with_llm_judge | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7475004310592563 | 0.03183140077470718 | 5 | 0.8352387969654065 | 5 | 1955 | 1270 |
| primary_with_llm_judge | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7655060635668716 | 0.03000787294525583 | 5 | 0.8433756951097625 | 5 | 1955 | 1270 |
| primary_with_llm_judge | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7616069889074086 | 0.02345341437315788 | 5 | 0.8497562205725833 | 5 | 1955 | 1270 |
| primary_with_llm_judge | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7754135295131904 | 0.02569074111422119 | 5 | 0.8534107773163563 | 5 | 1955 | 1270 |
| primary_with_llm_judge | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7549939651704121 | 0.025003372426997024 | 5 | 0.8406123523877909 | 5 | 1955 | 1270 |
| primary_with_llm_judge | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7727283177194092 | 0.026459306845752567 | 5 | 0.8456479267460382 | 5 | 1955 | 1270 |
| primary_with_llm_judge | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.7233818035519283 | 0.024292282250047564 | 5 | 0.8283714960645919 | 5 | 1955 | 1270 |
| primary_with_llm_judge | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7229875280188517 | 0.02541941810562884 | 5 | 0.8272016495154794 | 5 | 1955 | 1270 |
| primary_with_llm_judge | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7460083912868556 | 0.029629902476593962 | 5 | 0.819172345672903 | 5 | 1955 | 1270 |
| primary_with_llm_judge | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7483659980458646 | 0.03343626249251379 | 5 | 0.8181243504657412 | 5 | 1955 | 1270 |
| primary_with_llm_judge | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.535896315880223 | 0.03868077356813989 | 5 | 0.6863279746379565 | 5 | 1955 | 1270 |
| primary_with_llm_judge | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7748755675613541 | 0.023239292523169253 | 5 | 0.8481851547520952 | 5 | 1955 | 1270 |
| high_quality_primary | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.6314668057003824 | 0.03985644023657366 | 5 | 0.771566061753505 | 5 | 1945 | 1260 |
| high_quality_primary | workspace_noise_single | ['workspace_noise_score'] | 0.7548534352913915 | 0.024597819146184183 | 5 | 0.8392133728091026 | 5 | 1945 | 1260 |
| high_quality_primary | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7477754605491832 | 0.01958360218680917 | 5 | 0.8351304365834611 | 5 | 1945 | 1260 |
| high_quality_primary | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7645104854593906 | 0.029245442270439233 | 5 | 0.8439508032442057 | 5 | 1945 | 1260 |
| high_quality_primary | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7625628548256286 | 0.010043350816196794 | 5 | 0.8502512588346769 | 5 | 1945 | 1260 |
| high_quality_primary | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7750839995365543 | 0.020425030184847533 | 5 | 0.8545578182583161 | 5 | 1945 | 1260 |
| high_quality_primary | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7548534352913915 | 0.024597819146184183 | 5 | 0.8392133728091026 | 5 | 1945 | 1260 |
| high_quality_primary | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7721805121075194 | 0.026077337722543597 | 5 | 0.8465825584610672 | 5 | 1945 | 1260 |
| high_quality_primary | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.7237898273664698 | 0.013730596839323888 | 5 | 0.8283057703023156 | 5 | 1945 | 1260 |
| high_quality_primary | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.722167767350249 | 0.015168549552044117 | 5 | 0.8265851026592458 | 5 | 1945 | 1260 |
| high_quality_primary | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7453539566678252 | 0.031262082294319586 | 5 | 0.8214949860636731 | 5 | 1945 | 1260 |
| high_quality_primary | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7498667593558104 | 0.030337731028910613 | 5 | 0.8203072956930981 | 5 | 1945 | 1260 |
| high_quality_primary | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5401193372726218 | 0.011684687656776565 | 5 | 0.6909662592666669 | 5 | 1945 | 1260 |
| high_quality_primary | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7760108909743946 | 0.02748776251562996 | 5 | 0.8488296481807607 | 5 | 1945 | 1260 |


## Bootstrap AUC intervals

| label_regime | feature_set | roc_auc | roc_auc_ci_low | roc_auc_ci_high | pr_auc | pr_auc_ci_low | pr_auc_ci_high | bootstrap_n_effective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.6162117019533597 | 0.5902443486908563 | 0.6424637467821986 | 0.7806450291293816 | 0.756592193878571 | 0.8057275393823469 | 1000 |
| expanded_deterministic | combined_compact | 0.7631904116072892 | 0.7387287188612248 | 0.7851172603126121 | 0.8602934733485134 | 0.8394623578149583 | 0.8802122904168759 | 1000 |
| expanded_deterministic | combined_full | 0.7734453223134478 | 0.7510593947908507 | 0.7951380527948922 | 0.858643553051438 | 0.8367619252914146 | 0.87977732409835 | 1000 |
| expanded_deterministic | commitment_dynamics_full | 0.7223823979173873 | 0.700231055464188 | 0.7454448721012964 | 0.8380924575344564 | 0.8176880245212065 | 0.858689770014945 | 1000 |
| expanded_deterministic | commitment_dynamics_single | 0.7227112195299557 | 0.6998986138619947 | 0.7462781502923379 | 0.8402274570055458 | 0.8169614790786736 | 0.8602657195393515 | 1000 |
| expanded_deterministic | layer_l33_diff | 0.5178052920937176 | 0.49218475240097703 | 0.5425664959090225 | 0.6975243290770359 | 0.6712801829082327 | 0.725155515017351 | 1000 |
| expanded_deterministic | layer_l33_diff_in_full | 0.7681204602137227 | 0.7458104097756435 | 0.7896948350060606 | 0.8587496356211162 | 0.8382368682725331 | 0.8776036913950594 | 1000 |
| expanded_deterministic | layer_l33_full | 0.7492945695508911 | 0.7246684256700469 | 0.772465814152854 | 0.8354756122556728 | 0.809422115274839 | 0.8572987233024155 | 1000 |
| expanded_deterministic | layer_l33_single | 0.744877664706632 | 0.7210278810591502 | 0.7679617516271724 | 0.8355265604456186 | 0.8125026643999738 | 0.857812138849498 | 1000 |
| expanded_deterministic | workspace_compact | 0.7519240046603921 | 0.7278623592120352 | 0.7738069039569685 | 0.8502981995310736 | 0.8300523871621036 | 0.870454237657016 | 1000 |
| expanded_deterministic | workspace_full | 0.7657584060002547 | 0.7445312611591773 | 0.78751743385196 | 0.8490962491523661 | 0.8302047953057062 | 0.8714136587243527 | 1000 |
| expanded_deterministic | workspace_late_late_full | 0.7703277748448052 | 0.7468928562804082 | 0.7909040889820369 | 0.8544487376128314 | 0.8322440041105158 | 0.8761760133700957 | 1000 |
| expanded_deterministic | workspace_late_late_single | 0.7569689701625675 | 0.7358956410721856 | 0.7799140895036338 | 0.8524439582940004 | 0.831716105379082 | 0.8722709399553689 | 1000 |
| expanded_deterministic | workspace_noise_single | 0.7569689701625675 | 0.7357028800845631 | 0.778838252927598 | 0.8524439582940004 | 0.8320283160620544 | 0.8737808815927569 | 1000 |
| high_quality_primary | baseline_output_confidence | 0.6314668057003824 | 0.6055391534343497 | 0.6557723491885473 | 0.771566061753505 | 0.7466090354914321 | 0.7957148972326265 | 1000 |
| high_quality_primary | combined_compact | 0.7625628548256286 | 0.7415151101819473 | 0.783904619929913 | 0.8502512588346769 | 0.8308570305050452 | 0.8702891044023665 | 1000 |
| high_quality_primary | combined_full | 0.7750839995365543 | 0.7529998785257287 | 0.797550393886578 | 0.8545578182583161 | 0.8340169325086506 | 0.8750629535223038 | 1000 |
| high_quality_primary | commitment_dynamics_full | 0.722167767350249 | 0.6996921927865224 | 0.7440446334861877 | 0.8265851026592458 | 0.8047537206227524 | 0.8468008893278655 | 1000 |
| high_quality_primary | commitment_dynamics_single | 0.7237898273664698 | 0.6995271226045005 | 0.746111308768323 | 0.8283057703023156 | 0.8061365391987528 | 0.8504627643768652 | 1000 |
| high_quality_primary | layer_l33_diff | 0.5401193372726218 | 0.5145890318198141 | 0.5653109728432774 | 0.6909662592666669 | 0.6623784847725388 | 0.7192224971437536 | 1000 |
| high_quality_primary | layer_l33_diff_in_full | 0.7760108909743946 | 0.754842908441629 | 0.7957974366370958 | 0.8488296481807607 | 0.8250696032830463 | 0.8690755071329159 | 1000 |
| high_quality_primary | layer_l33_full | 0.7498667593558104 | 0.726649154915325 | 0.7722724440039148 | 0.8203072956930981 | 0.7954678307027881 | 0.8443811705098231 | 1000 |
| high_quality_primary | layer_l33_single | 0.7453539566678252 | 0.7234519057443786 | 0.767534207936381 | 0.8214949860636731 | 0.7973893100298398 | 0.8451404761105168 | 1000 |
| high_quality_primary | workspace_compact | 0.7477754605491832 | 0.7268803812412465 | 0.7692603819136214 | 0.8351304365834611 | 0.8141595277797473 | 0.8562954985180973 | 1000 |
| high_quality_primary | workspace_full | 0.7645104854593906 | 0.7434021037483135 | 0.7851646722200699 | 0.8439508032442057 | 0.8226173122618244 | 0.8637331071969653 | 1000 |
| high_quality_primary | workspace_late_late_full | 0.7721805121075194 | 0.7494930329759365 | 0.7927283483526045 | 0.8465825584610672 | 0.8247344960366896 | 0.8679658297993684 | 1000 |
| high_quality_primary | workspace_late_late_single | 0.7548534352913915 | 0.73194811237928 | 0.7768753945589839 | 0.8392133728091026 | 0.8171318536432538 | 0.8601810334971893 | 1000 |
| high_quality_primary | workspace_noise_single | 0.7548534352913915 | 0.7317281674321859 | 0.7768878757270905 | 0.8392133728091026 | 0.8156482324006724 | 0.8604646576008558 | 1000 |
| primary_with_llm_judge | baseline_output_confidence | 0.6303293292717973 | 0.6048459404911863 | 0.6552562849331843 | 0.7720407765994259 | 0.7491736875842709 | 0.7952570156010147 | 1000 |
| primary_with_llm_judge | combined_compact | 0.7616069889074086 | 0.7394376891134372 | 0.7820767172251455 | 0.8497562205725833 | 0.8276235480167009 | 0.8684108760283281 | 1000 |
| primary_with_llm_judge | combined_full | 0.7754135295131904 | 0.7548420994463085 | 0.7967650780590342 | 0.8534107773163563 | 0.8327102080068621 | 0.8734168276872014 | 1000 |
| primary_with_llm_judge | commitment_dynamics_full | 0.7229875280188517 | 0.7005892915104428 | 0.746675860617918 | 0.8272016495154794 | 0.8054336725640516 | 0.8492777706608604 | 1000 |
| primary_with_llm_judge | commitment_dynamics_single | 0.7233818035519283 | 0.7014824377277974 | 0.7453102272242094 | 0.8283714960645919 | 0.8056536022815319 | 0.8497055834755449 | 1000 |
| primary_with_llm_judge | layer_l33_diff | 0.535896315880223 | 0.5096698605343197 | 0.5615516928704204 | 0.6863279746379565 | 0.6564355550702387 | 0.7143264098445684 | 1000 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.7748755675613541 | 0.7529886430760234 | 0.7951895044891211 | 0.8481851547520952 | 0.8275309672025241 | 0.8693514803671417 | 1000 |
| primary_with_llm_judge | layer_l33_full | 0.7483659980458646 | 0.7247705118399511 | 0.7710972394606254 | 0.8181243504657412 | 0.7911561854592933 | 0.8441986296511893 | 1000 |
| primary_with_llm_judge | layer_l33_single | 0.7460083912868556 | 0.7236450169814207 | 0.7687033818445465 | 0.819172345672903 | 0.7928301522318049 | 0.8418396456057708 | 1000 |
| primary_with_llm_judge | workspace_compact | 0.7475004310592563 | 0.7256594839373779 | 0.7693769435936278 | 0.8352387969654065 | 0.8135282347659435 | 0.8569238922372231 | 1000 |
| primary_with_llm_judge | workspace_full | 0.7655060635668716 | 0.7446540085822319 | 0.7876347800176416 | 0.8433756951097625 | 0.8217485810939509 | 0.8651884755539857 | 1000 |
| primary_with_llm_judge | workspace_late_late_full | 0.7727283177194092 | 0.7521609533444144 | 0.794502675265537 | 0.8456479267460382 | 0.8236915310309405 | 0.8684903053673313 | 1000 |
| primary_with_llm_judge | workspace_late_late_single | 0.7549939651704121 | 0.7335026035112425 | 0.776629300294043 | 0.8406123523877909 | 0.8175255341749167 | 0.8605819192973738 | 1000 |
| primary_with_llm_judge | workspace_noise_single | 0.7549939651704121 | 0.7340343347422543 | 0.7766328713982993 | 0.8406123523877909 | 0.8192988864900944 | 0.860663261059437 | 1000 |
| strict | baseline_output_confidence | 0.5410080823684151 | 0.5009332965506416 | 0.5827109707389413 | 0.9352875440692288 | 0.9219326090809533 | 0.9472026638848915 | 1000 |
| strict | combined_compact | 0.7075320176189814 | 0.6699040469285592 | 0.7449376910234737 | 0.9602363282748516 | 0.9505424488662404 | 0.9690724439634332 | 1000 |
| strict | combined_full | 0.7499280956828325 | 0.710855498830184 | 0.7854846722340434 | 0.9661148718775856 | 0.9571121309038839 | 0.974216343375 | 1000 |
| strict | commitment_dynamics_full | 0.6806414188256813 | 0.6375946241864533 | 0.7245804621230266 | 0.9549799633746513 | 0.9440018097827991 | 0.9652759534262093 | 1000 |
| strict | commitment_dynamics_single | 0.6854145728237229 | 0.6453524547263984 | 0.7256675699610569 | 0.9566216256193267 | 0.9461596161116022 | 0.9661266703108509 | 1000 |
| strict | layer_l33_diff | 0.5606856278620342 | 0.520466086431729 | 0.6012286912424983 | 0.9388473812003807 | 0.9267171697660669 | 0.9510814871634347 | 1000 |
| strict | layer_l33_diff_in_full | 0.7771547865653651 | 0.7430498280155768 | 0.81006525429195 | 0.970346352981512 | 0.9617952453144542 | 0.9786203242606192 | 1000 |
| strict | layer_l33_full | 0.7417617042454248 | 0.7036557577564756 | 0.7817295969356941 | 0.9608817747443925 | 0.9502112177039049 | 0.9726413331516689 | 1000 |
| strict | layer_l33_single | 0.7373698855024738 | 0.6979976007546383 | 0.775472808654954 | 0.9600460532816546 | 0.9484264793976237 | 0.9715862623762819 | 1000 |
| strict | workspace_compact | 0.7124796809710476 | 0.6751268885880224 | 0.7499645256359101 | 0.9606906687966589 | 0.9511272623309498 | 0.9700638494845539 | 1000 |
| strict | workspace_full | 0.7538480928389764 | 0.7164155503826029 | 0.7880013161289594 | 0.9659774454820571 | 0.9564486543428876 | 0.9749125037804225 | 1000 |
| strict | workspace_late_late_full | 0.7690885764237863 | 0.732137317059324 | 0.8055667013305705 | 0.9675299864335555 | 0.9575585246950836 | 0.9764073093340581 | 1000 |
| strict | workspace_late_late_single | 0.7261818969166782 | 0.6871052068579041 | 0.7630359746411569 | 0.9628907626645641 | 0.9527273564909007 | 0.9721414434344835 | 1000 |
| strict | workspace_noise_single | 0.7261818969166782 | 0.6887748605860415 | 0.7623984551026695 | 0.9628907626645641 | 0.9537188524245359 | 0.9719287429704662 | 1000 |


## Permutation sanity checks

| label_regime | feature_set | real_roc_auc | perm_auc_mean | perm_auc_ci_low | perm_auc_ci_high | p_perm_ge_real | permutation_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.6162117019533597 | 0.4998698184995722 | 0.47550119695618137 | 0.5250628914001202 | 0.0 | 500 |
| expanded_deterministic | combined_compact | 0.7631904116072892 | 0.49997215370191694 | 0.47400633863392255 | 0.528291174382407 | 0.0 | 500 |
| expanded_deterministic | combined_full | 0.7734453223134478 | 0.49935266516174837 | 0.4741094225027762 | 0.5276931514081302 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_full | 0.7223823979173873 | 0.499821587537092 | 0.4730634511933152 | 0.5267742713586135 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_single | 0.7227112195299557 | 0.49998212530265246 | 0.4735915284629808 | 0.525104306994229 | 0.0 | 500 |
| expanded_deterministic | layer_l33_diff | 0.5178052920937176 | 0.5001149077934136 | 0.4721613535617411 | 0.5261624242231162 | 0.106 | 500 |
| expanded_deterministic | layer_l33_diff_in_full | 0.7681204602137227 | 0.4999013057290055 | 0.47581229747319365 | 0.5271673212757824 | 0.0 | 500 |
| expanded_deterministic | layer_l33_full | 0.7492945695508911 | 0.49946100790082104 | 0.4725721814640185 | 0.5263875930713077 | 0.0 | 500 |
| expanded_deterministic | layer_l33_single | 0.744877664706632 | 0.5004389893684804 | 0.47293197943784016 | 0.5260126340317852 | 0.0 | 500 |
| expanded_deterministic | workspace_compact | 0.7519240046603921 | 0.5009373600517013 | 0.47307081839034426 | 0.5292944500828312 | 0.0 | 500 |
| expanded_deterministic | workspace_full | 0.7657584060002547 | 0.5005856688390891 | 0.4728796410496805 | 0.5283670366004625 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_full | 0.7703277748448052 | 0.5011682019260527 | 0.4724621570697784 | 0.5278235422621106 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_single | 0.7569689701625675 | 0.4997245157561304 | 0.47145543955143726 | 0.5252286675556608 | 0.0 | 500 |
| expanded_deterministic | workspace_noise_single | 0.7569689701625675 | 0.500144410715261 | 0.47292176776319383 | 0.5288926960641532 | 0.0 | 500 |
| high_quality_primary | baseline_output_confidence | 0.6314668057003824 | 0.500152529255011 | 0.4714833014714402 | 0.5313700758892365 | 0.0 | 500 |
| high_quality_primary | combined_compact | 0.7625628548256286 | 0.5003456447688565 | 0.471219528443981 | 0.5272975900822616 | 0.0 | 500 |
| high_quality_primary | combined_full | 0.7750839995365543 | 0.500753523346078 | 0.47501610473873246 | 0.5271264337851929 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_full | 0.722167767350249 | 0.5005879898041942 | 0.4727165450121654 | 0.5274801876955161 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_single | 0.7237898273664698 | 0.49991043911481864 | 0.47107409338431233 | 0.5260810450700961 | 0.0 | 500 |
| high_quality_primary | layer_l33_diff | 0.5401193372726218 | 0.5009825489514541 | 0.4720817112733171 | 0.5286050573514077 | 0.006 | 500 |
| high_quality_primary | layer_l33_diff_in_full | 0.7760108909743946 | 0.5010693731896652 | 0.4739442706522998 | 0.5276313289305989 | 0.0 | 500 |
| high_quality_primary | layer_l33_full | 0.7498667593558104 | 0.5001776086200904 | 0.473514801297648 | 0.5288350712547794 | 0.0 | 500 |
| high_quality_primary | layer_l33_single | 0.7453539566678252 | 0.49804577685088636 | 0.47213845440852736 | 0.5218924226624956 | 0.0 | 500 |
| high_quality_primary | workspace_compact | 0.7477754605491832 | 0.4987387579654733 | 0.47042133008921333 | 0.5264136253041363 | 0.0 | 500 |
| high_quality_primary | workspace_full | 0.7645104854593906 | 0.49922146448847177 | 0.4754670953539567 | 0.5249053991426255 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_full | 0.7721805121075194 | 0.49957054802456263 | 0.4695294867338663 | 0.5268841965009848 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_single | 0.7548534352913915 | 0.5002449264279921 | 0.472725553238327 | 0.5262282759819256 | 0.0 | 500 |
| high_quality_primary | workspace_noise_single | 0.7548534352913915 | 0.5004750318618931 | 0.4735897346773259 | 0.5292320414783918 | 0.0 | 500 |
| primary_with_llm_judge | baseline_output_confidence | 0.6303293292717973 | 0.49945371228231505 | 0.4734760043680671 | 0.5255845881947239 | 0.0 | 500 |
| primary_with_llm_judge | combined_compact | 0.7616069889074086 | 0.5007372446692339 | 0.47490031036266456 | 0.5275119834473245 | 0.0 | 500 |
| primary_with_llm_judge | combined_full | 0.7754135295131904 | 0.500521011552388 | 0.4720425886545204 | 0.5248907983217427 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_full | 0.7229875280188517 | 0.5005976550376459 | 0.47449726995804364 | 0.5250979079257428 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_single | 0.7233818035519283 | 0.49978656014713485 | 0.47545962411632847 | 0.5244103684119777 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_diff | 0.535896315880223 | 0.49949096154951433 | 0.473715587102707 | 0.5258832691533996 | 0.004 | 500 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.7748755675613541 | 0.5002657669981033 | 0.4724639921834588 | 0.5262852750158055 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_full | 0.7483659980458646 | 0.5003549169492499 | 0.4736888039542502 | 0.5261081958733261 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_single | 0.7460083912868556 | 0.49980892924880743 | 0.47230076441174784 | 0.525526639462038 | 0.0 | 500 |
| primary_with_llm_judge | workspace_compact | 0.7475004310592563 | 0.49965369733892756 | 0.473455974481292 | 0.5261778550491407 | 0.0 | 500 |
| primary_with_llm_judge | workspace_full | 0.7655060635668716 | 0.4993845071555837 | 0.469515862980631 | 0.5249464049658027 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_full | 0.7727283177194092 | 0.49973997586068164 | 0.4768883843899075 | 0.5275190528191276 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_single | 0.7549939651704121 | 0.5001998091844359 | 0.4761702396689465 | 0.5267015058336686 | 0.0 | 500 |
| primary_with_llm_judge | workspace_noise_single | 0.7549939651704121 | 0.5000768526926835 | 0.4710181044887637 | 0.5233078050462671 | 0.0 | 500 |
| strict | baseline_output_confidence | 0.5410080823684151 | 0.5005227330750164 | 0.4562395173200534 | 0.5486902103484047 | 0.052 | 500 |
| strict | combined_compact | 0.7075320176189814 | 0.5015036630806071 | 0.46065662376106437 | 0.5446194565003118 | 0.0 | 500 |
| strict | combined_full | 0.7499280956828325 | 0.5014323727778335 | 0.45687914257737383 | 0.5457028687398808 | 0.0 | 500 |
| strict | commitment_dynamics_full | 0.6806414188256813 | 0.4993802849673118 | 0.4552737373117157 | 0.5435344284333907 | 0.0 | 500 |
| strict | commitment_dynamics_single | 0.6854145728237229 | 0.4996040447390277 | 0.45789000416883463 | 0.5411440542400926 | 0.0 | 500 |
| strict | layer_l33_diff | 0.5606856278620342 | 0.5006603240057007 | 0.45581285810773686 | 0.5447669007461892 | 0.004 | 500 |
| strict | layer_l33_diff_in_full | 0.7771547865653651 | 0.5002765003764877 | 0.45366550434819136 | 0.543800797572381 | 0.0 | 500 |
| strict | layer_l33_full | 0.7417617042454248 | 0.5010547991688183 | 0.45531065896671075 | 0.5479698745148478 | 0.0 | 500 |
| strict | layer_l33_single | 0.7373698855024738 | 0.5003340884633158 | 0.45606161472858947 | 0.5406275550270004 | 0.0 | 500 |
| strict | workspace_compact | 0.7124796809710476 | 0.5005047262950049 | 0.4537269057875704 | 0.5504159947517927 | 0.0 | 500 |
| strict | workspace_full | 0.7538480928389764 | 0.4988136660214129 | 0.45382280514091633 | 0.5435871851964361 | 0.0 | 500 |
| strict | workspace_late_late_full | 0.7690885764237863 | 0.5004976748244404 | 0.4529269904569237 | 0.5491344820788588 | 0.0 | 500 |
| strict | workspace_late_late_single | 0.7261818969166782 | 0.4996974524865967 | 0.4566485640142322 | 0.5435853269949812 | 0.0 | 500 |
| strict | workspace_noise_single | 0.7261818969166782 | 0.4989090709315891 | 0.4529484001693387 | 0.5435605240451269 | 0.0 | 500 |


## H.3 quadrant analysis

| quadrant | n | accuracy | wrong_rate | mean_confidence | mean_workspace_noise |
| --- | --- | --- | --- | --- | --- |
| high_confidence__clean_workspace | 502 | 0.5577689243027888 | 0.44223107569721115 | 0.8408647508497732 | 0.9410765123905167 |
| high_confidence__noisy_workspace | 474 | 0.21940928270042195 | 0.7805907172995781 | 0.8032167181687013 | 2.2730896264195146 |
| low_confidence__clean_workspace | 475 | 0.4863157894736842 | 0.5136842105263157 | 0.45303753562240157 | 0.939108794535817 |
| low_confidence__noisy_workspace | 504 | 0.1388888888888889 | 0.8611111111111112 | 0.44470814559089233 | 2.3159148723330527 |


## Conclusion

**supports_H_A_ci_distinguishable** — Combined workspace + confidence features improved AUC over output confidence with non-overlapping 95% bootstrap CIs under the primary label regime, supporting complementary J-space signal. The single-feature `workspace_noise_score` AUC is 0.755 with CI [0.734, 0.777], entirely above the baseline CI's upper bound (0.655) — a cleaner statistical claim than the combined_compact delta.

## Artefact guide

See `AGENT_BRIEF.md` for the most useful machine-readable files and selected examples.
