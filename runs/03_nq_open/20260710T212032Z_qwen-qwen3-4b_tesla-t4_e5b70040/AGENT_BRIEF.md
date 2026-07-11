# Agent Brief — Hallucination Detection via J-Space

## Run metadata

- Run ID: `20260710T212032Z_qwen-qwen3-4b_tesla-t4_e5b70040`
- Experiment: `01_hallucination_detection` — Hallucination Detection via J-Space State
- Dataset ID: `nq_open` (role: `dev`)
- Dataset repo: `google-research-datasets/nq_open` (config `nq_open`, split `validation`)
- Model: `Qwen/Qwen3-4B`
- dtype: `torch.bfloat16`
- Lens: `qwen3-4b/jlens/Salesforce-wikitext/Qwen3-4B_jacobian_lens.pt`
- GPU: `Tesla T4`
- Run mode: `full`
- Examples processed: `2000`

## Main conclusion

**supports_H_C_or_no_signal** — Workspace features did not improve prediction over output confidence under the primary label regime in this run. The single-feature `workspace_noise_score` AUC is 0.718 with CI [0.691, 0.746]; CI overlaps baseline upper bound (0.747), so the parsimonious claim is not statistically distinguishable either.

## Summary table

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


## AUC table

| label_regime | feature_set | features | roc_auc | roc_auc_per_fold_std | n_folds_with_both_classes | pr_auc | n_splits | n | n_wrong |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.646445455089462 | 0.07244527748275226 | 5 | 0.99107322409682 | 5 | 2000 | 1966 |
| strict | workspace_noise_single | ['workspace_noise_score'] | 0.7094279217282029 | 0.06493558476873998 | 5 | 0.9920816255916434 | 5 | 2000 | 1966 |
| strict | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7067799652923223 | 0.09052166711670359 | 5 | 0.9927414604536291 | 5 | 2000 | 1966 |
| strict | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.717521393094369 | 0.09860482816764736 | 5 | 0.9922036588016219 | 5 | 2000 | 1966 |
| strict | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7152923224223566 | 0.0702322523748229 | 5 | 0.9931239477479344 | 5 | 2000 | 1966 |
| strict | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7239991622284723 | 0.08293344235460316 | 5 | 0.9925530185787536 | 5 | 2000 | 1966 |
| strict | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7094279217282029 | 0.06493558476873998 | 5 | 0.9920816255916434 | 5 | 2000 | 1966 |
| strict | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.6890970019747472 | 0.12205225390358435 | 5 | 0.9904911623218556 | 5 | 2000 | 1966 |
| strict | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.6693345700436839 | 0.0686640887498727 | 5 | 0.9898176133284069 | 5 | 2000 | 1966 |
| strict | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.714170306983424 | 0.071762987369538 | 5 | 0.9929476783248813 | 5 | 2000 | 1966 |
| strict | layer_l33_single | ['layer_l33_entropy_topk'] | 0.689366285680091 | 0.08484513473519477 | 5 | 0.9907186663180835 | 5 | 2000 | 1966 |
| strict | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.6508736760217821 | 0.10249375551431418 | 5 | 0.9891247121642679 | 5 | 2000 | 1966 |
| strict | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.509754054215786 | 0.07191988374361576 | 5 | 0.9846444457787552 | 5 | 2000 | 1966 |
| strict | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.6944228352582131 | 0.08467644438795094 | 5 | 0.9921404578255483 | 5 | 2000 | 1966 |
| expanded_deterministic | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.6580084054368901 | 0.03293140307284805 | 5 | 0.9092826737815887 | 5 | 2000 | 1697 |
| expanded_deterministic | workspace_noise_single | ['workspace_noise_score'] | 0.6914084454998239 | 0.02182372465502416 | 5 | 0.9247001025690713 | 5 | 2000 | 1697 |
| expanded_deterministic | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.6983669492464862 | 0.017199784799656403 | 5 | 0.9267644715761387 | 5 | 2000 | 1697 |
| expanded_deterministic | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.6996038437078829 | 0.005498989116798258 | 5 | 0.9276386068417477 | 5 | 2000 | 1697 |
| expanded_deterministic | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7231145624874804 | 0.00969247312863301 | 5 | 0.9319264580743852 | 5 | 2000 | 1697 |
| expanded_deterministic | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7219671289462477 | 0.014333163942111742 | 5 | 0.9318428558952134 | 5 | 2000 | 1697 |
| expanded_deterministic | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.6914084454998239 | 0.02182372465502416 | 5 | 0.9247001025690713 | 5 | 2000 | 1697 |
| expanded_deterministic | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.6972720253757845 | 0.019991240821404865 | 5 | 0.9263405387553648 | 5 | 2000 | 1697 |
| expanded_deterministic | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.6632574276873769 | 0.0220764088479041 | 5 | 0.9172007397776848 | 5 | 2000 | 1697 |
| expanded_deterministic | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.6689226376968869 | 0.024283232975754156 | 5 | 0.9174799118106567 | 5 | 2000 | 1697 |
| expanded_deterministic | layer_l33_single | ['layer_l33_entropy_topk'] | 0.667781038563491 | 0.006448759035026377 | 5 | 0.91753483882971 | 5 | 2000 | 1697 |
| expanded_deterministic | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.6774408731385808 | 0.017326893773267352 | 5 | 0.919947011879003 | 5 | 2000 | 1697 |
| expanded_deterministic | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5155943997463976 | 0.028803492759480628 | 5 | 0.8543839282879893 | 5 | 2000 | 1697 |
| expanded_deterministic | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.680447537977133 | 0.021012824345557114 | 5 | 0.9233637410263237 | 5 | 2000 | 1697 |
| primary_with_llm_judge | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.7179196421492434 | 0.048184147676687814 | 5 | 0.8973080934511599 | 5 | 1810 | 1431 |
| primary_with_llm_judge | workspace_noise_single | ['workspace_noise_score'] | 0.7184561970244252 | 0.02429043754578908 | 5 | 0.9064681970245131 | 5 | 1810 | 1431 |
| primary_with_llm_judge | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7226398499858947 | 0.01688148147074487 | 5 | 0.9051312386649923 | 5 | 1810 | 1431 |
| primary_with_llm_judge | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7368023173270348 | 0.01580362793305394 | 5 | 0.9132799632959064 | 5 | 1810 | 1431 |
| primary_with_llm_judge | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.765743091625503 | 0.024656205114258294 | 5 | 0.9215869170179718 | 5 | 1810 | 1431 |
| primary_with_llm_judge | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7671296526775195 | 0.024692636015110056 | 5 | 0.9238095470507757 | 5 | 1810 | 1431 |
| primary_with_llm_judge | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7184561970244252 | 0.02429043754578908 | 5 | 0.9064681970245131 | 5 | 1810 | 1431 |
| primary_with_llm_judge | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7276347886692887 | 0.023670368812836212 | 5 | 0.9101753168107578 | 5 | 1810 | 1431 |
| primary_with_llm_judge | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.694128688353809 | 0.013900760897794065 | 5 | 0.895485530044081 | 5 | 1810 | 1431 |
| primary_with_llm_judge | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.6989152741131633 | 0.010480819826079634 | 5 | 0.8984095985890388 | 5 | 1810 | 1431 |
| primary_with_llm_judge | layer_l33_single | ['layer_l33_entropy_topk'] | 0.6898583753265886 | 0.017419715700763283 | 5 | 0.8940312306823937 | 5 | 1810 | 1431 |
| primary_with_llm_judge | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.6973848942286239 | 0.021054133550140432 | 5 | 0.8965931545139285 | 5 | 1810 | 1431 |
| primary_with_llm_judge | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.541820857049612 | 0.030465539543147267 | 5 | 0.8178770150182377 | 5 | 1810 | 1431 |
| primary_with_llm_judge | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7246957217584988 | 0.022423764882653578 | 5 | 0.9096670048794716 | 5 | 1810 | 1431 |
| high_quality_primary | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.7193798363672645 | 0.043017775209947165 | 5 | 0.8976840053927779 | 5 | 1807 | 1428 |
| high_quality_primary | workspace_noise_single | ['workspace_noise_score'] | 0.7186444498643785 | 0.027373038023656412 | 5 | 0.9064687146948964 | 5 | 1807 | 1428 |
| high_quality_primary | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.72250430515214 | 0.016784733515020422 | 5 | 0.9051173076005066 | 5 | 1807 | 1428 |
| high_quality_primary | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7344996045911768 | 0.022131451217746647 | 5 | 0.9125262215685824 | 5 | 1807 | 1428 |
| high_quality_primary | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.7674571147720303 | 0.026922874028795778 | 5 | 0.9219223753474651 | 5 | 1807 | 1428 |
| high_quality_primary | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.7667161851548006 | 0.023809802439296122 | 5 | 0.9235396558891489 | 5 | 1807 | 1428 |
| high_quality_primary | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.7186444498643785 | 0.027373038023656412 | 5 | 0.9064687146948964 | 5 | 1807 | 1428 |
| high_quality_primary | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.7276575537866863 | 0.030054505524932367 | 5 | 0.9100393378668721 | 5 | 1807 | 1428 |
| high_quality_primary | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.6946483078719614 | 0.018136351378190342 | 5 | 0.8955293741492665 | 5 | 1807 | 1428 |
| high_quality_primary | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.6992306157291412 | 0.014127406336970993 | 5 | 0.8986093046486002 | 5 | 1807 | 1428 |
| high_quality_primary | layer_l33_single | ['layer_l33_entropy_topk'] | 0.6900770862434684 | 0.020490799377531028 | 5 | 0.8938765297258443 | 5 | 1807 | 1428 |
| high_quality_primary | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.6959657213809005 | 0.03091105081894105 | 5 | 0.8962465216308109 | 5 | 1807 | 1428 |
| high_quality_primary | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5427669748638242 | 0.02890128109369545 | 5 | 0.8177548698297812 | 5 | 1807 | 1428 |
| high_quality_primary | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.7241801733886166 | 0.03345085540472043 | 5 | 0.9093917530708939 | 5 | 1807 | 1428 |


