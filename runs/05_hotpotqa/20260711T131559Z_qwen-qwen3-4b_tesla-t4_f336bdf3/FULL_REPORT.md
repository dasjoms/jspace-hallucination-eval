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
  "DATASET_ID": "hotpotqa_distractor",
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

- Dataset ID: `hotpotqa_distractor`
- Repo: `hotpotqa/hotpot_qa`
- Config: `distractor`
- Split: `validation`
- Task family: `multi_hop_factual`
- Prompt template: `short_answer_v1`

```json
{
  "dataset_id": "hotpotqa_distractor",
  "repo": "hotpotqa/hotpot_qa",
  "config": "distractor",
  "split": "validation",
  "task_family": "multi_hop_factual",
  "answer_format": "short_freeform",
  "prompt_template_id": "short_answer_v1",
  "max_new_tokens": 16,
  "n_total_in_split": 7405,
  "n_requested": 2000,
  "random_seed": 42,
  "expected_failure_mode": "multi_hop_intermediate_uncertainty",
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


## Descriptive statistics

| feature | mean_correct | mean_wrong | std_correct | std_wrong | cohen_d_wrong_minus_correct |
| --- | --- | --- | --- | --- | --- |
| first_content_token_prob | 0.7041919088320612 | 0.6149185334382283 | 0.2355280100285067 | 0.22073790085918754 | -0.4003753311119598 |
| sequence_content_logprob_mean | -0.27101935377621383 | -0.35290133657950407 | 0.13096238077778335 | 0.16479904990886218 | -0.510893211682307 |
| workspace_noise_score | 1.321009587178246 | 1.8382884478869181 | 0.6089874822007956 | 0.7139664825428388 | 0.7394700115184702 |
| late_entropy_topk_mean | 1.3696132500210505 | 1.7240687050318426 | 0.5377972065013893 | 0.6174303615164689 | 0.5845405842178277 |
| late_effective_concepts_topk_mean | 6.158651392249506 | 8.786060522432109 | 3.5448181785292534 | 5.3598390217589165 | 0.5118184106845469 |
| late_top1_dominance_topk_mean | 0.61179103492507 | 0.5182386603989567 | 0.1462029195545163 | 0.15887338178058483 | -0.5955891591491907 |
| late_top1_margin_mean | 1.892937725631769 | 1.4618196350592638 | 1.0859370647806734 | 0.8780014039074265 | -0.47295639721187405 |
| late_distinct_top1_count | 3.7509025270758123 | 4.031815346225827 | 1.2907309949537003 | 1.3660264823205341 | 0.20728162869973227 |
| late_top1_churn_rate | 0.4522949974213512 | 0.4873897157116121 | 0.21313719311768706 | 0.22060590701115293 | 0.15986719805399932 |
| late_top5_jaccard_adjacent_mean | 0.4682805733605115 | 0.46304052916654287 | 0.14186047127498233 | 0.13722752824895004 | -0.03799386572069513 |


## Predictive AUC results

| label_regime | feature_set | features | roc_auc | roc_auc_per_fold_std | n_folds_with_both_classes | pr_auc | n_splits | n | n_wrong |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.629963721933523 | 0.0682725391927068 | 5 | 0.9863555064218006 | 5 | 2000 | 1953 |
| strict | workspace_noise_single | ['workspace_noise_score'] | 0.7757405410116461 | 0.05532375169886125 | 5 | 0.9928834150110544 | 5 | 2000 | 1953 |
| strict | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7099279885827587 | 0.10780501079288109 | 5 | 0.9888862980122863 | 5 | 2000 | 1953 |
| strict | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8297000795284941 | 0.06737883545402022 | 5 | 0.9942295439638682 | 5 | 2000 | 1953 |
| strict | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.737436132082666 | 0.0649316965559983 | 5 | 0.9915561149863632 | 5 | 2000 | 1953 |
| strict | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8502903334749594 | 0.039181467455772674 | 5 | 0.995488442752506 | 5 | 2000 | 1953 |
| strict | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7757405410116461 | 0.05532375169886125 | 5 | 0.9928834150110544 | 5 | 2000 | 1953 |
| strict | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.8430782974365679 | 0.035620193101842196 | 5 | 0.9953174317471004 | 5 | 2000 | 1953 |
| strict | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.689130742665403 | 0.07239391849948912 | 5 | 0.9893994424622801 | 5 | 2000 | 1953 |
| strict | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7022257084027845 | 0.10067611950281813 | 5 | 0.9878999523005494 | 5 | 2000 | 1953 |
| strict | layer_l33_single | ['layer_l33_entropy_topk'] | 0.8309638199823512 | 0.035306669320066854 | 5 | 0.9947519997927328 | 5 | 2000 | 1953 |
| strict | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.8349293503720407 | 0.0472833078840178 | 5 | 0.9947577588458565 | 5 | 2000 | 1953 |
| strict | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.54848514560251 | 0.05116145163486787 | 5 | 0.9830431553584651 | 5 | 2000 | 1953 |
| strict | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.8593544029371072 | 0.041251015386101444 | 5 | 0.9955081747388915 | 5 | 2000 | 1953 |
| expanded_deterministic | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.606308023872679 | 0.036804505141272634 | 5 | 0.9213670655594406 | 5 | 2000 | 1768 |
| expanded_deterministic | workspace_noise_single | ['workspace_noise_score'] | 0.694765173974099 | 0.02887929608868665 | 5 | 0.9441973205593683 | 5 | 2000 | 1768 |
| expanded_deterministic | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.6557038929630208 | 0.04759315730076069 | 5 | 0.9354194089434585 | 5 | 2000 | 1768 |
| expanded_deterministic | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7254520010922141 | 0.040257913967949616 | 5 | 0.951431665239669 | 5 | 2000 | 1768 |
| expanded_deterministic | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.6695662349820565 | 0.040547436266476694 | 5 | 0.9390665949772972 | 5 | 2000 | 1768 |
| expanded_deterministic | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7234138516149164 | 0.035632994530681805 | 5 | 0.9508773729424543 | 5 | 2000 | 1768 |
| expanded_deterministic | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.694765173974099 | 0.02887929608868665 | 5 | 0.9441973205593683 | 5 | 2000 | 1768 |
| expanded_deterministic | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7444779801841162 | 0.04062633800053447 | 5 | 0.9538548392435915 | 5 | 2000 | 1768 |
| expanded_deterministic | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.6547091980028086 | 0.043794671857779646 | 5 | 0.9354229992344494 | 5 | 2000 | 1768 |
| expanded_deterministic | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.654421516617257 | 0.05220145828296078 | 5 | 0.9339754190613798 | 5 | 2000 | 1768 |
| expanded_deterministic | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7336094749570915 | 0.02916120018251195 | 5 | 0.9471355407141692 | 5 | 2000 | 1768 |
| expanded_deterministic | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7450362771103136 | 0.034659847708826956 | 5 | 0.949574619911034 | 5 | 2000 | 1768 |
| expanded_deterministic | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.4412325440786394 | 0.039037881944350365 | 5 | 0.869954467635147 | 5 | 2000 | 1768 |
| expanded_deterministic | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7546516617256982 | 0.039905345239647845 | 5 | 0.9547281527447897 | 5 | 2000 | 1768 |
| primary_with_llm_judge | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.6596724102596441 | 0.030217696071036124 | 5 | 0.91236348921451 | 5 | 1880 | 1603 |
| primary_with_llm_judge | workspace_noise_single | ['workspace_noise_score'] | 0.7044440590859646 | 0.015164096440444383 | 5 | 0.9319674953248406 | 5 | 1880 | 1603 |
| primary_with_llm_judge | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.6690839153122192 | 0.02591793151642798 | 5 | 0.922032947721833 | 5 | 1880 | 1603 |
| primary_with_llm_judge | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7491706660120576 | 0.03367531742280631 | 5 | 0.9439427657094743 | 5 | 1880 | 1603 |
| primary_with_llm_judge | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7050408642639816 | 0.03221634978725125 | 5 | 0.9308289437485667 | 5 | 1880 | 1603 |
| primary_with_llm_judge | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7532356975076065 | 0.03210905237158996 | 5 | 0.9444109748472826 | 5 | 1880 | 1603 |
| primary_with_llm_judge | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7044440590859646 | 0.015164096440444383 | 5 | 0.9319674953248406 | 5 | 1880 | 1603 |
| primary_with_llm_judge | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7605414937245374 | 0.0370177413230843 | 5 | 0.9447768414085375 | 5 | 1880 | 1603 |
| primary_with_llm_judge | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.6591183948868435 | 0.02529285268815018 | 5 | 0.9202161499786491 | 5 | 1880 | 1603 |
| primary_with_llm_judge | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.6685389083194643 | 0.0274647466298281 | 5 | 0.9218138883863544 | 5 | 1880 | 1603 |
| primary_with_llm_judge | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7348563501196989 | 0.03502273661120965 | 5 | 0.934017344372766 | 5 | 1880 | 1603 |
| primary_with_llm_judge | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7428039934148742 | 0.03195683961329368 | 5 | 0.9366607609174287 | 5 | 1880 | 1603 |
| primary_with_llm_judge | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5389668739344775 | 0.027720368666254585 | 5 | 0.8741955361159364 | 5 | 1880 | 1603 |
| primary_with_llm_judge | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7699687634421922 | 0.043264377902072 | 5 | 0.9472465627657396 | 5 | 1880 | 1603 |
| high_quality_primary | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.6623465703971119 | 0.033095109143511256 | 5 | 0.9134857689403595 | 5 | 1877 | 1600 |
| high_quality_primary | workspace_noise_single | ['workspace_noise_score'] | 0.7041493682310469 | 0.01858781468920611 | 5 | 0.9317975378666022 | 5 | 1877 | 1600 |
| high_quality_primary | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.6680437725631769 | 0.03481071137115908 | 5 | 0.9213927843777805 | 5 | 1877 | 1600 |
| high_quality_primary | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7496547833935018 | 0.031382829893348896 | 5 | 0.9439723519029326 | 5 | 1877 | 1600 |
| high_quality_primary | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7065478339350181 | 0.036700083170753635 | 5 | 0.9310969847862859 | 5 | 1877 | 1600 |
| high_quality_primary | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7546841155234657 | 0.02746362091506192 | 5 | 0.9446780074568104 | 5 | 1877 | 1600 |
| high_quality_primary | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7041493682310469 | 0.01858781468920611 | 5 | 0.9317975378666022 | 5 | 1877 | 1600 |
| high_quality_primary | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7604174187725632 | 0.035603788784814655 | 5 | 0.9447131485588184 | 5 | 1877 | 1600 |
| high_quality_primary | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.6590636281588448 | 0.032136594793375245 | 5 | 0.9199109911772227 | 5 | 1877 | 1600 |
| high_quality_primary | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.6696953971119133 | 0.036701880294675686 | 5 | 0.9218901593552484 | 5 | 1877 | 1600 |
| high_quality_primary | layer_l33_single | ['layer_l33_entropy_topk'] | 0.7346389891696752 | 0.03742195415399638 | 5 | 0.93337011585507 | 5 | 1877 | 1600 |
| high_quality_primary | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.7423984657039711 | 0.0329830968646355 | 5 | 0.9359731899864356 | 5 | 1877 | 1600 |
| high_quality_primary | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.54076940433213 | 0.025249290186754904 | 5 | 0.8749470124356311 | 5 | 1877 | 1600 |
| high_quality_primary | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7703339350180505 | 0.04243909543892858 | 5 | 0.9473020015893072 | 5 | 1877 | 1600 |


## Bootstrap AUC intervals

| label_regime | feature_set | roc_auc | roc_auc_ci_low | roc_auc_ci_high | pr_auc | pr_auc_ci_low | pr_auc_ci_high | bootstrap_n_effective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.606308023872679 | 0.572256417586882 | 0.6415007696507526 | 0.9213670655594406 | 0.9067663275903414 | 0.9361195086038074 | 1000 |
| expanded_deterministic | combined_compact | 0.6695662349820565 | 0.6320033219162773 | 0.6999552866116688 | 0.9390665949772972 | 0.9269451771618341 | 0.9501411099569821 | 1000 |
| expanded_deterministic | combined_full | 0.7234138516149164 | 0.6922347341542736 | 0.7538980388838515 | 0.9508773729424543 | 0.9415895754452668 | 0.9607032290824057 | 1000 |
| expanded_deterministic | commitment_dynamics_full | 0.654421516617257 | 0.619315872912815 | 0.689388431581175 | 0.9339754190613798 | 0.9215522507174594 | 0.9458373219213787 | 1000 |
| expanded_deterministic | commitment_dynamics_single | 0.6547091980028086 | 0.6221574317434724 | 0.6866246475902883 | 0.9354229992344494 | 0.9236940922744824 | 0.9468067598985714 | 1000 |
| expanded_deterministic | layer_l33_diff | 0.4412325440786394 | 0.4048775929736918 | 0.47670504925706647 | 0.869954467635147 | 0.8505877661433179 | 0.8906428171661496 | 1000 |
| expanded_deterministic | layer_l33_diff_in_full | 0.7546516617256982 | 0.7249584553009624 | 0.7844195879044423 | 0.9547281527447897 | 0.9431193677155411 | 0.9643298942689591 | 1000 |
| expanded_deterministic | layer_l33_full | 0.7450362771103136 | 0.7097184612222921 | 0.7769337910045219 | 0.949574619911034 | 0.9369614448773002 | 0.9616612825356431 | 1000 |
| expanded_deterministic | layer_l33_single | 0.7336094749570915 | 0.7004379922998485 | 0.7652541078702982 | 0.9471355407141692 | 0.9344065935855805 | 0.9601309583830242 | 1000 |
| expanded_deterministic | workspace_compact | 0.6557038929630208 | 0.6182315788668896 | 0.6906830274856351 | 0.9354194089434585 | 0.9236605611310724 | 0.9468251689554336 | 1000 |
| expanded_deterministic | workspace_full | 0.7254520010922141 | 0.6919389223166954 | 0.7574163662462522 | 0.951431665239669 | 0.9408846425409 | 0.9605694945935964 | 1000 |
| expanded_deterministic | workspace_late_late_full | 0.7444779801841162 | 0.7127329562743008 | 0.7745070194098597 | 0.9538548392435915 | 0.9431464857085579 | 0.9636715791277537 | 1000 |
| expanded_deterministic | workspace_late_late_single | 0.694765173974099 | 0.6603445852565891 | 0.7267183255500828 | 0.9441973205593683 | 0.9335224982313931 | 0.9549679440812555 | 1000 |
| expanded_deterministic | workspace_noise_single | 0.694765173974099 | 0.6619586938066941 | 0.7307973364678367 | 0.9441973205593683 | 0.9329733614009902 | 0.9549563659418374 | 1000 |
| high_quality_primary | baseline_output_confidence | 0.6623465703971119 | 0.6286155790981867 | 0.6946944681744127 | 0.9134857689403595 | 0.8959718616206276 | 0.929160591248899 | 1000 |
| high_quality_primary | combined_compact | 0.7065478339350181 | 0.6741651893389947 | 0.7382927613275128 | 0.9310969847862859 | 0.9180350168129362 | 0.9438687412271255 | 1000 |
| high_quality_primary | combined_full | 0.7546841155234657 | 0.7255895609321308 | 0.7858184608954568 | 0.9446780074568104 | 0.9328392974327349 | 0.9548699348793142 | 1000 |
| high_quality_primary | commitment_dynamics_full | 0.6696953971119133 | 0.6395047000965401 | 0.7021182795201106 | 0.9218901593552484 | 0.9076759177417146 | 0.9348043105179532 | 1000 |
| high_quality_primary | commitment_dynamics_single | 0.6590636281588448 | 0.6275333923030836 | 0.6918087398616937 | 0.9199109911772227 | 0.9061180893685963 | 0.9328822357345069 | 1000 |
| high_quality_primary | layer_l33_diff | 0.54076940433213 | 0.5064662661071212 | 0.5739382874721498 | 0.8749470124356311 | 0.85479826222908 | 0.8949657598964932 | 1000 |
| high_quality_primary | layer_l33_diff_in_full | 0.7703339350180505 | 0.7416224159776115 | 0.7976761675852888 | 0.9473020015893072 | 0.9356266832548809 | 0.9577391452467622 | 1000 |
| high_quality_primary | layer_l33_full | 0.7423984657039711 | 0.7106924594162328 | 0.7719340480874015 | 0.9359731899864356 | 0.9219650216835097 | 0.948161183974932 | 1000 |
| high_quality_primary | layer_l33_single | 0.7346389891696752 | 0.700370037442452 | 0.765146679184206 | 0.93337011585507 | 0.91781921694072 | 0.9465475887723541 | 1000 |
| high_quality_primary | workspace_compact | 0.6680437725631769 | 0.6330480386243577 | 0.7015451111273691 | 0.9213927843777805 | 0.9072640661870665 | 0.9351905953467979 | 1000 |
| high_quality_primary | workspace_full | 0.7496547833935018 | 0.7196911139495185 | 0.7780974370652258 | 0.9439723519029326 | 0.9335298892517804 | 0.9542933064121426 | 1000 |
| high_quality_primary | workspace_late_late_full | 0.7604174187725632 | 0.7313170149651769 | 0.786314620345975 | 0.9447131485588184 | 0.9323505028099804 | 0.9548060099829172 | 1000 |
| high_quality_primary | workspace_late_late_single | 0.7041493682310469 | 0.6755906667522924 | 0.7350984294396509 | 0.9317975378666022 | 0.9198908851407928 | 0.944054674155869 | 1000 |
| high_quality_primary | workspace_noise_single | 0.7041493682310469 | 0.6728750660572251 | 0.7325052179787312 | 0.9317975378666022 | 0.9191155497980473 | 0.9436211108941884 | 1000 |
| primary_with_llm_judge | baseline_output_confidence | 0.6596724102596441 | 0.6269592171866541 | 0.6935227578584094 | 0.91236348921451 | 0.8952429091380247 | 0.9286176356232324 | 1000 |
| primary_with_llm_judge | combined_compact | 0.7050408642639816 | 0.6747075498355882 | 0.7338147080293165 | 0.9308289437485667 | 0.9176895835704942 | 0.9427174073001388 | 1000 |
| primary_with_llm_judge | combined_full | 0.7532356975076065 | 0.7245192474855695 | 0.7828178520885674 | 0.9444109748472826 | 0.9333312790014866 | 0.9552726976577588 | 1000 |
| primary_with_llm_judge | commitment_dynamics_full | 0.6685389083194643 | 0.6360130427163606 | 0.7030597327851391 | 0.9218138883863544 | 0.9082987507303636 | 0.9345593788778088 | 1000 |
| primary_with_llm_judge | commitment_dynamics_single | 0.6591183948868435 | 0.6271732895801782 | 0.6917769258893789 | 0.9202161499786491 | 0.9055451147193905 | 0.9335941010436783 | 1000 |
| primary_with_llm_judge | layer_l33_diff | 0.5389668739344775 | 0.5033289958312384 | 0.57569307579204 | 0.8741955361159364 | 0.8544918114508623 | 0.8948409923180667 | 1000 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.7699687634421922 | 0.7425181303836732 | 0.7971708230388441 | 0.9472465627657396 | 0.9362809558965007 | 0.9575681036241085 | 1000 |
| primary_with_llm_judge | layer_l33_full | 0.7428039934148742 | 0.7104245878451865 | 0.7716729550366694 | 0.9366607609174287 | 0.9231852281798835 | 0.9492499261494458 | 1000 |
| primary_with_llm_judge | layer_l33_single | 0.7348563501196989 | 0.7003024971805842 | 0.764420868026212 | 0.934017344372766 | 0.9206035656128868 | 0.9467674387632476 | 1000 |
| primary_with_llm_judge | workspace_compact | 0.6690839153122192 | 0.636345913955987 | 0.7007418848851577 | 0.922032947721833 | 0.9077633939115127 | 0.9348604946201156 | 1000 |
| primary_with_llm_judge | workspace_full | 0.7491706660120576 | 0.7186075308979675 | 0.7780950700038763 | 0.9439427657094743 | 0.933677364713448 | 0.9539150630810249 | 1000 |
| primary_with_llm_judge | workspace_late_late_full | 0.7605414937245374 | 0.7336238945867266 | 0.7876784798505886 | 0.9447768414085375 | 0.934374790833372 | 0.9547669907706368 | 1000 |
| primary_with_llm_judge | workspace_late_late_single | 0.7044440590859646 | 0.673607920001014 | 0.7373097480067451 | 0.9319674953248406 | 0.9195473818802423 | 0.9439642593146649 | 1000 |
| primary_with_llm_judge | workspace_noise_single | 0.7044440590859646 | 0.6727240393712377 | 0.734361398680242 | 0.9319674953248406 | 0.9193081216500479 | 0.9439290393118566 | 1000 |
| strict | baseline_output_confidence | 0.629963721933523 | 0.5602314212742892 | 0.6963480118048082 | 0.9863555064218006 | 0.9802835985212452 | 0.9916166443110077 | 1000 |
| strict | combined_compact | 0.737436132082666 | 0.6788368092234328 | 0.7948734300541843 | 0.9915561149863632 | 0.9878498060767557 | 0.9947347155041222 | 1000 |
| strict | combined_full | 0.8502903334749594 | 0.7977354306983337 | 0.8938979031879254 | 0.995488442752506 | 0.9928956443569392 | 0.9975032069064708 | 1000 |
| strict | commitment_dynamics_full | 0.7022257084027845 | 0.6303165592623076 | 0.7716911101857629 | 0.9878999523005494 | 0.9807178142230624 | 0.9935219993594676 | 1000 |
| strict | commitment_dynamics_single | 0.689130742665403 | 0.6189277000685729 | 0.7550479397196727 | 0.9893994424622801 | 0.9850490884155085 | 0.9933790407392945 | 1000 |
| strict | layer_l33_diff | 0.54848514560251 | 0.4814382590383548 | 0.6105159216825348 | 0.9830431553584651 | 0.9765604144094555 | 0.9886826994727035 | 1000 |
| strict | layer_l33_diff_in_full | 0.8593544029371072 | 0.8081035143073294 | 0.9021124075489039 | 0.9955081747388915 | 0.9921732562469303 | 0.9976942561015014 | 1000 |
| strict | layer_l33_full | 0.8349293503720407 | 0.7808393926692059 | 0.8832846623672845 | 0.9947577588458565 | 0.9919508223114423 | 0.9972082879648372 | 1000 |
| strict | layer_l33_single | 0.8309638199823512 | 0.7744058317520508 | 0.8784670449058427 | 0.9947519997927328 | 0.9919373747531247 | 0.9969689051816399 | 1000 |
| strict | workspace_compact | 0.7099279885827587 | 0.6378704937893399 | 0.774173175161435 | 0.9888862980122863 | 0.982384559319454 | 0.9937234463728964 | 1000 |
| strict | workspace_full | 0.8297000795284941 | 0.768681217523759 | 0.8846203337258488 | 0.9942295439638682 | 0.9907222671918121 | 0.9971719463527826 | 1000 |
| strict | workspace_late_late_full | 0.8430782974365679 | 0.7927311735902751 | 0.8841750829147924 | 0.9953174317471004 | 0.9926815026215935 | 0.9973302951880753 | 1000 |
| strict | workspace_late_late_single | 0.7757405410116461 | 0.7109951914856062 | 0.8279520696840635 | 0.9928834150110544 | 0.9896261023626104 | 0.9957714539407116 | 1000 |
| strict | workspace_noise_single | 0.7757405410116461 | 0.717265047504509 | 0.8322965518430931 | 0.9928834150110544 | 0.9896751415773322 | 0.9957690622352723 | 1000 |


## Permutation sanity checks

| label_regime | feature_set | real_roc_auc | perm_auc_mean | perm_auc_ci_low | perm_auc_ci_high | p_perm_ge_real | permutation_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.606308023872679 | 0.4988078824699641 | 0.46114533761117177 | 0.5363209329653612 | 0.0 | 500 |
| expanded_deterministic | combined_compact | 0.6695662349820565 | 0.5002090370962708 | 0.4620504368856296 | 0.5389406620572632 | 0.0 | 500 |
| expanded_deterministic | combined_full | 0.7234138516149164 | 0.49988697047121233 | 0.46147196569277577 | 0.5393939430878452 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_full | 0.654421516617257 | 0.4992923769308785 | 0.4604763564908722 | 0.5349765100834762 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_single | 0.6547091980028086 | 0.4995111025511 | 0.46112711372679044 | 0.5362109801646123 | 0.0 | 500 |
| expanded_deterministic | layer_l33_diff | 0.4412325440786394 | 0.5000944521376189 | 0.4654068009829927 | 0.5382740579653612 | 0.996 | 500 |
| expanded_deterministic | layer_l33_diff_in_full | 0.7546516617256982 | 0.49970453171321577 | 0.4582865038422531 | 0.5406363365969731 | 0.0 | 500 |
| expanded_deterministic | layer_l33_full | 0.7450362771103136 | 0.5013221251365267 | 0.4647293478896864 | 0.5400885229755031 | 0.0 | 500 |
| expanded_deterministic | layer_l33_single | 0.7336094749570915 | 0.5008832940006241 | 0.4593827405796536 | 0.5400365330979872 | 0.0 | 500 |
| expanded_deterministic | workspace_compact | 0.6557038929630208 | 0.5003820165002341 | 0.4580478867608052 | 0.5413419483343735 | 0.0 | 500 |
| expanded_deterministic | workspace_full | 0.7254520010922141 | 0.5002053850054611 | 0.46222194862693083 | 0.5390295872991105 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_full | 0.7444779801841162 | 0.5011291153066001 | 0.4614515476283351 | 0.5386858324231549 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_single | 0.694765173974099 | 0.49974334432048684 | 0.46215594037681385 | 0.5405847124161335 | 0.0 | 500 |
| expanded_deterministic | workspace_noise_single | 0.694765173974099 | 0.49987414670775465 | 0.46071588781401157 | 0.5396665090107662 | 0.0 | 500 |
| high_quality_primary | baseline_output_confidence | 0.6623465703971119 | 0.5007675315884477 | 0.4665177120938628 | 0.5381356611010829 | 0.0 | 500 |
| high_quality_primary | combined_compact | 0.7065478339350181 | 0.5000400135379062 | 0.4651268614620939 | 0.5361317125451264 | 0.0 | 500 |
| high_quality_primary | combined_full | 0.7546841155234657 | 0.4992114801444044 | 0.46241476759927796 | 0.5349651962996389 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_full | 0.6696953971119133 | 0.5001631814079422 | 0.4627319494584838 | 0.5383086078519855 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_single | 0.6590636281588448 | 0.5000373465703971 | 0.4625418546931408 | 0.5348615185018051 | 0.0 | 500 |
| high_quality_primary | layer_l33_diff | 0.54076940433213 | 0.4999619990974729 | 0.4623880302346571 | 0.5383876353790613 | 0.02 | 500 |
| high_quality_primary | layer_l33_diff_in_full | 0.7703339350180505 | 0.4992658393501805 | 0.4632093298736462 | 0.5358861687725631 | 0.0 | 500 |
| high_quality_primary | layer_l33_full | 0.7423984657039711 | 0.4988277256317689 | 0.4600386958483755 | 0.5371246051444044 | 0.0 | 500 |
| high_quality_primary | layer_l33_single | 0.7346389891696752 | 0.5004929151624549 | 0.46151737364620943 | 0.5367766809566787 | 0.0 | 500 |
| high_quality_primary | workspace_compact | 0.6680437725631769 | 0.4994025541516246 | 0.46605398240072204 | 0.5331384250902527 | 0.0 | 500 |
| high_quality_primary | workspace_full | 0.7496547833935018 | 0.49983958935018047 | 0.4595895758122744 | 0.53875377933213 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_full | 0.7604174187725632 | 0.49990078971119134 | 0.4619612477436823 | 0.5370309679602887 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_single | 0.7041493682310469 | 0.49963982400722023 | 0.4653273916967509 | 0.5333166741877255 | 0.0 | 500 |
| high_quality_primary | workspace_noise_single | 0.7041493682310469 | 0.4999587680505415 | 0.4656376353790614 | 0.5347374210288809 | 0.0 | 500 |
| primary_with_llm_judge | baseline_output_confidence | 0.6596724102596441 | 0.500874767752702 | 0.4662462755978749 | 0.5393704493605176 | 0.0 | 500 |
| primary_with_llm_judge | combined_compact | 0.7050408642639816 | 0.5014810047046264 | 0.46701288873975016 | 0.5383142168001783 | 0.0 | 500 |
| primary_with_llm_judge | combined_full | 0.7532356975076065 | 0.5006835648862354 | 0.46695061831268536 | 0.537017798306875 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_full | 0.6685389083194643 | 0.5005166396039916 | 0.4621958827199002 | 0.5414990169605275 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_single | 0.6591183948868435 | 0.4997343383682671 | 0.45975281005155044 | 0.5370794494078117 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_diff | 0.5389668739344775 | 0.5006234474620015 | 0.46108717634579566 | 0.5409928586067189 | 0.03 | 500 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.7699687634421922 | 0.49884706698406195 | 0.46529893183133614 | 0.5376840243136177 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_full | 0.7428039934148742 | 0.5009820260297142 | 0.4610937074213287 | 0.5362544507027662 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_single | 0.7348563501196989 | 0.5006185694242068 | 0.46942747240620586 | 0.5369796815988074 | 0.0 | 500 |
| primary_with_llm_judge | workspace_compact | 0.6690839153122192 | 0.4987436507811392 | 0.46237790829919534 | 0.534794079692634 | 0.0 | 500 |
| primary_with_llm_judge | workspace_full | 0.7491706660120576 | 0.4998997367300932 | 0.46351116250892394 | 0.5359182692199419 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_full | 0.7605414937245374 | 0.4984737507065948 | 0.4624722710801723 | 0.5358266652553538 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_single | 0.7044440590859646 | 0.5006438424344246 | 0.4685796712391702 | 0.5404273575493602 | 0.0 | 500 |
| primary_with_llm_judge | workspace_noise_single | 0.7044440590859646 | 0.5014985620373352 | 0.4651766993745932 | 0.5365098945794324 | 0.0 | 500 |
| strict | baseline_output_confidence | 0.629963721933523 | 0.5006289069734505 | 0.42130410388818074 | 0.5792313516575699 | 0.0 | 500 |
| strict | combined_compact | 0.737436132082666 | 0.5007465437788019 | 0.4152542188231962 | 0.5891239337189921 | 0.0 | 500 |
| strict | combined_full | 0.8502903334749594 | 0.502698804893726 | 0.4185568301903237 | 0.5869088472726084 | 0.0 | 500 |
| strict | commitment_dynamics_full | 0.7022257084027845 | 0.5007236439302328 | 0.4149720560839298 | 0.5793299452015992 | 0.0 | 500 |
| strict | commitment_dynamics_single | 0.689130742665403 | 0.49890588401913044 | 0.4167878659127801 | 0.5773496312274623 | 0.0 | 500 |
| strict | layer_l33_diff | 0.54848514560251 | 0.49973199986926825 | 0.40312830233900926 | 0.5792852785131439 | 0.124 | 500 |
| strict | layer_l33_diff_in_full | 0.8593544029371072 | 0.49864960617053955 | 0.42572610604525496 | 0.5882744495647722 | 0.0 | 500 |
| strict | layer_l33_full | 0.8349293503720407 | 0.4991434890130841 | 0.4087925286792823 | 0.5786615790219084 | 0.0 | 500 |
| strict | layer_l33_single | 0.8309638199823512 | 0.49989123116645423 | 0.4122806157466418 | 0.5853719318887473 | 0.0 | 500 |
| strict | workspace_compact | 0.7099279885827587 | 0.49950969049253197 | 0.4178337200814895 | 0.576568236537351 | 0.0 | 500 |
| strict | workspace_full | 0.8297000795284941 | 0.4986662744713534 | 0.4184149317471212 | 0.597193897005153 | 0.0 | 500 |
| strict | workspace_late_late_full | 0.8430782974365679 | 0.4985754376790753 | 0.4063976860476517 | 0.5816101251756708 | 0.0 | 500 |
| strict | workspace_late_late_single | 0.7757405410116461 | 0.4963364600015252 | 0.4120665424714841 | 0.5770780904445969 | 0.0 | 500 |
| strict | workspace_noise_single | 0.7757405410116461 | 0.5004563410356135 | 0.42210919371180183 | 0.5827736379383599 | 0.0 | 500 |


## H.3 quadrant analysis

| quadrant | n | accuracy | wrong_rate | mean_confidence | mean_workspace_noise |
| --- | --- | --- | --- | --- | --- |
| high_confidence__clean_workspace | 447 | 0.25727069351230425 | 0.7427293064876958 | 0.8515902118928214 | 1.055952375105465 |
| high_confidence__noisy_workspace | 451 | 0.11086474501108648 | 0.8891352549889135 | 0.8063874386102291 | 2.19833126532986 |
| low_confidence__clean_workspace | 345 | 0.2 | 0.8 | 0.4575785336935002 | 1.0843740404865947 |
| low_confidence__noisy_workspace | 637 | 0.06750392464678179 | 0.9324960753532182 | 0.4370353705361017 | 2.3157439266990876 |


## Conclusion

**supports_H_C_or_no_signal** — Workspace features did not improve prediction over output confidence under the primary label regime in this run. The single-feature `workspace_noise_score` AUC is 0.704 with CI [0.673, 0.734]; CI overlaps baseline upper bound (0.694), so the parsimonious claim is not statistically distinguishable either.

## Artefact guide

See `AGENT_BRIEF.md` for the most useful machine-readable files and selected examples.
