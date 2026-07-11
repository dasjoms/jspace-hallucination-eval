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
  "DATASET_ID": "truthfulqa_gen",
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

- Dataset ID: `truthfulqa_gen`
- Repo: `truthfulqa/truthful_qa`
- Config: `generation`
- Split: `validation`
- Task family: `adversarial_truthfulness_short`
- Prompt template: `short_answer_v1`

```json
{
  "dataset_id": "truthfulqa_gen",
  "repo": "truthfulqa/truthful_qa",
  "config": "generation",
  "split": "validation",
  "task_family": "adversarial_truthfulness_short",
  "answer_format": "sentence",
  "prompt_template_id": "short_answer_v1",
  "max_new_tokens": 32,
  "n_total_in_split": 817,
  "n_requested": 2000,
  "random_seed": 42,
  "expected_failure_mode": "imitative_misconception_hallucination",
  "supports_short_answer": true,
  "supports_multiple_choice": false,
  "allow_prefix_match": true,
  "n_kept_after_dedup": 814,
  "n_selected": 814,
  "examples_with_aliases": 814,
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


## Descriptive statistics

| feature | mean_correct | mean_wrong | std_correct | std_wrong | cohen_d_wrong_minus_correct |
| --- | --- | --- | --- | --- | --- |
| first_content_token_prob | 0.7328800957936507 | 0.6054764531137656 | 0.2107083223808035 | 0.1804727345291236 | -0.6951838423812976 |
| sequence_content_logprob_mean | -0.20575711168166846 | -0.2580952620226509 | 0.0745172190184583 | 0.10354522451603948 | -0.5162652371880136 |
| workspace_noise_score | 1.406224398072809 | 1.682293254182293 | 0.7101637405194803 | 0.6765305822958355 | 0.40629353682044717 |
| late_entropy_topk_mean | 1.4404586315289354 | 1.6116420049334736 | 0.6317148373979192 | 0.5939842756940016 | 0.2865882555547477 |
| late_effective_concepts_topk_mean | 6.574549356701781 | 7.469687182333377 | 4.697174360392695 | 4.340224846961464 | 0.20474375476321047 |
| late_top1_dominance_topk_mean | 0.583256763062225 | 0.5436118559408687 | 0.16372508241649544 | 0.15360871168645085 | -0.2565970520905324 |
| late_top1_margin_mean | 1.5747596153846153 | 1.4370195827232797 | 0.9012163729281856 | 0.813695394127571 | -0.16765473320088786 |
| late_distinct_top1_count | 3.9384615384615387 | 3.8872620790629577 | 1.4348009778899127 | 1.4029290578920175 | -0.036422964415720446 |
| late_top1_churn_rate | 0.4747252747252747 | 0.47061284250156865 | 0.23838809827739718 | 0.22817359928752184 | -0.017952906138772404 |
| late_top5_jaccard_adjacent_mean | 0.49658991801848945 | 0.48620282666507303 | 0.14220194462560423 | 0.1391103210390437 | -0.07452448169448697 |


## Predictive AUC results

| label_regime | feature_set | features | roc_auc | roc_auc_per_fold_std | n_folds_with_both_classes | pr_auc | n_splits | n | n_wrong |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8042831076538941 | 0.12889558320373404 | 5 | 0.9955242726303211 | 5 | 814 | 801 |
| strict | workspace_noise_single | ['workspace_noise_score'] | 0.6816479400749064 | 0.2335790887817275 | 5 | 0.9877723614267003 | 5 | 814 | 801 |
| strict | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.6560069144338807 | 0.15876347396881407 | 5 | 0.9889008419707535 | 5 | 814 | 801 |
| strict | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.5970421588399115 | 0.17530204448243186 | 5 | 0.9851949948621104 | 5 | 814 | 801 |
| strict | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7988091808316529 | 0.10062781466745603 | 5 | 0.9951465448794014 | 5 | 814 | 801 |
| strict | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.707192931912033 | 0.1825523588737792 | 5 | 0.9921201984029604 | 5 | 814 | 801 |
| strict | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.6816479400749064 | 0.2335790887817275 | 5 | 0.9877723614267003 | 5 | 814 | 801 |
| strict | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.6844329203879765 | 0.2474890144303482 | 5 | 0.9877362015203496 | 5 | 814 | 801 |
| strict | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.5858062037837318 | 0.19243875902234475 | 5 | 0.9852772245894885 | 5 | 814 | 801 |
| strict | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.672428694900605 | 0.14578397473970106 | 5 | 0.9901453877382761 | 5 | 814 | 801 |
| strict | layer_l33_single | ['layer_l33_entropy_topk'] | 0.6751176414097763 | 0.2402042038636049 | 5 | 0.9882355941039185 | 5 | 814 | 801 |
| strict | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.676077979448766 | 0.22967970290062895 | 5 | 0.9883983060182737 | 5 | 814 | 801 |
| strict | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5436473638720829 | 0.13099601308645947 | 5 | 0.9882362874071944 | 5 | 814 | 801 |
| strict | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7084413713627197 | 0.18245493071446023 | 5 | 0.9901401967530121 | 5 | 814 | 801 |
| expanded_deterministic | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.6909727700123056 | 0.07548853588285333 | 5 | 0.9760359424095173 | 5 | 814 | 773 |
| expanded_deterministic | workspace_noise_single | ['workspace_noise_score'] | 0.6223771810809958 | 0.09304851683432093 | 5 | 0.962578476140984 | 5 | 814 | 773 |
| expanded_deterministic | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.6116492600889787 | 0.09236728295848279 | 5 | 0.9643741225276358 | 5 | 814 | 773 |
| expanded_deterministic | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.652415359858644 | 0.05134671153459645 | 5 | 0.9723490696866475 | 5 | 814 | 773 |
| expanded_deterministic | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.6954532546619127 | 0.052249855706624056 | 5 | 0.9767280043401362 | 5 | 814 | 773 |
| expanded_deterministic | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7059603066923295 | 0.04243747402844467 | 5 | 0.9776040800275465 | 5 | 814 | 773 |
| expanded_deterministic | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.6223771810809958 | 0.09304851683432093 | 5 | 0.962578476140984 | 5 | 814 | 773 |
| expanded_deterministic | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.6235130785977976 | 0.08452680071507403 | 5 | 0.9609780524792331 | 5 | 814 | 773 |
| expanded_deterministic | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.5848925630265359 | 0.03882242055680472 | 5 | 0.9597930002540365 | 5 | 814 | 773 |
| expanded_deterministic | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.6102609409017764 | 0.09801798470890638 | 5 | 0.9633445331436922 | 5 | 814 | 773 |
| expanded_deterministic | layer_l33_single | ['layer_l33_entropy_topk'] | 0.6183068816457894 | 0.11631439175374586 | 5 | 0.9590288558585633 | 5 | 814 | 773 |
| expanded_deterministic | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.6332313129082131 | 0.13457458198847536 | 5 | 0.9611022076078499 | 5 | 814 | 773 |
| expanded_deterministic | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.42321648313507715 | 0.06792927140662965 | 5 | 0.9404589942453779 | 5 | 814 | 773 |
| expanded_deterministic | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.6229451298393966 | 0.11806993931592324 | 5 | 0.9623269274505521 | 5 | 814 | 773 |
| primary_with_llm_judge | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.7432819011149905 | 0.07739701064875297 | 5 | 0.9640624688990223 | 5 | 748 | 683 |
| primary_with_llm_judge | workspace_noise_single | ['workspace_noise_score'] | 0.6173893456470323 | 0.054387172259492085 | 5 | 0.9305086150992913 | 5 | 748 | 683 |
| primary_with_llm_judge | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.5748169838945828 | 0.08281107974150068 | 5 | 0.929066480606058 | 5 | 748 | 683 |
| primary_with_llm_judge | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.6505687577429891 | 0.07814947274979288 | 5 | 0.9471482537096702 | 5 | 748 | 683 |
| primary_with_llm_judge | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7527874760671247 | 0.09703411458869642 | 5 | 0.9671503997482618 | 5 | 748 | 683 |
| primary_with_llm_judge | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7523820250028156 | 0.09967696574509981 | 5 | 0.968210360597007 | 5 | 748 | 683 |
| primary_with_llm_judge | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.6173893456470323 | 0.054387172259492085 | 5 | 0.9305086150992913 | 5 | 748 | 683 |
| primary_with_llm_judge | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.6666291249014529 | 0.08004787064846931 | 5 | 0.9421037484639477 | 5 | 748 | 683 |
| primary_with_llm_judge | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.5757630363779705 | 0.06499174902290811 | 5 | 0.9224186177363023 | 5 | 748 | 683 |
| primary_with_llm_judge | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.5652438337650637 | 0.06776461769813835 | 5 | 0.9269080687398821 | 5 | 748 | 683 |
| primary_with_llm_judge | layer_l33_single | ['layer_l33_entropy_topk'] | 0.6023426061493411 | 0.05396385192504323 | 5 | 0.9305678321997022 | 5 | 748 | 683 |
| primary_with_llm_judge | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.5795021961932649 | 0.03740730533353752 | 5 | 0.9270368007985241 | 5 | 748 | 683 |
| primary_with_llm_judge | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5813717761009123 | 0.11220732096962391 | 5 | 0.9256500605263892 | 5 | 748 | 683 |
| primary_with_llm_judge | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.6508165333934002 | 0.10505625461258762 | 5 | 0.9416648956728336 | 5 | 748 | 683 |
| high_quality_primary | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.7432819011149905 | 0.07739701064875297 | 5 | 0.9640624688990223 | 5 | 748 | 683 |
| high_quality_primary | workspace_noise_single | ['workspace_noise_score'] | 0.6173893456470323 | 0.054387172259492085 | 5 | 0.9305086150992913 | 5 | 748 | 683 |
| high_quality_primary | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.5748169838945828 | 0.08281107974150068 | 5 | 0.929066480606058 | 5 | 748 | 683 |
| high_quality_primary | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.6505687577429891 | 0.07814947274979288 | 5 | 0.9471482537096702 | 5 | 748 | 683 |
| high_quality_primary | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7527874760671247 | 0.09703411458869642 | 5 | 0.9671503997482618 | 5 | 748 | 683 |
| high_quality_primary | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7523820250028156 | 0.09967696574509981 | 5 | 0.968210360597007 | 5 | 748 | 683 |
| high_quality_primary | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.6173893456470323 | 0.054387172259492085 | 5 | 0.9305086150992913 | 5 | 748 | 683 |
| high_quality_primary | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.6666291249014529 | 0.08004787064846931 | 5 | 0.9421037484639477 | 5 | 748 | 683 |
| high_quality_primary | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.5757630363779705 | 0.06499174902290811 | 5 | 0.9224186177363023 | 5 | 748 | 683 |
| high_quality_primary | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.5652438337650637 | 0.06776461769813835 | 5 | 0.9269080687398821 | 5 | 748 | 683 |
| high_quality_primary | layer_l33_single | ['layer_l33_entropy_topk'] | 0.6023426061493411 | 0.05396385192504323 | 5 | 0.9305678321997022 | 5 | 748 | 683 |
| high_quality_primary | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.5795021961932649 | 0.03740730533353752 | 5 | 0.9270368007985241 | 5 | 748 | 683 |
| high_quality_primary | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5813717761009123 | 0.11220732096962391 | 5 | 0.9256500605263892 | 5 | 748 | 683 |
| high_quality_primary | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.6508165333934002 | 0.10505625461258762 | 5 | 0.9416648956728336 | 5 | 748 | 683 |


## Bootstrap AUC intervals

| label_regime | feature_set | roc_auc | roc_auc_ci_low | roc_auc_ci_high | pr_auc | pr_auc_ci_low | pr_auc_ci_high | bootstrap_n_effective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.6909727700123056 | 0.6131607864722333 | 0.7645956302414565 | 0.9760359424095173 | 0.9637998710836947 | 0.9861452916986012 | 1000 |
| expanded_deterministic | combined_compact | 0.6954532546619127 | 0.6132168943851274 | 0.7689352327901635 | 0.9767280043401362 | 0.9653074459164448 | 0.9865069931458461 | 1000 |
| expanded_deterministic | combined_full | 0.7059603066923295 | 0.6290659479513377 | 0.7765711111145356 | 0.9776040800275465 | 0.9669911842827323 | 0.9869886997423402 | 1000 |
| expanded_deterministic | commitment_dynamics_full | 0.6102609409017764 | 0.5155404041826238 | 0.6972923959354006 | 0.9633445331436922 | 0.9439147476653751 | 0.9784913853540913 | 1000 |
| expanded_deterministic | commitment_dynamics_single | 0.5848925630265359 | 0.4942779034544656 | 0.6748112645193948 | 0.9597930002540365 | 0.9391348661462251 | 0.9773018750733634 | 1000 |
| expanded_deterministic | layer_l33_diff | 0.42321648313507715 | 0.3386729408696549 | 0.5051449420356681 | 0.9404589942453779 | 0.9157606751802752 | 0.9613989072794102 | 1000 |
| expanded_deterministic | layer_l33_diff_in_full | 0.6229451298393966 | 0.5209313246043842 | 0.7248042098276056 | 0.9623269274505521 | 0.94407219819248 | 0.9791162575679915 | 1000 |
| expanded_deterministic | layer_l33_full | 0.6332313129082131 | 0.5204255968529571 | 0.729730348396416 | 0.9611022076078499 | 0.9407802155033043 | 0.9793123273359984 | 1000 |
| expanded_deterministic | layer_l33_single | 0.6183068816457894 | 0.5191235756082538 | 0.7214025185736658 | 0.9590288558585633 | 0.9375376584424167 | 0.9783414758429588 | 1000 |
| expanded_deterministic | workspace_compact | 0.6116492600889787 | 0.5174787511146327 | 0.6943068699253896 | 0.9643741225276358 | 0.9467144954005331 | 0.9782707846781741 | 1000 |
| expanded_deterministic | workspace_full | 0.652415359858644 | 0.5716461221262412 | 0.7208995021128823 | 0.9723490696866475 | 0.9584453519758425 | 0.9833405867969908 | 1000 |
| expanded_deterministic | workspace_late_late_full | 0.6235130785977976 | 0.5265879995514383 | 0.7135014354536556 | 0.9609780524792331 | 0.9395484431822676 | 0.9780217685404894 | 1000 |
| expanded_deterministic | workspace_late_late_single | 0.6223771810809958 | 0.5223396019113343 | 0.7197969279237576 | 0.962578476140984 | 0.9434951764207767 | 0.978379564254131 | 1000 |
| expanded_deterministic | workspace_noise_single | 0.6223771810809958 | 0.5132661759932796 | 0.7213266308556695 | 0.962578476140984 | 0.9441503759869073 | 0.9784059779397687 | 1000 |
| high_quality_primary | baseline_output_confidence | 0.7432819011149905 | 0.6810706284491554 | 0.8064026726364326 | 0.9640624688990223 | 0.9482873359242187 | 0.9782436623284934 | 1000 |
| high_quality_primary | combined_compact | 0.7527874760671247 | 0.6924886422478204 | 0.8065156555370926 | 0.9671503997482618 | 0.9531614608501753 | 0.9795787901409445 | 1000 |
| high_quality_primary | combined_full | 0.7523820250028156 | 0.6903785514696212 | 0.8051687155742051 | 0.968210360597007 | 0.9556517413771087 | 0.9794574827891334 | 1000 |
| high_quality_primary | commitment_dynamics_full | 0.5652438337650637 | 0.4925700258516282 | 0.6389817935357152 | 0.9269080687398821 | 0.9011156394290032 | 0.9522422972271172 | 1000 |
| high_quality_primary | commitment_dynamics_single | 0.5757630363779705 | 0.5010043300973352 | 0.6507171705944822 | 0.9224186177363023 | 0.8942051114487481 | 0.9506742302596217 | 1000 |
| high_quality_primary | layer_l33_diff | 0.5813717761009123 | 0.5110051270181555 | 0.6481613455929696 | 0.9256500605263892 | 0.9003381293033356 | 0.9519698715263732 | 1000 |
| high_quality_primary | layer_l33_diff_in_full | 0.6508165333934002 | 0.5825735910069897 | 0.7245459530808599 | 0.9416648956728336 | 0.9180234785209486 | 0.9650955741318756 | 1000 |
| high_quality_primary | layer_l33_full | 0.5795021961932649 | 0.5017026802439775 | 0.6494954234735255 | 0.9270368007985241 | 0.8982939507488724 | 0.9530414485448179 | 1000 |
| high_quality_primary | layer_l33_single | 0.6023426061493411 | 0.5263985265227467 | 0.6864939187808827 | 0.9305678321997022 | 0.9060304936185697 | 0.9551259545652522 | 1000 |
| high_quality_primary | workspace_compact | 0.5748169838945828 | 0.5021779384325489 | 0.6406331823098483 | 0.929066480606058 | 0.9035873860052693 | 0.9533872454713771 | 1000 |
| high_quality_primary | workspace_full | 0.6505687577429891 | 0.5815113940973167 | 0.7165751187121909 | 0.9471482537096702 | 0.9263077996598352 | 0.9650428655442486 | 1000 |
| high_quality_primary | workspace_late_late_full | 0.6666291249014529 | 0.5918291284971857 | 0.7379611538106667 | 0.9421037484639477 | 0.9180538652112509 | 0.9634817591335891 | 1000 |
| high_quality_primary | workspace_late_late_single | 0.6173893456470323 | 0.5445452973686267 | 0.6922679631143698 | 0.9305086150992913 | 0.9050353089683852 | 0.9565396028915409 | 1000 |
| high_quality_primary | workspace_noise_single | 0.6173893456470323 | 0.5364515473216133 | 0.6965748636047965 | 0.9305086150992913 | 0.9046149775569172 | 0.956373664632319 | 1000 |
| primary_with_llm_judge | baseline_output_confidence | 0.7432819011149905 | 0.6788338129858579 | 0.8027677722375629 | 0.9640624688990223 | 0.9478397912033446 | 0.9777033739986593 | 1000 |
| primary_with_llm_judge | combined_compact | 0.7527874760671247 | 0.6944889204663222 | 0.806766561566459 | 0.9671503997482618 | 0.9514479612688089 | 0.9797154915403619 | 1000 |
| primary_with_llm_judge | combined_full | 0.7523820250028156 | 0.695401597902439 | 0.8092628672334055 | 0.968210360597007 | 0.955878193912577 | 0.9802452581369726 | 1000 |
| primary_with_llm_judge | commitment_dynamics_full | 0.5652438337650637 | 0.49375976739227984 | 0.6371931278239396 | 0.9269080687398821 | 0.9016222857416079 | 0.9513046621010932 | 1000 |
| primary_with_llm_judge | commitment_dynamics_single | 0.5757630363779705 | 0.5011233368987239 | 0.6448121148670888 | 0.9224186177363023 | 0.8943192659501907 | 0.9506648913669455 | 1000 |
| primary_with_llm_judge | layer_l33_diff | 0.5813717761009123 | 0.5085278431428363 | 0.649521240841691 | 0.9256500605263892 | 0.8960339625838422 | 0.9510547542268444 | 1000 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.6508165333934002 | 0.5703448604556322 | 0.7189024073603011 | 0.9416648956728336 | 0.9162723505894121 | 0.96264388395293 | 1000 |
| primary_with_llm_judge | layer_l33_full | 0.5795021961932649 | 0.5057114105280789 | 0.6447403256253396 | 0.9270368007985241 | 0.8997509905835077 | 0.9512268401253222 | 1000 |
| primary_with_llm_judge | layer_l33_single | 0.6023426061493411 | 0.5284176125264739 | 0.6749895915542937 | 0.9305678321997022 | 0.9036802822127483 | 0.955021144288811 | 1000 |
| primary_with_llm_judge | workspace_compact | 0.5748169838945828 | 0.5059680123611019 | 0.6445590285686542 | 0.929066480606058 | 0.9048585487099393 | 0.953253426742813 | 1000 |
| primary_with_llm_judge | workspace_full | 0.6505687577429891 | 0.5760268093613895 | 0.7188007894757948 | 0.9471482537096702 | 0.9261055227973739 | 0.964980213727581 | 1000 |
| primary_with_llm_judge | workspace_late_late_full | 0.6666291249014529 | 0.5854300738631907 | 0.7422363377312614 | 0.9421037484639477 | 0.9193405922242233 | 0.9643475307657148 | 1000 |
| primary_with_llm_judge | workspace_late_late_single | 0.6173893456470323 | 0.542486443969795 | 0.6926726918456666 | 0.9305086150992913 | 0.9027807412600832 | 0.955846022013679 | 1000 |
| primary_with_llm_judge | workspace_noise_single | 0.6173893456470323 | 0.5342688830280254 | 0.6913109105969759 | 0.9305086150992913 | 0.9037132753153815 | 0.9554757984219268 | 1000 |
| strict | baseline_output_confidence | 0.8042831076538941 | 0.6714564700554737 | 0.905478855721393 | 0.9955242726303211 | 0.9906168547172666 | 0.9988076225053545 | 1000 |
| strict | combined_compact | 0.7988091808316529 | 0.6475450101784634 | 0.910710602310231 | 0.9951465448794014 | 0.9892786539091177 | 0.9989975142631785 | 1000 |
| strict | combined_full | 0.707192931912033 | 0.5335442498119587 | 0.879564989207028 | 0.9921201984029604 | 0.9842869781189354 | 0.9979250057371218 | 1000 |
| strict | commitment_dynamics_full | 0.672428694900605 | 0.488118958006219 | 0.840265074356063 | 0.9901453877382761 | 0.9799025686046916 | 0.9976091401638367 | 1000 |
| strict | commitment_dynamics_single | 0.5858062037837318 | 0.40011195958646617 | 0.7750204586876495 | 0.9852772245894885 | 0.9712352788591938 | 0.9963355032785601 | 1000 |
| strict | layer_l33_diff | 0.5436473638720829 | 0.40570734291505434 | 0.6687535378693535 | 0.9882362874071944 | 0.9791974811305494 | 0.995546833840256 | 1000 |
| strict | layer_l33_diff_in_full | 0.7084413713627197 | 0.5339856775472034 | 0.8678997375345309 | 0.9901401967530121 | 0.9786863384926955 | 0.9983154304188973 | 1000 |
| strict | layer_l33_full | 0.676077979448766 | 0.5008524335031127 | 0.840287836157037 | 0.9883983060182737 | 0.9754064590419513 | 0.9978502271023492 | 1000 |
| strict | layer_l33_single | 0.6751176414097763 | 0.48478710280580634 | 0.830846568473688 | 0.9882355941039185 | 0.9754897598528868 | 0.9977685055413709 | 1000 |
| strict | workspace_compact | 0.6560069144338807 | 0.4741009134467203 | 0.816418439716312 | 0.9889008419707535 | 0.9777862761553562 | 0.9970856144118332 | 1000 |
| strict | workspace_full | 0.5970421588399115 | 0.4101872888743598 | 0.7635813383697267 | 0.9851949948621104 | 0.9709385734871978 | 0.9964066677360668 | 1000 |
| strict | workspace_late_late_full | 0.6844329203879765 | 0.47555391749911347 | 0.8726196488370943 | 0.9877362015203496 | 0.9742701183700305 | 0.9979820861264125 | 1000 |
| strict | workspace_late_late_single | 0.6816479400749064 | 0.4890069918833025 | 0.8361947268281327 | 0.9877723614267003 | 0.9727675519285459 | 0.9977221089614732 | 1000 |
| strict | workspace_noise_single | 0.6816479400749064 | 0.487496765010352 | 0.8393728420119447 | 0.9877723614267003 | 0.9749050128100315 | 0.9978403557366475 | 1000 |


## Permutation sanity checks

| label_regime | feature_set | real_roc_auc | perm_auc_mean | perm_auc_ci_low | perm_auc_ci_high | p_perm_ge_real | permutation_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.6909727700123056 | 0.4978387025526141 | 0.4036648471271259 | 0.5896041712681034 | 0.0 | 500 |
| expanded_deterministic | combined_compact | 0.6954532546619127 | 0.4994054838607894 | 0.4049048685829678 | 0.5955455463351528 | 0.0 | 500 |
| expanded_deterministic | combined_full | 0.7059603066923295 | 0.4996549395765627 | 0.3985903827343577 | 0.5907787208531853 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_full | 0.6102609409017764 | 0.5031418294260562 | 0.4134319881361815 | 0.5977621241283564 | 0.016 | 500 |
| expanded_deterministic | commitment_dynamics_single | 0.5848925630265359 | 0.4986554128671946 | 0.40700706780677126 | 0.5886236708421418 | 0.028 | 500 |
| expanded_deterministic | layer_l33_diff | 0.42321648313507715 | 0.501030448363992 | 0.4179369261351087 | 0.5932627078534692 | 0.964 | 500 |
| expanded_deterministic | layer_l33_diff_in_full | 0.6229451298393966 | 0.49905032657053605 | 0.40403795790868646 | 0.5869947622503391 | 0.002 | 500 |
| expanded_deterministic | layer_l33_full | 0.6332313129082131 | 0.502122298299309 | 0.404973495724608 | 0.5901871075631843 | 0.0 | 500 |
| expanded_deterministic | layer_l33_single | 0.6183068816457894 | 0.501102262329221 | 0.4052117186760483 | 0.5933479001672294 | 0.008 | 500 |
| expanded_deterministic | workspace_compact | 0.6116492600889787 | 0.5012762439655445 | 0.4142807560029029 | 0.5924462815132677 | 0.016 | 500 |
| expanded_deterministic | workspace_full | 0.652415359858644 | 0.49933777174770455 | 0.41166819171425867 | 0.5921441643265074 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_full | 0.6235130785977976 | 0.498237339475594 | 0.40585697157100936 | 0.584412961852775 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_single | 0.6223771810809958 | 0.5019569621051968 | 0.41157668885873855 | 0.591202315968826 | 0.008 | 500 |
| expanded_deterministic | workspace_noise_single | 0.6223771810809958 | 0.4990935537815921 | 0.40998091061117603 | 0.5828763449342126 | 0.0 | 500 |
| high_quality_primary | baseline_output_confidence | 0.7432819011149905 | 0.49975510755715735 | 0.43302398918797164 | 0.5743000337875886 | 0.0 | 500 |
| high_quality_primary | combined_compact | 0.7527874760671247 | 0.4995546795810339 | 0.4265733753801103 | 0.5702607275594098 | 0.0 | 500 |
| high_quality_primary | combined_full | 0.7523820250028156 | 0.5002362878702556 | 0.4253857416375718 | 0.5682627548147313 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_full | 0.5652438337650637 | 0.49858578668769005 | 0.42325036603221083 | 0.5759409843450838 | 0.04 | 500 |
| high_quality_primary | commitment_dynamics_single | 0.5757630363779705 | 0.5004382475503999 | 0.4305265232571236 | 0.5746260840184706 | 0.022 | 500 |
| high_quality_primary | layer_l33_diff | 0.5813717761009123 | 0.5017514134474603 | 0.4294470097984007 | 0.5704780943799976 | 0.012 | 500 |
| high_quality_primary | layer_l33_diff_in_full | 0.6508165333934002 | 0.5011350377294741 | 0.4240691519315238 | 0.573289221759207 | 0.0 | 500 |
| high_quality_primary | layer_l33_full | 0.5795021961932649 | 0.4997545669557383 | 0.4201295190899876 | 0.5772671472012614 | 0.024 | 500 |
| high_quality_primary | layer_l33_single | 0.6023426061493411 | 0.5003066561549724 | 0.4341508052708638 | 0.565870593535308 | 0.004 | 500 |
| high_quality_primary | workspace_compact | 0.5748169838945828 | 0.5018726883658069 | 0.42720970830048427 | 0.5760451627435522 | 0.028 | 500 |
| high_quality_primary | workspace_full | 0.6505687577429891 | 0.4976708187858993 | 0.42378195742763825 | 0.5692245748395088 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_full | 0.6666291249014529 | 0.5001669557382589 | 0.4216195517513233 | 0.5808610203851785 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_single | 0.6173893456470323 | 0.503461651086834 | 0.43048992003604003 | 0.5865469084356346 | 0.002 | 500 |
| high_quality_primary | workspace_noise_single | 0.6173893456470323 | 0.49948629350152046 | 0.4306109922288546 | 0.5690961820024777 | 0.0 | 500 |
| primary_with_llm_judge | baseline_output_confidence | 0.7432819011149905 | 0.5010885460074334 | 0.43325656042347116 | 0.5808334271877464 | 0.0 | 500 |
| primary_with_llm_judge | combined_compact | 0.7527874760671247 | 0.5000830273679469 | 0.4291665728122536 | 0.5719844577092015 | 0.0 | 500 |
| primary_with_llm_judge | combined_full | 0.7523820250028156 | 0.5011449938056087 | 0.42912377519990985 | 0.5701103727897285 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_full | 0.5652438337650637 | 0.49891393174907084 | 0.42677553778578675 | 0.5730797387093141 | 0.042 | 500 |
| primary_with_llm_judge | commitment_dynamics_single | 0.5757630363779705 | 0.4998605698839959 | 0.4273842775087284 | 0.5703604009460526 | 0.02 | 500 |
| primary_with_llm_judge | layer_l33_diff | 0.5813717761009123 | 0.5000825768667643 | 0.4215339565266359 | 0.5760840184705485 | 0.016 | 500 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.6508165333934002 | 0.5002926455681946 | 0.4292921500168938 | 0.5849938056087397 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_full | 0.5795021961932649 | 0.49961000112625287 | 0.42871325599729704 | 0.5744706611104854 | 0.014 | 500 |
| primary_with_llm_judge | layer_l33_single | 0.6023426061493411 | 0.5019663475616624 | 0.4281439351278297 | 0.5698062844914968 | 0.0 | 500 |
| primary_with_llm_judge | workspace_compact | 0.5748169838945828 | 0.5025433044261741 | 0.43522581371776103 | 0.5705614370987724 | 0.022 | 500 |
| primary_with_llm_judge | workspace_full | 0.6505687577429891 | 0.5006734542178173 | 0.42903536434283135 | 0.5739278071854939 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_full | 0.6666291249014529 | 0.49989953823628785 | 0.4225582835904944 | 0.5754859781506927 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_single | 0.6173893456470323 | 0.5031253970041671 | 0.4254105192026129 | 0.5787825205541165 | 0.002 | 500 |
| primary_with_llm_judge | workspace_noise_single | 0.6173893456470323 | 0.49686640387431014 | 0.4183044261741187 | 0.5715255096294627 | 0.002 | 500 |
| strict | baseline_output_confidence | 0.8042831076538941 | 0.49662153077883414 | 0.34624027657735523 | 0.6592768654566408 | 0.0 | 500 |
| strict | combined_compact | 0.7988091808316529 | 0.49942783059636986 | 0.35324834341688277 | 0.6391793911456833 | 0.0 | 500 |
| strict | combined_full | 0.707192931912033 | 0.49755747623163354 | 0.3433064438682416 | 0.6484442523768366 | 0.002 | 500 |
| strict | commitment_dynamics_full | 0.672428694900605 | 0.4996880822049361 | 0.33322769614904446 | 0.6529626428502833 | 0.01 | 500 |
| strict | commitment_dynamics_single | 0.5858062037837318 | 0.5029899164505907 | 0.3413473542687026 | 0.6699102083933546 | 0.146 | 500 |
| strict | layer_l33_diff | 0.5436473638720829 | 0.5015432632286565 | 0.34562085854220687 | 0.6457649092480553 | 0.324 | 500 |
| strict | layer_l33_diff_in_full | 0.7084413713627197 | 0.4992505521943724 | 0.33789253817343706 | 0.6470349563046192 | 0.004 | 500 |
| strict | layer_l33_full | 0.676077979448766 | 0.5075225199270144 | 0.3477408047632766 | 0.6563382310573322 | 0.014 | 500 |
| strict | layer_l33_single | 0.6751176414097763 | 0.5006970133486988 | 0.3423052914625948 | 0.6519206760779793 | 0.006 | 500 |
| strict | workspace_compact | 0.6560069144338807 | 0.504058004417555 | 0.35070584845865743 | 0.6479928934985114 | 0.022 | 500 |
| strict | workspace_full | 0.5970421588399115 | 0.49870277537693264 | 0.3564174589455488 | 0.6658383751080379 | 0.116 | 500 |
| strict | workspace_late_late_full | 0.6844329203879765 | 0.49768904254297514 | 0.3405718813022183 | 0.6576995102276001 | 0.014 | 500 |
| strict | workspace_late_late_single | 0.6816479400749064 | 0.5061494285988667 | 0.3371050609814655 | 0.6776625372130988 | 0.024 | 500 |
| strict | workspace_noise_single | 0.6816479400749064 | 0.4960653029866513 | 0.3326082781138961 | 0.6685537309132814 | 0.01 | 500 |


## H.3 quadrant analysis

| quadrant | n | accuracy | wrong_rate | mean_confidence | mean_workspace_noise |
| --- | --- | --- | --- | --- | --- |
| high_confidence__clean_workspace | 166 | 0.15060240963855423 | 0.8493975903614458 | 0.793213659381292 | 1.0465362944846401 |
| high_confidence__noisy_workspace | 190 | 0.08421052631578947 | 0.9157894736842105 | 0.764786002824181 | 2.168702567760882 |
| low_confidence__clean_workspace | 173 | 0.10404624277456648 | 0.8959537572254336 | 0.47084957387061477 | 1.0227399734920832 |
| low_confidence__noisy_workspace | 219 | 0.0273972602739726 | 0.9726027397260274 | 0.46849707787463424 | 2.1812710059730156 |


## Conclusion

**supports_H_B_or_redundant** — Workspace features did not materially improve over output confidence under the primary label regime; signals may be redundant for this model/dataset. The single-feature `workspace_noise_score` AUC is 0.617 with CI [0.534, 0.691]; CI overlaps baseline upper bound (0.803), so the parsimonious claim is not statistically distinguishable either.

## Artefact guide

See `AGENT_BRIEF.md` for the most useful machine-readable files and selected examples.