## Bootstrap AUC intervals

| label_regime | feature_set | roc_auc | roc_auc_ci_low | roc_auc_ci_high | pr_auc | pr_auc_ci_low | pr_auc_ci_high | bootstrap_n_effective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.6580084054368901 | 0.6266382236078686 | 0.6912026913779693 | 0.9092826737815887 | 0.8922661827503104 | 0.925683638119923 | 1000 |
| expanded_deterministic | combined_compact | 0.7231145624874804 | 0.6932136164604276 | 0.7521934638626695 | 0.9319264580743852 | 0.9187588030654096 | 0.9449385615587922 | 1000 |
| expanded_deterministic | combined_full | 0.7219671289462477 | 0.6916886050726057 | 0.7508880259314356 | 0.9318428558952134 | 0.9183123139417281 | 0.9441199589306564 | 1000 |
| expanded_deterministic | commitment_dynamics_full | 0.6689226376968869 | 0.6393271368370472 | 0.6994238435395199 | 0.9174799118106567 | 0.9036735740930153 | 0.9315620562615524 | 1000 |
| expanded_deterministic | commitment_dynamics_single | 0.6632574276873769 | 0.6318844910338837 | 0.6947190312785286 | 0.9172007397776848 | 0.9030557022240269 | 0.9318975870495051 | 1000 |
| expanded_deterministic | layer_l33_diff | 0.5155943997463976 | 0.47999435981060834 | 0.5511044717148037 | 0.8543839282879893 | 0.8326039101372267 | 0.8762147034715836 | 1000 |
| expanded_deterministic | layer_l33_diff_in_full | 0.680447537977133 | 0.6468291245512295 | 0.7107588922966507 | 0.9233637410263237 | 0.9108908887982103 | 0.9353154933953315 | 1000 |
| expanded_deterministic | layer_l33_full | 0.6774408731385808 | 0.6450228190873266 | 0.7087200886292017 | 0.919947011879003 | 0.9056224939849408 | 0.9321431146732934 | 1000 |
| expanded_deterministic | layer_l33_single | 0.667781038563491 | 0.6331342159147021 | 0.6995180771670834 | 0.91753483882971 | 0.9041625684491653 | 0.9309325194714793 | 1000 |
| expanded_deterministic | workspace_compact | 0.6983669492464862 | 0.6678619177354412 | 0.7271183600845791 | 0.9267644715761387 | 0.9142553655108662 | 0.9382961023310271 | 1000 |
| expanded_deterministic | workspace_full | 0.6996038437078829 | 0.6691395456141562 | 0.7308976003441288 | 0.9276386068417477 | 0.9145863534557507 | 0.9403725136722499 | 1000 |
| expanded_deterministic | workspace_late_late_full | 0.6972720253757845 | 0.6684866376168018 | 0.7294624165167302 | 0.9263405387553648 | 0.9134224657733285 | 0.9390725382950355 | 1000 |
| expanded_deterministic | workspace_late_late_single | 0.6914084454998239 | 0.6610235309112651 | 0.7232842085940712 | 0.9247001025690713 | 0.9113691279120084 | 0.936440561114696 | 1000 |
| expanded_deterministic | workspace_noise_single | 0.6914084454998239 | 0.661364855237139 | 0.7234603700574644 | 0.9247001025690713 | 0.9120412882864468 | 0.9372544552939952 | 1000 |
| high_quality_primary | baseline_output_confidence | 0.7193798363672645 | 0.6901148793755297 | 0.7457314656433942 | 0.8976840053927779 | 0.8795163245116013 | 0.9142577487045037 | 1000 |
| high_quality_primary | combined_compact | 0.7674571147720303 | 0.7412478353377739 | 0.7933303976975504 | 0.9219223753474651 | 0.9059999358653372 | 0.9359913892684741 | 1000 |
| high_quality_primary | combined_full | 0.7667161851548006 | 0.740686151311603 | 0.7915572721648352 | 0.9235396558891489 | 0.9093780254900456 | 0.9368954770729473 | 1000 |
| high_quality_primary | commitment_dynamics_full | 0.6992306157291412 | 0.6700660076361735 | 0.7269068616460376 | 0.8986093046486002 | 0.8823610600947669 | 0.9126604297833023 | 1000 |
| high_quality_primary | commitment_dynamics_single | 0.6946483078719614 | 0.6658701618900874 | 0.7243178745887752 | 0.8955293741492665 | 0.8798676902739205 | 0.9118673779764221 | 1000 |
| high_quality_primary | layer_l33_diff | 0.5427669748638242 | 0.5116384854339894 | 0.571757410105694 | 0.8177548698297812 | 0.7925428377602245 | 0.8403725176283192 | 1000 |
| high_quality_primary | layer_l33_diff_in_full | 0.7241801733886166 | 0.6969194584618581 | 0.7519119272413923 | 0.9093917530708939 | 0.8953991814689719 | 0.9229725923871126 | 1000 |
| high_quality_primary | layer_l33_full | 0.6959657213809005 | 0.6699306024606413 | 0.723198511493574 | 0.8962465216308109 | 0.8812832170750634 | 0.9111964556365549 | 1000 |
| high_quality_primary | layer_l33_single | 0.6900770862434684 | 0.6621052132715957 | 0.718493876767345 | 0.8938765297258443 | 0.8755302945845498 | 0.9095171613930838 | 1000 |
| high_quality_primary | workspace_compact | 0.72250430515214 | 0.694965736577837 | 0.7495545180949277 | 0.9051173076005066 | 0.889454419470418 | 0.9199225830633653 | 1000 |
| high_quality_primary | workspace_full | 0.7344996045911768 | 0.7074572752116408 | 0.7597090729875448 | 0.9125262215685824 | 0.8981210320230896 | 0.9247020431307478 | 1000 |
| high_quality_primary | workspace_late_late_full | 0.7276575537866863 | 0.7021394516626702 | 0.7550354366662764 | 0.9100393378668721 | 0.8956475926495153 | 0.923391830610888 | 1000 |
| high_quality_primary | workspace_late_late_single | 0.7186444498643785 | 0.6900763552165323 | 0.7446834338539837 | 0.9064687146948964 | 0.8896070684196987 | 0.9204891424371485 | 1000 |
| high_quality_primary | workspace_noise_single | 0.7186444498643785 | 0.6909336679758971 | 0.7448598319280859 | 0.9064687146948964 | 0.8916361729812813 | 0.920484048183084 | 1000 |
| primary_with_llm_judge | baseline_output_confidence | 0.7179196421492434 | 0.6898832270667932 | 0.7470585373507156 | 0.8973080934511599 | 0.880077409546903 | 0.9143131328469174 | 1000 |
| primary_with_llm_judge | combined_compact | 0.765743091625503 | 0.7408115149940331 | 0.7906812984777636 | 0.9215869170179718 | 0.9073536468217865 | 0.9348110261945786 | 1000 |
| primary_with_llm_judge | combined_full | 0.7671296526775195 | 0.740900563747905 | 0.7923871905594825 | 0.9238095470507757 | 0.9103189092595104 | 0.9363483759606379 | 1000 |
| primary_with_llm_judge | commitment_dynamics_full | 0.6989152741131633 | 0.6696334297408377 | 0.7269896043437739 | 0.8984095985890388 | 0.8822624397000524 | 0.9137313900374631 | 1000 |
| primary_with_llm_judge | commitment_dynamics_single | 0.694128688353809 | 0.6647478870803825 | 0.7237990386737436 | 0.895485530044081 | 0.8788208158042472 | 0.9104377515205522 | 1000 |
| primary_with_llm_judge | layer_l33_diff | 0.541820857049612 | 0.5111976941681167 | 0.5731901823633131 | 0.8178770150182377 | 0.7955589732688645 | 0.8397105505549136 | 1000 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.7246957217584988 | 0.6975457333596339 | 0.7526840958737634 | 0.9096670048794716 | 0.8946803753641291 | 0.9233806068343112 | 1000 |
| primary_with_llm_judge | layer_l33_full | 0.6973848942286239 | 0.671071901153385 | 0.7262572977376796 | 0.8965931545139285 | 0.8803662139033718 | 0.9116271414690706 | 1000 |
| primary_with_llm_judge | layer_l33_single | 0.6898583753265886 | 0.6629630719753931 | 0.7193765256912482 | 0.8940312306823937 | 0.8767756923744504 | 0.910093485554776 | 1000 |
| primary_with_llm_judge | workspace_compact | 0.7226398499858947 | 0.6935923932927862 | 0.7510435920988187 | 0.9051312386649923 | 0.8887027586622313 | 0.9196540275153262 | 1000 |
| primary_with_llm_judge | workspace_full | 0.7368023173270348 | 0.7117272736505653 | 0.7639716875215727 | 0.9132799632959064 | 0.899346238191868 | 0.9268335087959655 | 1000 |
| primary_with_llm_judge | workspace_late_late_full | 0.7276347886692887 | 0.6989939604988925 | 0.7549623048252153 | 0.9101753168107578 | 0.8957028960050277 | 0.9237010310279283 | 1000 |
| primary_with_llm_judge | workspace_late_late_single | 0.7184561970244252 | 0.6910161509221762 | 0.7443556308068443 | 0.9064681970245131 | 0.8889373047502565 | 0.9201453759511234 | 1000 |
| primary_with_llm_judge | workspace_noise_single | 0.7184561970244252 | 0.6914605338105724 | 0.7455928696822358 | 0.9064681970245131 | 0.8922131018395115 | 0.9207840039346629 | 1000 |
| strict | baseline_output_confidence | 0.646445455089462 | 0.5665498291900757 | 0.7260046221280443 | 0.99107322409682 | 0.9866753435084161 | 0.9947972127114322 | 1000 |
| strict | combined_compact | 0.7152923224223566 | 0.6322853846402402 | 0.7898754846309125 | 0.9931239477479344 | 0.9897287943163157 | 0.9959451506021896 | 1000 |
| strict | combined_full | 0.7239991622284723 | 0.6439639621618787 | 0.8099362788940583 | 0.9925530185787536 | 0.9881232409423738 | 0.9964044747009807 | 1000 |
| strict | commitment_dynamics_full | 0.714170306983424 | 0.6331305665612741 | 0.7871599230632319 | 0.9929476783248813 | 0.9892217341936126 | 0.996093502343114 | 1000 |
| strict | commitment_dynamics_single | 0.6693345700436839 | 0.5610122705273181 | 0.7674452119752876 | 0.9898176133284069 | 0.9837125708888154 | 0.9949710138865998 | 1000 |
| strict | layer_l33_diff | 0.509754054215786 | 0.4153629441624365 | 0.6050072624251192 | 0.9846444457787552 | 0.9777050216924252 | 0.9904225353276718 | 1000 |
| strict | layer_l33_diff_in_full | 0.6944228352582131 | 0.609040097155758 | 0.7768799348638747 | 0.9921404578255483 | 0.987925412142157 | 0.9955870164336997 | 1000 |
| strict | layer_l33_full | 0.6508736760217821 | 0.5444077275038128 | 0.7469050377871767 | 0.9891247121642679 | 0.9825432683165973 | 0.9945030892602534 | 1000 |
| strict | layer_l33_single | 0.689366285680091 | 0.5834426688021991 | 0.7776490192024289 | 0.9907186663180835 | 0.9850159972060755 | 0.9950325882661746 | 1000 |
| strict | workspace_compact | 0.7067799652923223 | 0.624126816498165 | 0.7882893520817539 | 0.9927414604536291 | 0.9889005734187825 | 0.9958759152202825 | 1000 |
| strict | workspace_full | 0.717521393094369 | 0.6247008584276368 | 0.7997156587392077 | 0.9922036588016219 | 0.9878658390321531 | 0.9962677282595968 | 1000 |
| strict | workspace_late_late_full | 0.6890970019747472 | 0.5883134903861531 | 0.7846616756987912 | 0.9904911623218556 | 0.9847868692888165 | 0.9951884058712991 | 1000 |
| strict | workspace_late_late_single | 0.7094279217282029 | 0.6180414516540378 | 0.7984114161031522 | 0.9920816255916434 | 0.9875509693331286 | 0.9959711012995057 | 1000 |
| strict | workspace_noise_single | 0.7094279217282029 | 0.6071023068992215 | 0.8010916365402281 | 0.9920816255916434 | 0.9874913940036096 | 0.9958321521819334 | 1000 |


