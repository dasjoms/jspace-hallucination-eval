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
  "DATASET_ID": "commonsenseqa",
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

- Dataset ID: `commonsenseqa`
- Repo: `tau/commonsense_qa`
- Config: `default`
- Split: `validation`
- Task family: `multiple_choice_commonsense`
- Prompt template: `mc_letter_v1`

```json
{
  "dataset_id": "commonsenseqa",
  "repo": "tau/commonsense_qa",
  "config": "default",
  "split": "validation",
  "task_family": "multiple_choice_commonsense",
  "answer_format": "mc_letter",
  "prompt_template_id": "mc_letter_v1",
  "max_new_tokens": 4,
  "n_total_in_split": 1221,
  "n_requested": 2000,
  "random_seed": 42,
  "expected_failure_mode": "commonsense_choice_ambiguity",
  "supports_short_answer": false,
  "supports_multiple_choice": true,
  "n_kept_after_dedup": 1221,
  "n_selected": 1221,
  "examples_with_aliases": 1221,
  "examples_with_choices": 1221,
  "run_mode": "full",
  "dataset_role": "dev"
}
```

## Aggregate summary

| item | value |
| --- | --- |
| model | Qwen/Qwen3-4B |
| run_mode | full |
| dataset_id | commonsenseqa |
| dataset_role | dev |
| n_processed | 1221 |
| n_primary_included | 1187 |
| accuracy_primary | 0.7287278854254423 |
| wrong_rate_primary | 0.2712721145745577 |
| llm_judge_calls | 87 |
| analysis_status_primary | completed |
| conclusion_status | supports_H_B_or_redundant |
| conclusion | Workspace features did not materially improve over output confidence under the primary label regime; signals may be redundant for this model/dataset. The single-feature `workspace_noise_score` AUC is 0.589 with CI [0.551, 0.624]; CI overlaps baseline upper bound (0.867), so the parsimonious claim is not statistically distinguishable either. |


## Label regimes

| label_regime | n | n_correct | n_wrong | accuracy |
| --- | --- | --- | --- | --- |
| strict | 1221 | 865 | 356 | 0.7084357084357085 |
| expanded_deterministic | 1221 | 865 | 356 | 0.7084357084357085 |
| primary_with_llm_judge | 1187 | 865 | 322 | 0.7287278854254423 |
| high_quality_primary | 1180 | 865 | 315 | 0.7330508474576272 |


## Descriptive statistics

| feature | mean_correct | mean_wrong | std_correct | std_wrong | cohen_d_wrong_minus_correct |
| --- | --- | --- | --- | --- | --- |
| first_content_token_prob | 0.8300331872322656 | 0.5604734012151357 | 0.18155892004258709 | 0.22181590695646242 | -1.3945604058888112 |
| sequence_content_logprob_mean | -0.25994575402381603 | -0.5257463144520669 | 0.16286615780647565 | 0.2848751991526922 | -1.3075473627933587 |
| workspace_noise_score | 1.425119574668392 | 1.603080527355131 | 0.574685949135962 | 0.5205838102800945 | 0.3174776834023659 |
| late_entropy_topk_mean | 1.4200394540867605 | 1.5422028898967302 | 0.48572627938412805 | 0.4610251492757614 | 0.2549528725828117 |
| late_effective_concepts_topk_mean | 6.060347217957035 | 6.792661441619978 | 2.9611049805174807 | 3.122728205972839 | 0.2436381885496957 |
| late_top1_dominance_topk_mean | 0.5973868088452199 | 0.5633308398971184 | 0.13814378129743815 | 0.1283544059527945 | -0.25122097601319426 |
| late_top1_margin_mean | 1.8091040462427745 | 1.5473359860248448 | 0.8951688193248202 | 0.7446702916769334 | -0.30544171164119416 |
| late_distinct_top1_count | 4.034682080924855 | 4.096273291925466 | 1.26058460202272 | 1.2505643933943942 | 0.04896436989531756 |
| late_top1_churn_rate | 0.48587943848059456 | 0.5035492457852705 | 0.21172404256168845 | 0.20581866421750394 | 0.08408558344176432 |
| late_top5_jaccard_adjacent_mean | 0.42307813298729896 | 0.43256080900269006 | 0.10931051962813636 | 0.10497156174820003 | 0.08767887315118482 |


## Predictive AUC results

