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
  "DATASET_ID": "gsm8k",
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
  "THRESHOLD_MODE": "frozen_absolute",
  "PROTOCOL_FILE": "/content/drive/MyDrive/J-Space_Artifacts/workspace_backup/protocols/H3_overconfident_workspace_stratification_v1.DRAFT.json",
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

- Dataset ID: `gsm8k`
- Repo: `openai/gsm8k`
- Config: `main`
- Split: `test`
- Task family: `numeric_reasoning_short`
- Prompt template: `numeric_v1`

```json
{
  "dataset_id": "gsm8k",
  "repo": "openai/gsm8k",
  "config": "main",
  "split": "test",
  "task_family": "numeric_reasoning_short",
  "answer_format": "numeric",
  "prompt_template_id": "numeric_v1",
  "max_new_tokens": 200,
  "n_total_in_split": 1319,
  "n_requested": 2000,
  "random_seed": 42,
  "expected_failure_mode": "multi_step_arithmetic_failure",
  "supports_short_answer": true,
  "supports_multiple_choice": false,
  "n_kept_after_dedup": 1319,
  "n_selected": 1319,
  "examples_with_aliases": 1319,
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


## Descriptive statistics

| feature | mean_correct | mean_wrong | std_correct | std_wrong | cohen_d_wrong_minus_correct |
| --- | --- | --- | --- | --- | --- |
| first_content_token_prob | 0.8670089873713214 | 0.6305233567862156 | 0.19579155205992393 | 0.23544478946009875 | -1.0411932369891705 |
| sequence_content_logprob_mean | -0.12542588392227025 | -0.14779414729674736 | 0.055348686867539354 | 0.04939747553101985 | -0.4403464951603725 |
| workspace_noise_score | 1.6363334937208456 | 2.0829339183792945 | 0.5005982921184204 | 0.4827685237122407 | 0.9173527441021525 |
| late_entropy_topk_mean | 2.1117598088127503 | 2.40894852364011 | 0.43835880481975414 | 0.42821129328239105 | 0.6903102076864599 |
| late_effective_concepts_topk_mean | 14.853244486506886 | 16.576624500544316 | 5.237675882031899 | 5.452981941293741 | 0.31883161012127104 |
| late_top1_dominance_topk_mean | 0.4620061888297616 | 0.3676064174981373 | 0.11907104696664635 | 0.12069254704320068 | -0.7845092548497075 |
| late_top1_margin_mean | 1.8285893793706294 | 1.0511190233977619 | 0.9789959800332922 | 0.6494691910864253 | -1.0555444239769205 |
| late_distinct_top1_count | 4.674825174825175 | 4.747711088504578 | 1.1769105277724188 | 1.2414400800897678 | 0.05939104650115368 |
| late_top1_churn_rate | 0.5509490509490509 | 0.5731725039965122 | 0.17692167807665812 | 0.19210991730353313 | 0.11770896646118024 |
| late_top5_jaccard_adjacent_mean | 0.33404294118579836 | 0.37965423538014725 | 0.0993763958114522 | 0.09993288885161496 | 0.4569904489042818 |


## Predictive AUC results

| label_regime | feature_set | features | roc_auc | roc_auc_per_fold_std | n_folds_with_both_classes | pr_auc | n_splits | n | n_wrong |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8084590477043138 | 0.041670455323531454 | 5 | 0.9382817091271821 | 5 | 1319 | 1068 |
| strict | workspace_noise_single | ['workspace_noise_score'] | 0.7406292433263201 | 0.014537121917369205 | 5 | 0.922047950153027 | 5 | 1319 | 1068 |
| strict | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7350448393691154 | 0.03348909078303373 | 5 | 0.9195662111373315 | 5 | 1319 | 1068 |
| strict | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7897138039601892 | 0.03271987658089362 | 5 | 0.9354667739904248 | 5 | 1319 | 1068 |
| strict | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8125848665264037 | 0.04185880046339763 | 5 | 0.9415679179418344 | 5 | 1319 | 1068 |
| strict | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8229031439783936 | 0.03972734403122713 | 5 | 0.9432664807335702 | 5 | 1319 | 1068 |
| strict | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7406292433263201 | 0.014537121917369205 | 5 | 0.922047950153027 | 5 | 1319 | 1068 |
| strict | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7824395302684393 | 0.031011202654300456 | 5 | 0.9334548947806638 | 5 | 1319 | 1068 |
| strict | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.7180491517077756 | 0.024089090492229383 | 5 | 0.912903698977259 | 5 | 1319 | 1068 |
| strict | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7249242729456704 | 0.028316508472923208 | 5 | 0.9169409779913913 | 5 | 1319 | 1068 |
| strict | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7587216676365698 | 0.03381494703823512 | 5 | 0.9183717847567716 | 5 | 1319 | 1068 |
| strict | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7659250637897848 | 0.034330397995587264 | 5 | 0.9248988861271253 | 5 | 1319 | 1068 |
| strict | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.6399980601936822 | 0.03189021685075826 | 5 | 0.8561631934231921 | 5 | 1319 | 1068 |
| strict | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7827528835966995 | 0.035078934750688684 | 5 | 0.9336493104008502 | 5 | 1319 | 1068 |
| expanded_deterministic | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8040431266846362 | 0.02077199266384074 | 5 | 0.9339210194896643 | 5 | 1319 | 1060 |
| expanded_deterministic | workspace_noise_single | ['workspace_noise_score'] | 0.7375209441247177 | 0.039172028537276485 | 5 | 0.9180244272302205 | 5 | 1319 | 1060 |
| expanded_deterministic | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7359109783638087 | 0.03265031491162527 | 5 | 0.9168187877236672 | 5 | 1319 | 1060 |
| expanded_deterministic | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7824943541924675 | 0.02214021411074927 | 5 | 0.9307521847935321 | 5 | 1319 | 1060 |
| expanded_deterministic | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8092518394405186 | 0.02244182086866622 | 5 | 0.9372612723889533 | 5 | 1319 | 1060 |
| expanded_deterministic | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8167735120565309 | 0.017555644158137172 | 5 | 0.9370404326434677 | 5 | 1319 | 1060 |
| expanded_deterministic | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7375209441247177 | 0.039172028537276485 | 5 | 0.9180244272302205 | 5 | 1319 | 1060 |
| expanded_deterministic | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.777427697239018 | 0.03373571407362009 | 5 | 0.9301058119193995 | 5 | 1319 | 1060 |
| expanded_deterministic | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.7165841043199535 | 0.04194746846318113 | 5 | 0.9079442830814689 | 5 | 1319 | 1060 |
| expanded_deterministic | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.724768704013987 | 0.04096169750429165 | 5 | 0.9148764680331146 | 5 | 1319 | 1060 |
| expanded_deterministic | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7492423690536897 | 0.04187430555540854 | 5 | 0.9102658625867892 | 5 | 1319 | 1060 |
| expanded_deterministic | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7538427915786405 | 0.03765899185953673 | 5 | 0.9161031230705069 | 5 | 1319 | 1060 |
| expanded_deterministic | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.6236067603992133 | 0.053903768256981094 | 5 | 0.840715652344838 | 5 | 1319 | 1060 |
| expanded_deterministic | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7770088147446638 | 0.032633254482105155 | 5 | 0.9301330459440798 | 5 | 1319 | 1060 |
| primary_with_llm_judge | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8054905420113966 | 0.01919593949765772 | 5 | 0.9233209435787814 | 5 | 1269 | 983 |
| primary_with_llm_judge | workspace_noise_single | ['workspace_noise_score'] | 0.743570773072299 | 0.03170190589425757 | 5 | 0.9064506837554087 | 5 | 1269 | 983 |
| primary_with_llm_judge | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7355355732771807 | 0.02886131776105233 | 5 | 0.9012505508210116 | 5 | 1269 | 983 |
| primary_with_llm_judge | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7839459624810592 | 0.02905580830696801 | 5 | 0.9190076429770186 | 5 | 1269 | 983 |
| primary_with_llm_judge | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8112279378810405 | 0.01814932302551885 | 5 | 0.9268696382549543 | 5 | 1269 | 983 |
| primary_with_llm_judge | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8142655919868534 | 0.022040179183207543 | 5 | 0.9262522914144177 | 5 | 1269 | 983 |
| primary_with_llm_judge | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.743570773072299 | 0.03170190589425757 | 5 | 0.9064506837554087 | 5 | 1269 | 983 |
| primary_with_llm_judge | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.77677866385903 | 0.027687178237774702 | 5 | 0.9180665979262637 | 5 | 1269 | 983 |
| primary_with_llm_judge | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.721588685983396 | 0.02441297544891061 | 5 | 0.8984228038334648 | 5 | 1269 | 983 |
| primary_with_llm_judge | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7278240579359604 | 0.02512118181435954 | 5 | 0.9002659766049479 | 5 | 1269 | 983 |
| primary_with_llm_judge | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7407998918680506 | 0.04434515258456344 | 5 | 0.8894663419524278 | 5 | 1269 | 983 |
| primary_with_llm_judge | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7516450995596469 | 0.04077546292977809 | 5 | 0.9019184370106258 | 5 | 1269 | 983 |
| primary_with_llm_judge | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.606271653067177 | 0.02679346911440096 | 5 | 0.8029649556836396 | 5 | 1269 | 983 |
| primary_with_llm_judge | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7800048374819483 | 0.031296332670623685 | 5 | 0.9200510918856828 | 5 | 1269 | 983 |
| high_quality_primary | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8057090567273866 | 0.01943086729151882 | 5 | 0.9231389385273957 | 5 | 1268 | 982 |
| high_quality_primary | workspace_noise_single | ['workspace_noise_score'] | 0.7437689601640722 | 0.027434795052420045 | 5 | 0.9065714183110979 | 5 | 1268 | 982 |
| high_quality_primary | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7351950493498356 | 0.020013672076757062 | 5 | 0.9012957912534488 | 5 | 1268 | 982 |
| high_quality_primary | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7838968567074474 | 0.03003420058900858 | 5 | 0.9186286880701303 | 5 | 1268 | 982 |
| high_quality_primary | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8099283608448578 | 0.017982707080053006 | 5 | 0.9263065794022532 | 5 | 1268 | 982 |
| high_quality_primary | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8131578197769643 | 0.027929433837320963 | 5 | 0.9254019942698055 | 5 | 1268 | 982 |
| high_quality_primary | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7437689601640722 | 0.027434795052420045 | 5 | 0.9065714183110979 | 5 | 1268 | 982 |
| high_quality_primary | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.777452181220002 | 0.02772759144009341 | 5 | 0.9181790536890693 | 5 | 1268 | 982 |
| high_quality_primary | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.7216469884494324 | 0.01664735460390329 | 5 | 0.8983287586622887 | 5 | 1268 | 982 |
| high_quality_primary | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7272264395482319 | 0.01606657063313174 | 5 | 0.9000624535724465 | 5 | 1268 | 982 |
| high_quality_primary | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7396992010026633 | 0.04463569602313639 | 5 | 0.8891825145141382 | 5 | 1268 | 982 |
| high_quality_primary | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7510788600401634 | 0.04340069482675015 | 5 | 0.9014187601258385 | 5 | 1268 | 982 |
| high_quality_primary | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.6043467733895433 | 0.02677196924642376 | 5 | 0.8014994725447003 | 5 | 1268 | 982 |
| high_quality_primary | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7794461139674989 | 0.030600743089616876 | 5 | 0.9197719742804406 | 5 | 1268 | 982 |


## Bootstrap AUC intervals

| label_regime | feature_set | roc_auc | roc_auc_ci_low | roc_auc_ci_high | pr_auc | pr_auc_ci_low | pr_auc_ci_high | bootstrap_n_effective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.8040431266846362 | 0.7706370865322554 | 0.8357718818591082 | 0.9339210194896643 | 0.917247690804027 | 0.9487667623884996 | 1000 |
| expanded_deterministic | combined_compact | 0.8092518394405186 | 0.779965063903079 | 0.8372901906202753 | 0.9372612723889533 | 0.9228503919510954 | 0.9508043897424856 | 1000 |
| expanded_deterministic | combined_full | 0.8167735120565309 | 0.7856563172844935 | 0.8452573079516494 | 0.9370404326434677 | 0.9201439137356862 | 0.9526496717344225 | 1000 |
| expanded_deterministic | commitment_dynamics_full | 0.724768704013987 | 0.6921935864226284 | 0.7557745426863518 | 0.9148764680331146 | 0.8982932715750285 | 0.9303745748784061 | 1000 |
| expanded_deterministic | commitment_dynamics_single | 0.7165841043199535 | 0.6843358039674202 | 0.749713686049014 | 0.9079442830814689 | 0.8886517025163625 | 0.925428815925946 | 1000 |
| expanded_deterministic | layer_l33_diff | 0.6236067603992133 | 0.5822136714298193 | 0.6654490321879533 | 0.840715652344838 | 0.81330136340335 | 0.8689231509080906 | 1000 |
| expanded_deterministic | layer_l33_diff_in_full | 0.7770088147446638 | 0.7459928773467226 | 0.8067456166379665 | 0.9301330459440798 | 0.9155451430398263 | 0.9436376498044966 | 1000 |
| expanded_deterministic | layer_l33_full | 0.7538427915786405 | 0.7201452431788227 | 0.7862985267083205 | 0.9161031230705069 | 0.8972887408670212 | 0.9327001096270456 | 1000 |
| expanded_deterministic | layer_l33_single | 0.7492423690536897 | 0.7142540470729493 | 0.7821849469228674 | 0.9102658625867892 | 0.8897420343065126 | 0.9298256699075188 | 1000 |
| expanded_deterministic | workspace_compact | 0.7359109783638087 | 0.706795837730964 | 0.7676715297428082 | 0.9168187877236672 | 0.9008736684439848 | 0.9326352861256468 | 1000 |
| expanded_deterministic | workspace_full | 0.7824943541924675 | 0.7519753135360083 | 0.813965523309738 | 0.9307521847935321 | 0.9153471969026998 | 0.9451957226498792 | 1000 |
| expanded_deterministic | workspace_late_late_full | 0.777427697239018 | 0.7438760817672053 | 0.8082308293474734 | 0.9301058119193995 | 0.9160476898176683 | 0.9437670039174088 | 1000 |
| expanded_deterministic | workspace_late_late_single | 0.7375209441247177 | 0.7059648500487965 | 0.7687501191822 | 0.9180244272302205 | 0.9016927366545039 | 0.9331115795912192 | 1000 |
| expanded_deterministic | workspace_noise_single | 0.7375209441247177 | 0.7037237584493443 | 0.7674649639956298 | 0.9180244272302205 | 0.9013096675456677 | 0.9336043978556909 | 1000 |
| high_quality_primary | baseline_output_confidence | 0.8057090567273866 | 0.7753014011321411 | 0.8369438744830924 | 0.9231389385273957 | 0.9028438156229376 | 0.9414472327944948 | 1000 |
| high_quality_primary | combined_compact | 0.8099283608448578 | 0.7806194091399137 | 0.8379342120869592 | 0.9263065794022532 | 0.9092420898755658 | 0.9426788186304325 | 1000 |
| high_quality_primary | combined_full | 0.8131578197769643 | 0.7808754770227616 | 0.8422728888821365 | 0.9254019942698055 | 0.905156972680074 | 0.9422906645383348 | 1000 |
| high_quality_primary | commitment_dynamics_full | 0.7272264395482319 | 0.6964053946070351 | 0.7579785364196883 | 0.9000624535724465 | 0.881286838682123 | 0.9191851066674885 | 1000 |
| high_quality_primary | commitment_dynamics_single | 0.7216469884494324 | 0.6906605931919181 | 0.7521695477632714 | 0.8983287586622887 | 0.8781539963013141 | 0.9168335345055107 | 1000 |
| high_quality_primary | layer_l33_diff | 0.6043467733895433 | 0.5620754296629048 | 0.6406447256242916 | 0.8014994725447003 | 0.7714847414607195 | 0.8341545255651405 | 1000 |
| high_quality_primary | layer_l33_diff_in_full | 0.7794461139674989 | 0.7479254154109843 | 0.8098656286549101 | 0.9197719742804406 | 0.9030158508767517 | 0.9351717621088389 | 1000 |
| high_quality_primary | layer_l33_full | 0.7510788600401634 | 0.7175795819186014 | 0.7813489068838267 | 0.9014187601258385 | 0.8786918431229858 | 0.9199033622913377 | 1000 |
| high_quality_primary | layer_l33_single | 0.7396992010026633 | 0.7041808467639217 | 0.7717483638124373 | 0.8891825145141382 | 0.8658311542195352 | 0.910357808572835 | 1000 |
| high_quality_primary | workspace_compact | 0.7351950493498356 | 0.7041474420180667 | 0.7666378626968314 | 0.9012957912534488 | 0.8813348021017395 | 0.9199967553071987 | 1000 |
| high_quality_primary | workspace_full | 0.7838968567074474 | 0.7534853474442925 | 0.8129952964741102 | 0.9186286880701303 | 0.9017733146314243 | 0.9346672469827085 | 1000 |
| high_quality_primary | workspace_late_late_full | 0.777452181220002 | 0.7475536137145079 | 0.8082793700020184 | 0.9181790536890693 | 0.901015284095578 | 0.934091399889181 | 1000 |
| high_quality_primary | workspace_late_late_single | 0.7437689601640722 | 0.713907893869633 | 0.7726234547028715 | 0.9065714183110979 | 0.8878629431170205 | 0.9217160126670821 | 1000 |
| high_quality_primary | workspace_noise_single | 0.7437689601640722 | 0.7120466048955038 | 0.775045222553583 | 0.9065714183110979 | 0.8886589243017147 | 0.9239498674077187 | 1000 |
| primary_with_llm_judge | baseline_output_confidence | 0.8054905420113966 | 0.7754092228163885 | 0.8355647173966755 | 0.9233209435787814 | 0.90384544397707 | 0.9402559415637977 | 1000 |
| primary_with_llm_judge | combined_compact | 0.8112279378810405 | 0.7829998970077495 | 0.8392818242631012 | 0.9268696382549543 | 0.909862337870887 | 0.9433872451374542 | 1000 |
| primary_with_llm_judge | combined_full | 0.8142655919868534 | 0.7833180286333431 | 0.8424215896500361 | 0.9262522914144177 | 0.9068919308826711 | 0.9434830674416125 | 1000 |
| primary_with_llm_judge | commitment_dynamics_full | 0.7278240579359604 | 0.6946230223915313 | 0.758366350690982 | 0.9002659766049479 | 0.8784017470142652 | 0.9181143187118184 | 1000 |
| primary_with_llm_judge | commitment_dynamics_single | 0.721588685983396 | 0.6895992850173214 | 0.7530035197998639 | 0.8984228038334648 | 0.8804105846043211 | 0.9172722154639823 | 1000 |
| primary_with_llm_judge | layer_l33_diff | 0.606271653067177 | 0.5675214140835557 | 0.6489399674909071 | 0.8029649556836396 | 0.773684060986254 | 0.8375871756231642 | 1000 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.7800048374819483 | 0.7511980111170476 | 0.8106629510287092 | 0.9200510918856828 | 0.9046164993288095 | 0.9364150173000606 | 1000 |
| primary_with_llm_judge | layer_l33_full | 0.7516450995596469 | 0.7180835061928421 | 0.7827485787851863 | 0.9019184370106258 | 0.8825719149516518 | 0.9211360316406324 | 1000 |
| primary_with_llm_judge | layer_l33_single | 0.7407998918680506 | 0.7022149389112894 | 0.7732491303974478 | 0.8894663419524278 | 0.867070724629465 | 0.9129219749206272 | 1000 |
| primary_with_llm_judge | workspace_compact | 0.7355355732771807 | 0.7052082577232127 | 0.766282797371694 | 0.9012505508210116 | 0.8819183435788857 | 0.9196448289821003 | 1000 |
| primary_with_llm_judge | workspace_full | 0.7839459624810592 | 0.7539329427263736 | 0.8109706177743078 | 0.9190076429770186 | 0.9013413239698392 | 0.9346045283875478 | 1000 |
| primary_with_llm_judge | workspace_late_late_full | 0.77677866385903 | 0.7441689448620474 | 0.8055467931514547 | 0.9180665979262637 | 0.9009042034799698 | 0.9337442481412123 | 1000 |
| primary_with_llm_judge | workspace_late_late_single | 0.743570773072299 | 0.7116758332009564 | 0.7756093454172724 | 0.9064506837554087 | 0.8879431252931972 | 0.9224623739511976 | 1000 |
| primary_with_llm_judge | workspace_noise_single | 0.743570773072299 | 0.7136523442871455 | 0.7752984879389444 | 0.9064506837554087 | 0.8890300769783124 | 0.9238109671115952 | 1000 |
| strict | baseline_output_confidence | 0.8084590477043138 | 0.7761440803610717 | 0.8368440294577307 | 0.9382817091271821 | 0.9223101573470845 | 0.9532939214636396 | 1000 |
| strict | combined_compact | 0.8125848665264037 | 0.780389008477815 | 0.8407173292662637 | 0.9415679179418344 | 0.9263188069928497 | 0.954335804860568 | 1000 |
| strict | combined_full | 0.8229031439783936 | 0.7907501559707844 | 0.8524784473333497 | 0.9432664807335702 | 0.9263808119649248 | 0.9573138120231796 | 1000 |
| strict | commitment_dynamics_full | 0.7249242729456704 | 0.6928118621196694 | 0.7584505933698624 | 0.9169409779913913 | 0.8996227217902731 | 0.9328672126975261 | 1000 |
| strict | commitment_dynamics_single | 0.7180491517077756 | 0.6845511183312486 | 0.7501693440036866 | 0.912903698977259 | 0.8950889729267653 | 0.9294425164556931 | 1000 |
| strict | layer_l33_diff | 0.6399980601936822 | 0.5958754405034193 | 0.6831075621084939 | 0.8561631934231921 | 0.8303060740168461 | 0.8839096001655896 | 1000 |
| strict | layer_l33_diff_in_full | 0.7827528835966995 | 0.7529266632539583 | 0.8127406107027033 | 0.9336493104008502 | 0.918808658301658 | 0.9468303733070508 | 1000 |
| strict | layer_l33_full | 0.7659250637897848 | 0.7314559168337703 | 0.7999234828001017 | 0.9248988861271253 | 0.9075822801727598 | 0.9414012566229139 | 1000 |
| strict | layer_l33_single | 0.7587216676365698 | 0.7230940300112509 | 0.7920563060693016 | 0.9183717847567716 | 0.8983357272864353 | 0.9362828362532469 | 1000 |
| strict | workspace_compact | 0.7350448393691154 | 0.7015543577933219 | 0.7671423187115376 | 0.9195662111373315 | 0.9028909395237056 | 0.9355582209993321 | 1000 |
| strict | workspace_full | 0.7897138039601892 | 0.7573863486729512 | 0.8172962381786444 | 0.9354667739904248 | 0.9191309602978417 | 0.948438046472103 | 1000 |
| strict | workspace_late_late_full | 0.7824395302684393 | 0.7497974229522613 | 0.8117140779281125 | 0.9334548947806638 | 0.9180096976817123 | 0.9465442741463432 | 1000 |
| strict | workspace_late_late_single | 0.7406292433263201 | 0.7106237545367068 | 0.7712584608161128 | 0.922047950153027 | 0.9074280230934896 | 0.936067778198285 | 1000 |
| strict | workspace_noise_single | 0.7406292433263201 | 0.7063684479242217 | 0.7712180815468429 | 0.922047950153027 | 0.9070112584838588 | 0.9363025400696555 | 1000 |


## Permutation sanity checks

| label_regime | feature_set | real_roc_auc | perm_auc_mean | perm_auc_ci_low | perm_auc_ci_high | p_perm_ge_real | permutation_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.8040431266846362 | 0.499362723100459 | 0.4630889852116268 | 0.5386777883004298 | 0.0 | 500 |
| expanded_deterministic | combined_compact | 0.8092518394405186 | 0.5006462154877249 | 0.4615969439790194 | 0.5408419538136519 | 0.0 | 500 |
| expanded_deterministic | combined_full | 0.8167735120565309 | 0.49955776207474323 | 0.4607998834413929 | 0.5379722444816785 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_full | 0.724768704013987 | 0.49911312741312747 | 0.4615938478910177 | 0.5403484920230204 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_single | 0.7165841043199535 | 0.5004687622932906 | 0.46079086836162314 | 0.5354146936694106 | 0.0 | 500 |
| expanded_deterministic | layer_l33_diff | 0.6236067603992133 | 0.4998488963356888 | 0.4574395352225541 | 0.536763586362643 | 0.0 | 500 |
| expanded_deterministic | layer_l33_diff_in_full | 0.7770088147446638 | 0.5014280177751875 | 0.46170831208567054 | 0.5390643439935893 | 0.0 | 500 |
| expanded_deterministic | layer_l33_full | 0.7538427915786405 | 0.49961542944561815 | 0.45812914329423765 | 0.5393892511109492 | 0.0 | 500 |
| expanded_deterministic | layer_l33_single | 0.7492423690536897 | 0.4998427551540759 | 0.46397273621330226 | 0.538676695563488 | 0.0 | 500 |
| expanded_deterministic | workspace_compact | 0.7359109783638087 | 0.4983610111459168 | 0.45504644132002625 | 0.534426039921323 | 0.0 | 500 |
| expanded_deterministic | workspace_full | 0.7824943541924675 | 0.4986558315728126 | 0.4596549683106287 | 0.5347421140817368 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_full | 0.777427697239018 | 0.5011083266554965 | 0.46437777737306035 | 0.540859710788956 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_single | 0.7375209441247177 | 0.4986204487506374 | 0.4610906425293218 | 0.5346581554600423 | 0.0 | 500 |
| expanded_deterministic | workspace_noise_single | 0.7375209441247177 | 0.49914145843957164 | 0.4582066365556931 | 0.5388568150360603 | 0.0 | 500 |
| high_quality_primary | baseline_output_confidence | 0.8057090567273866 | 0.5004559910557874 | 0.4639238816173643 | 0.5374912765442296 | 0.0 | 500 |
| high_quality_primary | combined_compact | 0.8099283608448578 | 0.49998653383276603 | 0.4647866135900759 | 0.5371649480865366 | 0.0 | 500 |
| high_quality_primary | combined_full | 0.8131578197769643 | 0.4997726631820318 | 0.4622551201344481 | 0.5402725456824234 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_full | 0.7272264395482319 | 0.5004515474342358 | 0.46122877885861585 | 0.5391533619130361 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_single | 0.7216469884494324 | 0.5013658296896587 | 0.4664034794126444 | 0.5408069908706366 | 0.0 | 500 |
| high_quality_primary | layer_l33_diff | 0.6043467733895433 | 0.5005354991240938 | 0.4632249369774828 | 0.5360788778431345 | 0.0 | 500 |
| high_quality_primary | layer_l33_diff_in_full | 0.7794461139674989 | 0.4997056527993392 | 0.4604288913733923 | 0.5359179389856579 | 0.0 | 500 |
| high_quality_primary | layer_l33_full | 0.7510788600401634 | 0.49935944198367826 | 0.46064733382706907 | 0.5371976165382479 | 0.0 | 500 |
| high_quality_primary | layer_l33_single | 0.7396992010026633 | 0.49899910273026366 | 0.46396028869297706 | 0.532100180878185 | 0.0 | 500 |
| high_quality_primary | workspace_compact | 0.7351950493498356 | 0.500442702918263 | 0.45883178684858933 | 0.540851053223762 | 0.0 | 500 |
| high_quality_primary | workspace_full | 0.7838968567074474 | 0.4988851565949326 | 0.4642076609744634 | 0.5324442232919829 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_full | 0.777452181220002 | 0.4994581487758677 | 0.46349856864113487 | 0.5420402916838761 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_single | 0.7437689601640722 | 0.4993445230940139 | 0.46037120974748263 | 0.5391360040163502 | 0.0 | 500 |
| high_quality_primary | workspace_noise_single | 0.7437689601640722 | 0.5007044137125604 | 0.46403265776992864 | 0.5355459459074531 | 0.0 | 500 |
| primary_with_llm_judge | baseline_output_confidence | 0.8054905420113966 | 0.4996855992430764 | 0.4586622050380952 | 0.5385514409293656 | 0.0 | 500 |
| primary_with_llm_judge | combined_compact | 0.8112279378810405 | 0.49951366944347614 | 0.4661784426153704 | 0.5354649673825665 | 0.0 | 500 |
| primary_with_llm_judge | combined_full | 0.8142655919868534 | 0.5001835326423323 | 0.4610134524681829 | 0.539091744979334 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_full | 0.7278240579359604 | 0.5010763183916795 | 0.46277522071011384 | 0.5366734486266531 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_single | 0.721588685983396 | 0.5007270166252872 | 0.4631726234091443 | 0.5366085338872724 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_diff | 0.606271653067177 | 0.5023055296687037 | 0.45942099609444476 | 0.544412530501035 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.7800048374819483 | 0.49974539194274703 | 0.4635308994159452 | 0.539311210153021 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_full | 0.7516450995596469 | 0.5003497286030348 | 0.4670126414785621 | 0.5362226024230093 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_single | 0.7407998918680506 | 0.50039597635325 | 0.4641167327077805 | 0.5365076048061805 | 0.0 | 500 |
| primary_with_llm_judge | workspace_compact | 0.7355355732771807 | 0.4991469385141816 | 0.4600247031706849 | 0.537046219294439 | 0.0 | 500 |
| primary_with_llm_judge | workspace_full | 0.7839459624810592 | 0.49898867460108554 | 0.458959923596241 | 0.534613072583571 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_full | 0.77677866385903 | 0.49954307137420056 | 0.4649593793795218 | 0.536963163997752 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_single | 0.743570773072299 | 0.499703441014733 | 0.46347149798319687 | 0.5365357938094459 | 0.0 | 500 |
| primary_with_llm_judge | workspace_noise_single | 0.743570773072299 | 0.49989478476762306 | 0.4625793204760651 | 0.5319031934494803 | 0.0 | 500 |
| strict | baseline_output_confidence | 0.8084590477043138 | 0.5010207484668069 | 0.46160414521688525 | 0.5406429525344316 | 0.0 | 500 |
| strict | combined_compact | 0.8125848665264037 | 0.5003334004804751 | 0.4639173642508618 | 0.5372853156661742 | 0.0 | 500 |
| strict | combined_full | 0.8229031439783936 | 0.5016124416192906 | 0.4638614082993867 | 0.5390035364161332 | 0.0 | 500 |
| strict | commitment_dynamics_full | 0.7249242729456704 | 0.4998942880164734 | 0.4582067796230807 | 0.5421456496112925 | 0.0 | 500 |
| strict | commitment_dynamics_single | 0.7180491517077756 | 0.5002361341152245 | 0.46296844457376485 | 0.5403973991673755 | 0.0 | 500 |
| strict | layer_l33_diff | 0.6399980601936822 | 0.49948489189310175 | 0.4590533931688975 | 0.5371872994911739 | 0.0 | 500 |
| strict | layer_l33_diff_in_full | 0.7827528835966995 | 0.5013837608368026 | 0.45924140516585343 | 0.5429400376023994 | 0.0 | 500 |
| strict | layer_l33_full | 0.7659250637897848 | 0.5006123222465941 | 0.46045508975334615 | 0.5444764947699837 | 0.0 | 500 |
| strict | layer_l33_single | 0.7587216676365698 | 0.4986609666204097 | 0.46007076562663207 | 0.5407910492860021 | 0.0 | 500 |
| strict | workspace_compact | 0.7350448393691154 | 0.5006861990241283 | 0.4609279175433099 | 0.5376794320843965 | 0.0 | 500 |
| strict | workspace_full | 0.7897138039601892 | 0.4991322500261128 | 0.4572632690212931 | 0.5379235865526657 | 0.0 | 500 |
| strict | workspace_late_late_full | 0.7824395302684393 | 0.5005059313308563 | 0.4610543779936434 | 0.5419056918393839 | 0.0 | 500 |
| strict | workspace_late_late_single | 0.7406292433263201 | 0.5003211498574989 | 0.46182106778877 | 0.539687597922915 | 0.0 | 500 |
| strict | workspace_noise_single | 0.7406292433263201 | 0.5002637763552532 | 0.4603191167912619 | 0.5398600355133772 | 0.0 | 500 |


## H.3 quadrant analysis

| quadrant | n | accuracy | wrong_rate | mean_confidence | mean_workspace_noise |
| --- | --- | --- | --- | --- | --- |
| high_confidence__clean_workspace | 250 | 0.492 | 0.508 | 0.9450358762741089 | 1.211894944343812 |
| high_confidence__noisy_workspace | 459 | 0.2657952069716776 | 0.7342047930283224 | 0.843445878273002 | 2.055902483005281 |
| low_confidence__clean_workspace | 29 | 0.06896551724137931 | 0.9310344827586207 | 0.4881832918216442 | 1.3659211341677036 |
| low_confidence__noisy_workspace | 531 | 0.07344632768361582 | 0.9265536723163842 | 0.4335425375713467 | 2.315010795282049 |


## Conclusion

**supports_H_B_or_redundant** — Workspace features did not materially improve over output confidence under the primary label regime; signals may be redundant for this model/dataset. The single-feature `workspace_noise_score` AUC is 0.744 with CI [0.714, 0.775]; CI overlaps baseline upper bound (0.836), so the parsimonious claim is not statistically distinguishable either.

## Artefact guide

See `AGENT_BRIEF.md` for the most useful machine-readable files and selected examples.