## Permutation sanity checks

| label_regime | feature_set | real_roc_auc | perm_auc_mean | perm_auc_ci_low | perm_auc_ci_high | p_perm_ge_real | permutation_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.6580084054368901 | 0.5017604956134977 | 0.4628401459768841 | 0.5383752827256797 | 0.0 | 500 |
| expanded_deterministic | combined_compact | 0.7231145624874804 | 0.500648583891978 | 0.4646321600339174 | 0.5373628671058032 | 0.0 | 500 |
| expanded_deterministic | combined_full | 0.7219671289462477 | 0.4993592069872868 | 0.4634497686657293 | 0.5343687948641652 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_full | 0.6689226376968869 | 0.500133985231169 | 0.46347855174439073 | 0.5346599804352856 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_single | 0.6632574276873769 | 0.5003662257799145 | 0.46591140257219593 | 0.539442055578569 | 0.0 | 500 |
| expanded_deterministic | layer_l33_diff | 0.5155943997463976 | 0.5001374975446867 | 0.4679599604038188 | 0.5364688413449477 | 0.178 | 500 |
| expanded_deterministic | layer_l33_diff_in_full | 0.680447537977133 | 0.5000357260239872 | 0.466956879836481 | 0.5347338829345516 | 0.0 | 500 |
| expanded_deterministic | layer_l33_full | 0.6774408731385808 | 0.5004362347843505 | 0.46664896896289515 | 0.5328955582653139 | 0.0 | 500 |
| expanded_deterministic | layer_l33_single | 0.667781038563491 | 0.5001570000252824 | 0.4627715673747693 | 0.5349502422251654 | 0.0 | 500 |
| expanded_deterministic | workspace_compact | 0.6983669492464862 | 0.498774844367171 | 0.4656642667802432 | 0.5326542082611325 | 0.0 | 500 |
| expanded_deterministic | workspace_full | 0.6996038437078829 | 0.5005309427819624 | 0.46538120076002887 | 0.5347027174726902 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_full | 0.6972720253757845 | 0.5005039722593355 | 0.4630406308161753 | 0.5384565268548069 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_single | 0.6914084454998239 | 0.500549371731516 | 0.46496909708649115 | 0.5372073315168877 | 0.0 | 500 |
| expanded_deterministic | workspace_noise_single | 0.6914084454998239 | 0.49984905220044684 | 0.46475813462312643 | 0.5328785412424566 | 0.0 | 500 |
| high_quality_primary | baseline_output_confidence | 0.7193798363672645 | 0.5010348717323341 | 0.4700860522309187 | 0.5308394169013252 | 0.0 | 500 |
| high_quality_primary | combined_compact | 0.7674571147720303 | 0.4993339467713207 | 0.4631892400759776 | 0.5301852601198791 | 0.0 | 500 |
| high_quality_primary | combined_full | 0.7667161851548006 | 0.5007337420456309 | 0.47012321419332903 | 0.5342899362911391 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_full | 0.6992306157291412 | 0.4993352216876196 | 0.46598869758985384 | 0.530492579617599 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_single | 0.6946483078719614 | 0.4991494497535162 | 0.46510327745874075 | 0.5312501847704781 | 0.0 | 500 |
| high_quality_primary | layer_l33_diff | 0.5427669748638242 | 0.4999135902382061 | 0.47066085009201575 | 0.5346987871665817 | 0.006 | 500 |
| high_quality_primary | layer_l33_diff_in_full | 0.7241801733886166 | 0.4980820380922818 | 0.4661367911280607 | 0.5299970251953023 | 0.0 | 500 |
| high_quality_primary | layer_l33_full | 0.6959657213809005 | 0.5000039577836413 | 0.46434719666230606 | 0.5322785710590304 | 0.0 | 500 |
| high_quality_primary | layer_l33_single | 0.6900770862434684 | 0.49907859766597934 | 0.4696551905722711 | 0.5334977790588531 | 0.0 | 500 |
| high_quality_primary | workspace_compact | 0.72250430515214 | 0.4996696377759547 | 0.46470860771749334 | 0.5332755925589232 | 0.0 | 500 |
| high_quality_primary | workspace_full | 0.7344996045911768 | 0.49967970776701187 | 0.47104013769096026 | 0.5312075027900341 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_full | 0.7276575537866863 | 0.5009566824091114 | 0.46764530350398736 | 0.5336703546854098 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_single | 0.7186444498643785 | 0.4986584369895716 | 0.46598024434048024 | 0.5302321456287 | 0.0 | 500 |
| high_quality_primary | workspace_noise_single | 0.7186444498643785 | 0.4996591723760745 | 0.46624871584517713 | 0.5326292654264873 | 0.0 | 500 |
| primary_with_llm_judge | baseline_output_confidence | 0.7179196421492434 | 0.5003513383448664 | 0.4690208242294169 | 0.5311016983529055 | 0.0 | 500 |
| primary_with_llm_judge | combined_compact | 0.765743091625503 | 0.5000291767846903 | 0.4695361289501778 | 0.531208456178586 | 0.0 | 500 |
| primary_with_llm_judge | combined_full | 0.7671296526775195 | 0.5001795854698726 | 0.4669377559468165 | 0.5328914591895624 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_full | 0.6989152741131633 | 0.5000013791857273 | 0.4701552874625011 | 0.530835910087416 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_single | 0.694128688353809 | 0.5001808872146902 | 0.46716634491812464 | 0.5341328646314457 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_diff | 0.541820857049612 | 0.49862852148708675 | 0.46665094800580437 | 0.5321684007898972 | 0.002 | 500 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.7246957217584988 | 0.5014264689342102 | 0.46814901474880566 | 0.5336672050653731 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_full | 0.6973848942286239 | 0.5000382115575026 | 0.4691921161466141 | 0.5324795012067876 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_single | 0.6898583753265886 | 0.4998610451941462 | 0.4677949069694975 | 0.5325686965404195 | 0.0 | 500 |
| primary_with_llm_judge | workspace_compact | 0.7226398499858947 | 0.5011264812878792 | 0.4677872550700748 | 0.534589120658469 | 0.0 | 500 |
| primary_with_llm_judge | workspace_full | 0.7368023173270348 | 0.4995430396294636 | 0.4705193058344351 | 0.5290127759062891 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_full | 0.7276347886692887 | 0.4996161807249575 | 0.46883685597281455 | 0.5302379095379544 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_single | 0.7184561970244252 | 0.5004082131616358 | 0.46857120599466395 | 0.5319810214456006 | 0.0 | 500 |
| primary_with_llm_judge | workspace_noise_single | 0.7184561970244252 | 0.49994311412024367 | 0.4670949425554394 | 0.5321657272346773 | 0.0 | 500 |
| strict | baseline_output_confidence | 0.646445455089462 | 0.49848623661061575 | 0.4041073245167853 | 0.5948260128059362 | 0.002 | 500 |
| strict | combined_compact | 0.7152923224223566 | 0.5052012746095386 | 0.40717005265992456 | 0.6054514990126264 | 0.0 | 500 |
| strict | combined_full | 0.7239991622284723 | 0.4993601519956915 | 0.3994221620489498 | 0.5960175932020824 | 0.0 | 500 |
| strict | commitment_dynamics_full | 0.714170306983424 | 0.5031676141463707 | 0.400510143019568 | 0.6018528214948238 | 0.0 | 500 |
| strict | commitment_dynamics_single | 0.6693345700436839 | 0.49761229130512835 | 0.3946105858416612 | 0.5932069445275566 | 0.0 | 500 |
| strict | layer_l33_diff | 0.509754054215786 | 0.5031189635569385 | 0.4095760277661421 | 0.5975065076895457 | 0.47 | 500 |
| strict | layer_l33_diff_in_full | 0.6944228352582131 | 0.5028943510262701 | 0.40992347854706485 | 0.5969481180061038 | 0.002 | 500 |
| strict | layer_l33_full | 0.6508736760217821 | 0.4986233917778709 | 0.4054114804619711 | 0.5947171773083598 | 0.0 | 500 |
| strict | layer_l33_single | 0.689366285680091 | 0.49915417988151517 | 0.40025806355095445 | 0.6003702650948477 | 0.0 | 500 |
| strict | workspace_compact | 0.7067799652923223 | 0.4984384237927113 | 0.3953455059541619 | 0.6097151576805697 | 0.0 | 500 |
| strict | workspace_full | 0.717521393094369 | 0.4994632876548381 | 0.40580081981928073 | 0.6027930704326492 | 0.0 | 500 |
| strict | workspace_late_late_full | 0.6890970019747472 | 0.4989064987134223 | 0.39738233798097067 | 0.5990305786607624 | 0.0 | 500 |
| strict | workspace_late_late_single | 0.7094279217282029 | 0.4996881096283885 | 0.3910429507510023 | 0.5971459667285022 | 0.0 | 500 |
| strict | workspace_noise_single | 0.7094279217282029 | 0.4991291963377416 | 0.3938061007719466 | 0.594397402908264 | 0.0 | 500 |