| label_regime | feature_set | features | roc_auc | roc_auc_per_fold_std | n_folds_with_both_classes | pr_auc | n_splits | n | n_wrong |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.7974410599467427 | 0.033445841686617496 | 5 | 0.6392186827531096 | 5 | 1221 | 356 |
| strict | workspace_noise_single | ['workspace_noise_score'] | 0.5835552380333832 | 0.037687270163962526 | 5 | 0.332553232471428 | 5 | 1221 | 356 |
| strict | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.5529616158992012 | 0.031296754112520836 | 5 | 0.32244202028853247 | 5 | 1221 | 356 |
| strict | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.6001753588361368 | 0.029012231440761257 | 5 | 0.34607103229991726 | 5 | 1221 | 356 |
| strict | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8005065921932845 | 0.0333585320062974 | 5 | 0.6335720154435179 | 5 | 1221 | 356 |
| strict | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7996460349418717 | 0.03671246284390962 | 5 | 0.6376128291082287 | 5 | 1221 | 356 |
| strict | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.5835552380333832 | 0.037687270163962526 | 5 | 0.332553232471428 | 5 | 1221 | 356 |
| strict | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.604101448334091 | 0.029259176066476947 | 5 | 0.3701671423743189 | 5 | 1221 | 356 |
| strict | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.5613106449308306 | 0.043018747931885745 | 5 | 0.32156741313433845 | 5 | 1221 | 356 |
| strict | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.5549490160420861 | 0.03685937309270171 | 5 | 0.3158909965129579 | 5 | 1221 | 356 |
| strict | layer_l33_single | ['layer_l33_entropy_topk'] | 0.5620607910631941 | 0.04024216492670942 | 5 | 0.33072033886422947 | 5 | 1221 | 356 |
| strict | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.5537312463466909 | 0.03076975374272973 | 5 | 0.3246715513340181 | 5 | 1221 | 356 |
| strict | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5713970253945573 | 0.02986038854609833 | 5 | 0.33774262733570165 | 5 | 1221 | 356 |
| strict | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.6136032993440281 | 0.02305459601908895 | 5 | 0.3662129709746106 | 5 | 1221 | 356 |
| expanded_deterministic | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.7974410599467427 | 0.033445841686617496 | 5 | 0.6392186827531096 | 5 | 1221 | 356 |
| expanded_deterministic | workspace_noise_single | ['workspace_noise_score'] | 0.5835552380333832 | 0.037687270163962526 | 5 | 0.332553232471428 | 5 | 1221 | 356 |
| expanded_deterministic | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.5529616158992012 | 0.031296754112520836 | 5 | 0.32244202028853247 | 5 | 1221 | 356 |
| expanded_deterministic | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.6001753588361368 | 0.029012231440761257 | 5 | 0.34607103229991726 | 5 | 1221 | 356 |
| expanded_deterministic | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8005065921932845 | 0.0333585320062974 | 5 | 0.6335720154435179 | 5 | 1221 | 356 |
| expanded_deterministic | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7996460349418717 | 0.03671246284390962 | 5 | 0.6376128291082287 | 5 | 1221 | 356 |
| expanded_deterministic | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.5835552380333832 | 0.037687270163962526 | 5 | 0.332553232471428 | 5 | 1221 | 356 |
| expanded_deterministic | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.604101448334091 | 0.029259176066476947 | 5 | 0.3701671423743189 | 5 | 1221 | 356 |
| expanded_deterministic | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.5613106449308306 | 0.043018747931885745 | 5 | 0.32156741313433845 | 5 | 1221 | 356 |
| expanded_deterministic | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.5549490160420861 | 0.03685937309270171 | 5 | 0.3158909965129579 | 5 | 1221 | 356 |
| expanded_deterministic | layer_l33_single | ['layer_l33_entropy_topk'] | 0.5620607910631941 | 0.04024216492670942 | 5 | 0.33072033886422947 | 5 | 1221 | 356 |
| expanded_deterministic | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.5537312463466909 | 0.03076975374272973 | 5 | 0.3246715513340181 | 5 | 1221 | 356 |
| expanded_deterministic | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5713970253945573 | 0.02986038854609833 | 5 | 0.33774262733570165 | 5 | 1221 | 356 |
| expanded_deterministic | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.6136032993440281 | 0.02305459601908895 | 5 | 0.3662129709746106 | 5 | 1221 | 356 |
| primary_with_llm_judge | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8442429899831257 | 0.03308408143357674 | 5 | 0.6617218507270932 | 5 | 1187 | 322 |
| primary_with_llm_judge | workspace_noise_single | ['workspace_noise_score'] | 0.5885362438516497 | 0.05774272881263058 | 5 | 0.3163657814336839 | 5 | 1187 | 322 |
| primary_with_llm_judge | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.5566868918967436 | 0.03400411080059557 | 5 | 0.31379685268361435 | 5 | 1187 | 322 |
| primary_with_llm_judge | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.6191361792266542 | 0.028564036681752107 | 5 | 0.33563290355946795 | 5 | 1187 | 322 |
| primary_with_llm_judge | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8431587261695329 | 0.034239759890403426 | 5 | 0.6541484295531579 | 5 | 1187 | 322 |
| primary_with_llm_judge | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8443076149786377 | 0.0349770859888913 | 5 | 0.6609330279060958 | 5 | 1187 | 322 |
| primary_with_llm_judge | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.5885362438516497 | 0.05774272881263058 | 5 | 0.3163657814336839 | 5 | 1187 | 322 |
| primary_with_llm_judge | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.631371845043622 | 0.0321524910744553 | 5 | 0.37095964194661857 | 5 | 1187 | 322 |
| primary_with_llm_judge | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.5697662729328977 | 0.04726279374871305 | 5 | 0.30890141246699887 | 5 | 1187 | 322 |
| primary_with_llm_judge | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.561501454062399 | 0.024215709577954714 | 5 | 0.3063379255003483 | 5 | 1187 | 322 |
| primary_with_llm_judge | layer_l33_single | ['layer_l33_entropy_topk'] | 0.5814310846228413 | 0.028909253722584533 | 5 | 0.32433316796997447 | 5 | 1187 | 322 |
| primary_with_llm_judge | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.57363659210857 | 0.029053526809437097 | 5 | 0.31441075874815344 | 5 | 1187 | 322 |
| primary_with_llm_judge | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5796826194664848 | 0.037436472064396244 | 5 | 0.32816361717022347 | 5 | 1187 | 322 |
| primary_with_llm_judge | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.6361146016587081 | 0.04133005202294545 | 5 | 0.3591182850512393 | 5 | 1187 | 322 |
| high_quality_primary | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8467125424350859 | 0.02716716370438189 | 5 | 0.6630699503397063 | 5 | 1180 | 315 |
| high_quality_primary | workspace_noise_single | ['workspace_noise_score'] | 0.5898302596568493 | 0.05174184726555753 | 5 | 0.30984468035065826 | 5 | 1180 | 315 |
| high_quality_primary | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.5628956785026149 | 0.044687774163363954 | 5 | 0.30059024939839885 | 5 | 1180 | 315 |
| high_quality_primary | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.6173997614460043 | 0.0459622727871562 | 5 | 0.3293722125553651 | 5 | 1180 | 315 |
| high_quality_primary | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8451931369850445 | 0.027649580997852273 | 5 | 0.6566704634272106 | 5 | 1180 | 315 |
| high_quality_primary | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8406826314340765 | 0.027553431059341178 | 5 | 0.6560028018834778 | 5 | 1180 | 315 |
| high_quality_primary | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.5898302596568493 | 0.05174184726555753 | 5 | 0.30984468035065826 | 5 | 1180 | 315 |
| high_quality_primary | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.6359592623176439 | 0.040002901950637215 | 5 | 0.3663924699684162 | 5 | 1180 | 315 |
| high_quality_primary | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.5715533535186715 | 0.03230462034751096 | 5 | 0.30359237126488947 | 5 | 1180 | 315 |
| high_quality_primary | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.5655124323332416 | 0.046315926786548035 | 5 | 0.3011361092021928 | 5 | 1180 | 315 |
| high_quality_primary | layer_l33_single | ['layer_l33_entropy_topk'] | 0.5795687677768602 | 0.04760815640309153 | 5 | 0.312368735644059 | 5 | 1180 | 315 |
| high_quality_primary | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.5692228644829801 | 0.04393003795439315 | 5 | 0.3052265621455096 | 5 | 1180 | 315 |
| high_quality_primary | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5848169556840077 | 0.0403646284954563 | 5 | 0.3271207708272694 | 5 | 1180 | 315 |
| high_quality_primary | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.6405431690980825 | 0.03505425071812656 | 5 | 0.35170558125412055 | 5 | 1180 | 315 |


## Bootstrap AUC intervals

| label_regime | feature_set | roc_auc | roc_auc_ci_low | roc_auc_ci_high | pr_auc | pr_auc_ci_low | pr_auc_ci_high | bootstrap_n_effective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.7974410599467427 | 0.7697834257315423 | 0.8214435645909614 | 0.6392186827531096 | 0.5867629313673556 | 0.6946287040216392 | 1000 |
| expanded_deterministic | combined_compact | 0.8005065921932845 | 0.774468818971363 | 0.8275492179130316 | 0.6335720154435179 | 0.5855020938160105 | 0.6859753146091282 | 1000 |
| expanded_deterministic | combined_full | 0.7996460349418717 | 0.7719333821201854 | 0.8289942983883849 | 0.6376128291082287 | 0.5768304907625174 | 0.6948927119600655 | 1000 |
| expanded_deterministic | commitment_dynamics_full | 0.5549490160420861 | 0.5190864192655995 | 0.5877651020637595 | 0.3158909965129579 | 0.2829004879388643 | 0.35807908945526046 | 1000 |
| expanded_deterministic | commitment_dynamics_single | 0.5613106449308306 | 0.5240390256973225 | 0.5963201025131285 | 0.32156741313433845 | 0.2832347119734482 | 0.3613756383294626 | 1000 |
| expanded_deterministic | layer_l33_diff | 0.5713970253945573 | 0.5365725661753079 | 0.6072855265662542 | 0.33774262733570165 | 0.30083260210726626 | 0.38491663829669637 | 1000 |
| expanded_deterministic | layer_l33_diff_in_full | 0.6136032993440281 | 0.5817481102748955 | 0.6477496738023195 | 0.3662129709746106 | 0.32516965031070433 | 0.41639560927555386 | 1000 |
| expanded_deterministic | layer_l33_full | 0.5537312463466909 | 0.5202843774363313 | 0.5870133220637982 | 0.3246715513340181 | 0.2917749850157594 | 0.3688451258657674 | 1000 |
| expanded_deterministic | layer_l33_single | 0.5620607910631941 | 0.5258713015924178 | 0.597055857534315 | 0.33072033886422947 | 0.2918438867563851 | 0.3762672443830056 | 1000 |
| expanded_deterministic | workspace_compact | 0.5529616158992012 | 0.5194716751266371 | 0.5880086538813795 | 0.32244202028853247 | 0.28996771734053767 | 0.364046282409082 | 1000 |
| expanded_deterministic | workspace_full | 0.6001753588361368 | 0.5686430487386226 | 0.6325511355347271 | 0.34607103229991726 | 0.3090351418360999 | 0.38784923869975757 | 1000 |
| expanded_deterministic | workspace_late_late_full | 0.604101448334091 | 0.5686857738909616 | 0.6378591680074608 | 0.3701671423743189 | 0.325113609553832 | 0.421233856587734 | 1000 |
| expanded_deterministic | workspace_late_late_single | 0.5835552380333832 | 0.5473201898298163 | 0.618714919868913 | 0.332553232471428 | 0.29455014853147504 | 0.3738650552373183 | 1000 |
| expanded_deterministic | workspace_noise_single | 0.5835552380333832 | 0.5508063778867802 | 0.6196702504375223 | 0.332553232471428 | 0.29863446112375036 | 0.3754446906958878 | 1000 |
| high_quality_primary | baseline_output_confidence | 0.8467125424350859 | 0.823198663128964 | 0.8701317939038328 | 0.6630699503397063 | 0.6105988508831279 | 0.7211005869173336 | 1000 |
| high_quality_primary | combined_compact | 0.8451931369850445 | 0.8208324200971261 | 0.867686366849547 | 0.6566704634272106 | 0.5990728724667664 | 0.7122250422306566 | 1000 |
| high_quality_primary | combined_full | 0.8406826314340765 | 0.8147495690740761 | 0.8631859591231765 | 0.6560028018834778 | 0.5958888752457493 | 0.7148297674108577 | 1000 |
| high_quality_primary | commitment_dynamics_full | 0.5655124323332416 | 0.5300265580533667 | 0.6020055559547847 | 0.3011361092021928 | 0.2645946899179265 | 0.3445677254109763 | 1000 |
| high_quality_primary | commitment_dynamics_single | 0.5715533535186715 | 0.5384891678265419 | 0.6054051023468818 | 0.30359237126488947 | 0.268603793302348 | 0.34694331445022086 | 1000 |
| high_quality_primary | layer_l33_diff | 0.5848169556840077 | 0.5485782232272818 | 0.6205664713119836 | 0.3271207708272694 | 0.2895404167658484 | 0.37758094774199663 | 1000 |
| high_quality_primary | layer_l33_diff_in_full | 0.6405431690980825 | 0.6085477154541894 | 0.6737958337014059 | 0.35170558125412055 | 0.31292862371748914 | 0.40026493388714735 | 1000 |
| high_quality_primary | layer_l33_full | 0.5692228644829801 | 0.5336853861579048 | 0.6054806390471981 | 0.3052265621455096 | 0.2684495611282405 | 0.3504513619896402 | 1000 |
| high_quality_primary | layer_l33_single | 0.5795687677768602 | 0.5414614130738034 | 0.6143993076452468 | 0.312368735644059 | 0.2779503562616397 | 0.35755684445899144 | 1000 |
| high_quality_primary | workspace_compact | 0.5628956785026149 | 0.5254324865444545 | 0.6008707852864498 | 0.30059024939839885 | 0.26740900130813394 | 0.3425562174827079 | 1000 |
| high_quality_primary | workspace_full | 0.6173997614460043 | 0.583657814431333 | 0.6522252333876932 | 0.3293722125553651 | 0.2896218394302045 | 0.3772212023166932 | 1000 |
| high_quality_primary | workspace_late_late_full | 0.6359592623176439 | 0.6026276741801966 | 0.6694237095196169 | 0.3663924699684162 | 0.32253496043872 | 0.4207951497637387 | 1000 |
| high_quality_primary | workspace_late_late_single | 0.5898302596568493 | 0.5551182003372236 | 0.626079423283674 | 0.30984468035065826 | 0.27416305334319574 | 0.356623731157135 | 1000 |
| high_quality_primary | workspace_noise_single | 0.5898302596568493 | 0.554445539652055 | 0.6270805281792584 | 0.30984468035065826 | 0.2737286672238492 | 0.35785237597256586 | 1000 |
| primary_with_llm_judge | baseline_output_confidence | 0.8442429899831257 | 0.821607561939543 | 0.8674111586232826 | 0.6617218507270932 | 0.6082032743234767 | 0.7200910796900725 | 1000 |
| primary_with_llm_judge | combined_compact | 0.8431587261695329 | 0.8192059068240942 | 0.8674223131068131 | 0.6541484295531579 | 0.5998094300382663 | 0.7115457077091566 | 1000 |
| primary_with_llm_judge | combined_full | 0.8443076149786377 | 0.8211801274902668 | 0.8683306849093316 | 0.6609330279060958 | 0.6054518145884714 | 0.7177684089481118 | 1000 |
| primary_with_llm_judge | commitment_dynamics_full | 0.561501454062399 | 0.526168753616509 | 0.5955579604020326 | 0.3063379255003483 | 0.2734605896859102 | 0.3491562669385555 | 1000 |
| primary_with_llm_judge | commitment_dynamics_single | 0.5697662729328977 | 0.5355358770500357 | 0.6048352985305692 | 0.30890141246699887 | 0.27438654117630795 | 0.35201404024548233 | 1000 |
| primary_with_llm_judge | layer_l33_diff | 0.5796826194664848 | 0.5418025532325218 | 0.614268277850913 | 0.32816361717022347 | 0.286061776969668 | 0.37215194290118664 | 1000 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.6361146016587081 | 0.6027181917121848 | 0.6683159430482081 | 0.3591182850512393 | 0.3190094110523877 | 0.40736541994387915 | 1000 |
| primary_with_llm_judge | layer_l33_full | 0.57363659210857 | 0.5359416442294666 | 0.6086275610698729 | 0.31441075874815344 | 0.2793798830745394 | 0.36174076168174046 | 1000 |
| primary_with_llm_judge | layer_l33_single | 0.5814310846228413 | 0.5445417867763709 | 0.6165107339622613 | 0.32433316796997447 | 0.2858480118439053 | 0.3724282715267066 | 1000 |
| primary_with_llm_judge | workspace_compact | 0.5566868918967436 | 0.5203341335566883 | 0.5928098933822998 | 0.31379685268361435 | 0.27252602973024864 | 0.3616899379049905 | 1000 |
| primary_with_llm_judge | workspace_full | 0.6191361792266542 | 0.5837510337060845 | 0.6520746949141183 | 0.33563290355946795 | 0.29579984352197514 | 0.3841156758933077 | 1000 |
| primary_with_llm_judge | workspace_late_late_full | 0.631371845043622 | 0.5916820252044215 | 0.6638437815369304 | 0.37095964194661857 | 0.32470522543245844 | 0.42233096499403855 | 1000 |
| primary_with_llm_judge | workspace_late_late_single | 0.5885362438516497 | 0.5529090149528518 | 0.6226477579937649 | 0.3163657814336839 | 0.2795779273410406 | 0.36266888825686633 | 1000 |
| primary_with_llm_judge | workspace_noise_single | 0.5885362438516497 | 0.5514317551386401 | 0.624391226792898 | 0.3163657814336839 | 0.280786789332471 | 0.3628755707442429 | 1000 |
| strict | baseline_output_confidence | 0.7974410599467427 | 0.7696006855621543 | 0.8247716187105583 | 0.6392186827531096 | 0.5872257241312719 | 0.6945327702425316 | 1000 |
| strict | combined_compact | 0.8005065921932845 | 0.7733030215851866 | 0.8272631328822693 | 0.6335720154435179 | 0.5800507651601928 | 0.690723974074941 | 1000 |
| strict | combined_full | 0.7996460349418717 | 0.7739479947549578 | 0.8252326304959934 | 0.6376128291082287 | 0.5866796900869357 | 0.6907360383362279 | 1000 |
| strict | commitment_dynamics_full | 0.5549490160420861 | 0.5171522605445977 | 0.5882742374658343 | 0.3158909965129579 | 0.2843962193075359 | 0.35683922520378697 | 1000 |
| strict | commitment_dynamics_single | 0.5613106449308306 | 0.5279888715248562 | 0.5951795418220605 | 0.32156741313433845 | 0.2894993158370529 | 0.362171393641184 | 1000 |
| strict | layer_l33_diff | 0.5713970253945573 | 0.5339259653433959 | 0.6060264043256027 | 0.33774262733570165 | 0.30014819741070653 | 0.3853991661468544 | 1000 |
| strict | layer_l33_diff_in_full | 0.6136032993440281 | 0.581452224067656 | 0.6467701027430335 | 0.3662129709746106 | 0.3264748402397262 | 0.41358249950959464 | 1000 |
| strict | layer_l33_full | 0.5537312463466909 | 0.5193489888628371 | 0.5903666407735656 | 0.3246715513340181 | 0.2875088235130134 | 0.3688059430812083 | 1000 |
| strict | layer_l33_single | 0.5620607910631941 | 0.5273994511733752 | 0.5990163872145171 | 0.33072033886422947 | 0.2945277514979391 | 0.3758454624620953 | 1000 |
| strict | workspace_compact | 0.5529616158992012 | 0.5193429980008041 | 0.5874019240968663 | 0.32244202028853247 | 0.2876556339279003 | 0.3662479555704293 | 1000 |
| strict | workspace_full | 0.6001753588361368 | 0.5655319759411149 | 0.6307842932481724 | 0.34607103229991726 | 0.3092007865871363 | 0.3916535412897668 | 1000 |
| strict | workspace_late_late_full | 0.604101448334091 | 0.5691697820360594 | 0.6372526681582353 | 0.3701671423743189 | 0.327190042601808 | 0.4216556265521669 | 1000 |
| strict | workspace_late_late_single | 0.5835552380333832 | 0.5500357156713448 | 0.6211062745910177 | 0.332553232471428 | 0.2992778181378752 | 0.3772982938455282 | 1000 |
| strict | workspace_noise_single | 0.5835552380333832 | 0.5489787350421711 | 0.6188202372786922 | 0.332553232471428 | 0.29875553526551135 | 0.3776264253609919 | 1000 |