## H.3 quadrant analysis

| quadrant | n | accuracy | wrong_rate | mean_confidence | mean_workspace_noise |
| --- | --- | --- | --- | --- | --- |
| high_confidence__clean_workspace | 463 | 0.3952483801295896 | 0.6047516198704104 | 0.8910143439764595 | 1.0804909726635583 |
| high_confidence__noisy_workspace | 466 | 0.19313304721030042 | 0.8068669527896996 | 0.8347012451789921 | 2.151883210773409 |
| low_confidence__clean_workspace | 234 | 0.24786324786324787 | 0.7521367521367521 | 0.44809104816923884 | 1.0099978255885969 |
| low_confidence__noisy_workspace | 647 | 0.07418856259659969 | 0.9258114374034003 | 0.4363565143915067 | 2.4640324487038523 |


## Rec 2 (single-feature callout)

See `brief_single_feature.md` for the parsimonious `workspace_noise_score` AUC + CI + strict-above-baseline check. The most defensible single-feature claim is in there.

## Rec 3 (layer-specific features, v2.1+)

**v2.2 note:** As of v2.2, `workspace_noise_score` IS the `late_late` band entropy (L30-L34), so `workspace_noise_single` and `workspace_late_late_single` are now the same field. The wider `late` band (L27-L34) is preserved as `late_entropy_topk_mean` for backwards compatibility. To compare bands side-by-side, look at `late_entropy_topk_mean` vs `late_late_entropy_topk_mean` directly in `workspace_aggregate_features.csv`.