## Permutation sanity checks

| label_regime | feature_set | real_roc_auc | perm_auc_mean | perm_auc_ci_low | perm_auc_ci_high | p_perm_ge_real | permutation_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.7974410599467427 | 0.4992804247580697 | 0.4655480775475742 | 0.5336260310450087 | 0.0 | 500 |
| expanded_deterministic | combined_compact | 0.8005065921932845 | 0.4978486328505553 | 0.4636187244268364 | 0.5333556861726311 | 0.0 | 500 |
| expanded_deterministic | combined_full | 0.7996460349418717 | 0.5002166525946612 | 0.46268152886926023 | 0.5357490907319608 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_full | 0.5549490160420861 | 0.5016235760213028 | 0.46726172306293434 | 0.539253994284601 | 0.002 | 500 |
| expanded_deterministic | commitment_dynamics_single | 0.5613106449308306 | 0.5001588945898552 | 0.4643297395596545 | 0.5370554328765343 | 0.0 | 500 |
| expanded_deterministic | layer_l33_diff | 0.5713970253945573 | 0.49967879457037084 | 0.46345188997856723 | 0.5352493180489706 | 0.0 | 500 |
| expanded_deterministic | layer_l33_diff_in_full | 0.6136032993440281 | 0.4994875690069494 | 0.46398040202636875 | 0.5348166850685199 | 0.0 | 500 |
| expanded_deterministic | layer_l33_full | 0.5537312463466909 | 0.5005118269792816 | 0.4681568649736962 | 0.535508297070858 | 0.0 | 500 |
| expanded_deterministic | layer_l33_single | 0.5620607910631941 | 0.49904517113723457 | 0.46366978956939664 | 0.5369247255958953 | 0.0 | 500 |
| expanded_deterministic | workspace_compact | 0.5529616158992012 | 0.4998723127882055 | 0.46238025264661947 | 0.5372475969344678 | 0.002 | 500 |
| expanded_deterministic | workspace_full | 0.6001753588361368 | 0.5009781450932 | 0.46719563876079756 | 0.536128547769046 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_full | 0.604101448334091 | 0.5014927778138598 | 0.4677371403520167 | 0.5365073553289602 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_single | 0.5835552380333832 | 0.4999312918100929 | 0.46486515230239656 | 0.5340642657660583 | 0.0 | 500 |
| expanded_deterministic | workspace_noise_single | 0.5835552380333832 | 0.5011856140806651 | 0.46474597324154054 | 0.5343915210755341 | 0.0 | 500 |
| high_quality_primary | baseline_output_confidence | 0.8467125424350859 | 0.49997396458390686 | 0.4622392880080741 | 0.5360389944031563 | 0.0 | 500 |
| high_quality_primary | combined_compact | 0.8451931369850445 | 0.4995813634278374 | 0.4609130195430774 | 0.5373931553353518 | 0.0 | 500 |
| high_quality_primary | combined_full | 0.8406826314340765 | 0.5009620038535646 | 0.4645595008716396 | 0.5379883475548215 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_full | 0.5655124323332416 | 0.5004728213597578 | 0.4651475364712359 | 0.5381146894210479 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_single | 0.5715533535186715 | 0.5002777649325627 | 0.4646002385539958 | 0.5389589870630332 | 0.0 | 500 |
| high_quality_primary | layer_l33_diff | 0.5848169556840077 | 0.5008114359115515 | 0.46067529131112944 | 0.537552436003303 | 0.0 | 500 |
| high_quality_primary | layer_l33_diff_in_full | 0.6405431690980825 | 0.4997020644095788 | 0.46378227360308283 | 0.5389768786127168 | 0.0 | 500 |
| high_quality_primary | layer_l33_full | 0.5692228644829801 | 0.49914842095605105 | 0.463504816955684 | 0.5361002844297642 | 0.0 | 500 |
| high_quality_primary | layer_l33_single | 0.5795687677768602 | 0.49919354069180655 | 0.46159390769795394 | 0.5352191944215066 | 0.0 | 500 |
| high_quality_primary | workspace_compact | 0.5628956785026149 | 0.5014514726121663 | 0.46529699972474536 | 0.5358884301312047 | 0.004 | 500 |
| high_quality_primary | workspace_full | 0.6173997614460043 | 0.5012654592164418 | 0.46759721075328015 | 0.5363325993210386 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_full | 0.6359592623176439 | 0.49871724745389484 | 0.4643457197908065 | 0.5305295898706304 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_single | 0.5898302596568493 | 0.501443604000367 | 0.4597822736030828 | 0.5380999174236168 | 0.0 | 500 |
| high_quality_primary | workspace_noise_single | 0.5898302596568493 | 0.5004804257271309 | 0.4657624552711258 | 0.5368733828791632 | 0.0 | 500 |
| primary_with_llm_judge | baseline_output_confidence | 0.8442429899831257 | 0.5013934513337881 | 0.46601012458263025 | 0.5363682547660934 | 0.0 | 500 |
| primary_with_llm_judge | combined_compact | 0.8431587261695329 | 0.49909060424370794 | 0.45996194305819843 | 0.5369923347574768 | 0.0 | 500 |
| primary_with_llm_judge | combined_full | 0.8443076149786377 | 0.5015449682260439 | 0.46093535705310024 | 0.5385735827379455 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_full | 0.561501454062399 | 0.5017545040031595 | 0.46716439880802785 | 0.5400493663160163 | 0.002 | 500 |
| primary_with_llm_judge | commitment_dynamics_single | 0.5697662729328977 | 0.4995665816967652 | 0.46141896743618277 | 0.5357769360571571 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_diff | 0.5796826194664848 | 0.5000205579291279 | 0.46770347897892506 | 0.5342028686317453 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.6361146016587081 | 0.5004450077190967 | 0.4643287078591175 | 0.5353498725451478 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_full | 0.57363659210857 | 0.5002722076616523 | 0.4610700822173554 | 0.5378860445912469 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_single | 0.5814310846228413 | 0.5003092952285212 | 0.4642191146375615 | 0.5356421211359638 | 0.0 | 500 |
| primary_with_llm_judge | workspace_compact | 0.5566868918967436 | 0.5000865113273256 | 0.46271766057516245 | 0.5371115319714214 | 0.002 | 500 |
| primary_with_llm_judge | workspace_full | 0.6191361792266542 | 0.4991937672782106 | 0.46371171866585287 | 0.5359571679890855 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_full | 0.631371845043622 | 0.4983859763759738 | 0.4639280328869422 | 0.5323983053890066 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_single | 0.5885362438516497 | 0.5012609198291028 | 0.46504272430258864 | 0.5365752342656087 | 0.0 | 500 |
| primary_with_llm_judge | workspace_noise_single | 0.5885362438516497 | 0.5000163860266399 | 0.4644458406634833 | 0.5378206117832909 | 0.0 | 500 |
| strict | baseline_output_confidence | 0.7974410599467427 | 0.49930754042995384 | 0.4658740339027083 | 0.5345855523803338 | 0.0 | 500 |
| strict | combined_compact | 0.8005065921932845 | 0.5008443722803143 | 0.4650049522634279 | 0.5375707930116257 | 0.0 | 500 |
| strict | combined_full | 0.7996460349418717 | 0.5000886081704228 | 0.462887088393843 | 0.5345636325258167 | 0.0 | 500 |
| strict | commitment_dynamics_full | 0.5549490160420861 | 0.5003189257647594 | 0.4678907417029291 | 0.537586218094434 | 0.004 | 500 |
| strict | commitment_dynamics_single | 0.5613106449308306 | 0.4996594596349938 | 0.4649103721504189 | 0.531768688705592 | 0.0 | 500 |
| strict | layer_l33_diff | 0.5713970253945573 | 0.4992322465415341 | 0.46480913489640835 | 0.5338251769825291 | 0.0 | 500 |
| strict | layer_l33_diff_in_full | 0.6136032993440281 | 0.5001115736831852 | 0.46338759173865035 | 0.5355631778917971 | 0.0 | 500 |
| strict | layer_l33_full | 0.5537312463466909 | 0.5015191465869975 | 0.4646986425927129 | 0.5384630122751185 | 0.006 | 500 |
| strict | layer_l33_single | 0.5620607910631941 | 0.4999921932844061 | 0.4656779729817497 | 0.5333309248554913 | 0.0 | 500 |
| strict | workspace_compact | 0.5529616158992012 | 0.4998698123010976 | 0.46319388517243615 | 0.536577498863415 | 0.004 | 500 |
| strict | workspace_full | 0.6001753588361368 | 0.49919255049685 | 0.46351951678898484 | 0.5371989673312982 | 0.0 | 500 |
| strict | workspace_late_late_full | 0.604101448334091 | 0.5001950899525881 | 0.4647879457037085 | 0.5357255471845165 | 0.0 | 500 |
| strict | workspace_late_late_single | 0.5835552380333832 | 0.500339540170163 | 0.4665711664609989 | 0.5325289829187504 | 0.0 | 500 |
| strict | workspace_noise_single | 0.5835552380333832 | 0.4993799831135936 | 0.46222795025004876 | 0.5351161752289407 | 0.0 | 500 |


## H.3 quadrant analysis

| quadrant | n | accuracy | wrong_rate | mean_confidence | mean_workspace_noise |
| --- | --- | --- | --- | --- | --- |
| high_confidence__clean_workspace | 532 | 0.868421052631579 | 0.13157894736842105 | 0.8954570262055648 | 1.0472307459691093 |
| high_confidence__noisy_workspace | 322 | 0.8478260869565217 | 0.15217391304347827 | 0.8609368838138461 | 1.989562034077063 |
| low_confidence__clean_workspace | 148 | 0.4189189189189189 | 0.581081081081081 | 0.4418466011616024 | 1.1620015115766609 |
| low_confidence__noisy_workspace | 185 | 0.3675675675675676 | 0.6324324324324324 | 0.42947584132890443 | 2.049613007323162 |


## Conclusion

**supports_H_B_or_redundant** — Workspace features did not materially improve over output confidence under the primary label regime; signals may be redundant for this model/dataset. The single-feature `workspace_noise_score` AUC is 0.589 with CI [0.551, 0.624]; CI overlaps baseline upper bound (0.867), so the parsimonious claim is not statistically distinguishable either.

## Artefact guide

See `AGENT_BRIEF.md` for the most useful machine-readable files and selected examples.