**Layer-specific ablations** (also in `auc_scores.csv`):
- `commitment_dynamics_*`: commitment-dynamic features (max-minus-mean of top-1 dominance in last 3 layers).
- `layer_l33_single` / `layer_l33_full`: L33 alone entropy / full L33 triplet (entropy + dominance + margin). Tests whether the signal is concentrated at a single layer.
- `layer_l33_diff` / `layer_l33_diff_in_full`: L33 - L34 entropy difference, with and without the underlying L33 features. Tests the "commitment flip" hypothesis in the last two layers.

## Key machine-readable files

- `manifest.json`
- `config.json`
- `model_lens.json`
- `datasets/dataset_manifest.json`
- `datasets/questions.jsonl`
- `prompts/prompts.jsonl`
- `generations/generations.jsonl`
- `scans/workspace_aggregate_features.csv`
- `scans/workspace_layer_features.csv`
- `metrics/per_example_metrics.csv`
- `metrics/auc_scores.csv`
- `metrics/auc_bootstrap_ci.csv`
- `metrics/auc_permutation_sanity.csv`
- `metrics/cv_predictions.csv`
- `metrics/quadrant_analysis.csv`
- `metrics/aggregate_metrics.json`

## Selected example reports

- `examples/confident_wrong_noisy.md` — cases where J-space noise may catch confident errors.
- `examples/confident_wrong_clean_blindspots.md` — confident wrong answers with clean workspaces.
- `examples/confident_correct_clean.md` — high-confidence correct clean examples.
- `examples/possible_label_noise.md` — likely automatic-label edge cases.

## Caveats

- This is not a lie detector; it tests correlations between workspace features and correctness.
- Correctness labels are automatic and should be manually audited for key examples.
- Workspace entropy may reflect answer-type ambiguity, formatting, or tokenization, not only epistemic uncertainty.
- Display filters are optional and do not affect metrics. No NSFW-specific filtering is implemented.
- Full logits/residuals are not saved by default.
