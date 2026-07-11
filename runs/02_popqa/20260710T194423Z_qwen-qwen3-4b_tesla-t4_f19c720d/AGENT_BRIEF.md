# Agent Brief — Hallucination Detection via J-Space

## Run metadata

- Run ID: `20260710T194423Z_qwen-qwen3-4b_tesla-t4_f19c720d`
- Experiment: `01_hallucination_detection` — Hallucination Detection via J-Space State
- Dataset ID: `popqa` (role: `dev`)
- Dataset repo: `akariasai/PopQA` (config `default`, split `test`)
- Model: `Qwen/Qwen3-4B`
- dtype: `torch.bfloat16`
- Lens: `qwen3-4b/jlens/Salesforce-wikitext/Qwen3-4B_jacobian_lens.pt`
- GPU: `Tesla T4`
- Run mode: `full`
- Examples processed: `2000`

## Main conclusion

**supports_H_C_or_no_signal** — Workspace features did not improve prediction over output confidence under the primary label regime in this run. The single-feature `workspace_noise_score` AUC is 0.839 with CI [0.807, 0.869]; CI overlaps baseline upper bound (0.850), so the parsimonious claim is not statistically distinguishable either.

## Summary table

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


## AUC table

| label_regime | feature_set | features | roc_auc | roc_auc_per_fold_std | n_folds_with_both_classes | pr_auc | n_splits | n | n_wrong |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8103665814151747 | 0.042178959990558484 | 5 | 0.9949466375385307 | 5 | 2000 | 1955 |
| strict | workspace_noise_single | ['workspace_noise_score'] | 0.869337880079568 | 0.06623808678560954 | 5 | 0.9960250679790308 | 5 | 2000 | 1955 |
| strict | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8704290991759022 | 0.0415840314087488 | 5 | 0.9963728730628658 | 5 | 2000 | 1955 |
| strict | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8908439897698209 | 0.03628861824697456 | 5 | 0.9967637023895721 | 5 | 2000 | 1955 |
| strict | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.905541346973572 | 0.03132442945132234 | 5 | 0.9975877257690429 | 5 | 2000 | 1955 |
| strict | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.9186018755328218 | 0.02038958743442895 | 5 | 0.9979747752426141 | 5 | 2000 | 1955 |
| strict | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.869337880079568 | 0.06623808678560954 | 5 | 0.9960250679790308 | 5 | 2000 | 1955 |
| strict | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.9118840579710144 | 0.04694916269229827 | 5 | 0.9974743508883034 | 5 | 2000 | 1955 |
| strict | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.8316908212560387 | 0.052807394906227434 | 5 | 0.9948033727682586 | 5 | 2000 | 1955 |
| strict | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.8431031543052003 | 0.0470788451339625 | 5 | 0.9953802324323427 | 5 | 2000 | 1955 |
| strict | layer_l33_single | ['layer_l33_entropy_topk'] | 0.889434498437056 | 0.052889144287907475 | 5 | 0.9968701849779071 | 5 | 2000 | 1955 |
| strict | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.8828871838590507 | 0.0541948918696225 | 5 | 0.9964697743027648 | 5 | 2000 | 1955 |
| strict | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.6685080988917306 | 0.0848609030971053 | 5 | 0.9879373700887373 | 5 | 2000 | 1955 |
| strict | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.9088377379937482 | 0.04825080471002178 | 5 | 0.997324710945179 | 5 | 2000 | 1955 |
| expanded_deterministic | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8200334086422393 | 0.03660828329544951 | 5 | 0.9780085570244392 | 5 | 2000 | 1823 |
| expanded_deterministic | workspace_noise_single | ['workspace_noise_score'] | 0.8307595042628559 | 0.02104506622496518 | 5 | 0.9776979018297814 | 5 | 2000 | 1823 |
| expanded_deterministic | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8152917367845266 | 0.03651250651740383 | 5 | 0.9733134396557672 | 5 | 2000 | 1823 |
| expanded_deterministic | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8649150372980527 | 0.027259873658504193 | 5 | 0.9841432765271415 | 5 | 2000 | 1823 |
| expanded_deterministic | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8664243145494946 | 0.03194394577072925 | 5 | 0.9828794169633908 | 5 | 2000 | 1823 |
| expanded_deterministic | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8897855710615457 | 0.025203311956571564 | 5 | 0.9870937915612551 | 5 | 2000 | 1823 |
| expanded_deterministic | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.8307595042628559 | 0.02104506622496518 | 5 | 0.9776979018297814 | 5 | 2000 | 1823 |
| expanded_deterministic | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.8636103027541986 | 0.031577042551953066 | 5 | 0.9828161090908066 | 5 | 2000 | 1823 |
| expanded_deterministic | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.750684133374242 | 0.04332110867577012 | 5 | 0.9633423601250015 | 5 | 2000 | 1823 |
| expanded_deterministic | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7625290156227241 | 0.04115784112262702 | 5 | 0.9663053549429508 | 5 | 2000 | 1823 |
| expanded_deterministic | layer_l33_single | ['layer_l33_entropy_topk'] | 0.8511920810980844 | 0.025675012384243433 | 5 | 0.9803879328805557 | 5 | 2000 | 1823 |
| expanded_deterministic | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.8538108475815924 | 0.026406549069072742 | 5 | 0.9809219485859497 | 5 | 2000 | 1823 |
| expanded_deterministic | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5657279396041169 | 0.05295629922859744 | 5 | 0.9246238343079834 | 5 | 2000 | 1823 |
| expanded_deterministic | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.8707166122769013 | 0.02995972974399908 | 5 | 0.9841491367934487 | 5 | 2000 | 1823 |
| primary_with_llm_judge | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8244243122045812 | 0.025378115232253286 | 5 | 0.9776200409240255 | 5 | 1969 | 1784 |
| primary_with_llm_judge | workspace_noise_single | ['workspace_noise_score'] | 0.8390679917585747 | 0.010183894786398646 | 5 | 0.9775135838873685 | 5 | 1969 | 1784 |
| primary_with_llm_judge | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8198339595200581 | 0.03314030426134786 | 5 | 0.9722260854359766 | 5 | 1969 | 1784 |
| primary_with_llm_judge | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8712913586231972 | 0.012737378186637963 | 5 | 0.984223193752563 | 5 | 1969 | 1784 |
| primary_with_llm_judge | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.870024845473276 | 0.012219669284826509 | 5 | 0.9824673442117816 | 5 | 1969 | 1784 |
| primary_with_llm_judge | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8940189067991761 | 0.011215749597860638 | 5 | 0.9870387803225593 | 5 | 1969 | 1784 |
| primary_with_llm_judge | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.8390679917585747 | 0.010183894786398646 | 5 | 0.9775135838873685 | 5 | 1969 | 1784 |
| primary_with_llm_judge | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.8759938189310386 | 0.009989979347865966 | 5 | 0.9840417837468867 | 5 | 1969 | 1784 |
| primary_with_llm_judge | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.758835292691795 | 0.020218335109096923 | 5 | 0.9627755649150279 | 5 | 1969 | 1784 |
| primary_with_llm_judge | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7734365531450733 | 0.02183123752284731 | 5 | 0.9664364715939466 | 5 | 1969 | 1784 |
| primary_with_llm_judge | layer_l33_single | ['layer_l33_entropy_topk'] | 0.8589413404435826 | 0.015843748480841094 | 5 | 0.9807786272969399 | 5 | 1969 | 1784 |
| primary_with_llm_judge | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.8593170524784874 | 0.013657003687272679 | 5 | 0.9810670089124154 | 5 | 1969 | 1784 |
| primary_with_llm_judge | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5634044358259604 | 0.05363586880677153 | 5 | 0.917197183459522 | 5 | 1969 | 1784 |
| primary_with_llm_judge | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.8774360683553508 | 0.005157221146607242 | 5 | 0.9846853081515717 | 5 | 1969 | 1784 |
| high_quality_primary | baseline_output_confidence | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens'] | 0.8251413499871154 | 0.02155538169927217 | 5 | 0.9777232490576864 | 5 | 1968 | 1783 |
| high_quality_primary | workspace_noise_single | ['workspace_noise_score'] | 0.8389625744645374 | 0.015065441138200098 | 5 | 0.9774595485581454 | 5 | 1968 | 1783 |
| high_quality_primary | workspace_compact | ['late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.819917842688454 | 0.035066777702423446 | 5 | 0.9722184761129928 | 5 | 1968 | 1783 |
| high_quality_primary | workspace_full | ['late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.8712888996680359 | 0.011808930406840931 | 5 | 0.9841606060673178 | 5 | 1968 | 1783 |
| high_quality_primary | combined_compact | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_churn_rate'] | 0.8700459292719528 | 0.007328464697075426 | 5 | 0.98247271645186 | 5 | 1968 | 1783 |
| high_quality_primary | combined_full | ['first_content_token_prob', 'sequence_content_logprob_mean', 'answer_length_content_tokens', 'late_entropy_topk_mean', 'late_entropy_topk_std', 'late_entropy_topk_slope', 'late_effective_concepts_topk_mean', 'late_top1_dominance_topk_mean', 'late_top1_margin_mean', 'late_distinct_top1_count', 'late_top1_churn_rate', 'late_top5_jaccard_adjacent_mean'] | 0.893774537296691 | 0.011462787762455328 | 5 | 0.986976486656099 | 5 | 1968 | 1783 |
| high_quality_primary | workspace_late_late_single | ['late_late_entropy_topk_mean'] | 0.8389625744645374 | 0.015065441138200098 | 5 | 0.9774595485581454 | 5 | 1968 | 1783 |
| high_quality_primary | workspace_late_late_full | ['late_late_entropy_topk_mean', 'late_late_entropy_topk_std', 'late_late_entropy_topk_slope'] | 0.8762971608737172 | 0.012267965785037827 | 5 | 0.9841111904511811 | 5 | 1968 | 1783 |
| high_quality_primary | commitment_dynamics_single | ['late_top1_dominance_topk_mean'] | 0.758396871352564 | 0.02588454895275333 | 5 | 0.9625580240833714 | 5 | 1968 | 1783 |
| high_quality_primary | commitment_dynamics_full | ['late_top1_dominance_topk_mean', 'late_top1_dominance_last3_max_minus_mean', 'late_top1_churn_rate'] | 0.7730821118370192 | 0.03132779312172741 | 5 | 0.9662994673822549 | 5 | 1968 | 1783 |
| high_quality_primary | layer_l33_single | ['layer_l33_entropy_topk'] | 0.8589016385987783 | 0.012653283203705465 | 5 | 0.9809299683278064 | 5 | 1968 | 1783 |
| high_quality_primary | layer_l33_full | ['layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk', 'layer_l33_top1_margin'] | 0.8599263312667687 | 0.011888936352614158 | 5 | 0.9811501717708607 | 5 | 1968 | 1783 |
| high_quality_primary | layer_l33_diff | ['layer_l33_l34_entropy_diff'] | 0.5627108881175061 | 0.05254164430902407 | 5 | 0.9173858573019777 | 5 | 1968 | 1783 |
| high_quality_primary | layer_l33_diff_in_full | ['layer_l33_l34_entropy_diff', 'layer_l33_entropy_topk', 'layer_l33_top1_dominance_topk'] | 0.8779766867259857 | 0.00926379820499667 | 5 | 0.9847504750185507 | 5 | 1968 | 1783 |


## Bootstrap AUC intervals

| label_regime | feature_set | roc_auc | roc_auc_ci_low | roc_auc_ci_high | pr_auc | pr_auc_ci_low | pr_auc_ci_high | bootstrap_n_effective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.8200334086422393 | 0.7928100766225508 | 0.8444310195225219 | 0.9780085570244392 | 0.9708776318017412 | 0.9834219030494037 | 1000 |
| expanded_deterministic | combined_compact | 0.8664243145494946 | 0.8397527524122165 | 0.8908258851044006 | 0.9828794169633908 | 0.976924238377004 | 0.9876677766993355 | 1000 |
| expanded_deterministic | combined_full | 0.8897855710615457 | 0.8664113142390265 | 0.911399798997778 | 0.9870937915612551 | 0.9832906622544609 | 0.9905155944827856 | 1000 |
| expanded_deterministic | commitment_dynamics_full | 0.7625290156227241 | 0.7237390404002052 | 0.796455402855867 | 0.9663053549429508 | 0.9576803174624028 | 0.9737210928438221 | 1000 |
| expanded_deterministic | commitment_dynamics_single | 0.750684133374242 | 0.7093242778371252 | 0.7915585751247086 | 0.9633423601250015 | 0.9540116231071931 | 0.9717666011582936 | 1000 |
| expanded_deterministic | layer_l33_diff | 0.5657279396041169 | 0.517852768780531 | 0.6114563674807322 | 0.9246238343079834 | 0.9087703854469438 | 0.9398325229072092 | 1000 |
| expanded_deterministic | layer_l33_diff_in_full | 0.8707166122769013 | 0.8432702990173672 | 0.8954237497946121 | 0.9841491367934487 | 0.9789602673141472 | 0.9885161552028406 | 1000 |
| expanded_deterministic | layer_l33_full | 0.8538108475815924 | 0.8242904624164928 | 0.8822353292333336 | 0.9809219485859497 | 0.9741775874887659 | 0.9863261388538885 | 1000 |
| expanded_deterministic | layer_l33_single | 0.8511920810980844 | 0.8212030163013185 | 0.8794854929687411 | 0.9803879328805557 | 0.9733200129153774 | 0.9862822002355836 | 1000 |
| expanded_deterministic | workspace_compact | 0.8152917367845266 | 0.776595493734251 | 0.8470546494247254 | 0.9733134396557672 | 0.9647304062075832 | 0.9801149996454731 | 1000 |
| expanded_deterministic | workspace_full | 0.8649150372980527 | 0.8411492590654134 | 0.8907580119949821 | 0.9841432765271415 | 0.9795719967773917 | 0.9884801770331061 | 1000 |
| expanded_deterministic | workspace_late_late_full | 0.8636103027541986 | 0.8368293826586087 | 0.8905036976118818 | 0.9828161090908066 | 0.9771561573657949 | 0.9876531392532383 | 1000 |
| expanded_deterministic | workspace_late_late_single | 0.8307595042628559 | 0.798655424136315 | 0.8618214504692709 | 0.9776979018297814 | 0.9713792124621748 | 0.9838445871570493 | 1000 |
| expanded_deterministic | workspace_noise_single | 0.8307595042628559 | 0.7965399800673877 | 0.8592674854493757 | 0.9776979018297814 | 0.9710095977184631 | 0.9833846557237357 | 1000 |
| high_quality_primary | baseline_output_confidence | 0.8251413499871154 | 0.7991621293902611 | 0.8475777548461675 | 0.9777232490576864 | 0.9716968657391052 | 0.9831087050893057 | 1000 |
| high_quality_primary | combined_compact | 0.8700459292719528 | 0.8420135082867084 | 0.8939843808589781 | 0.98247271645186 | 0.9764920668202974 | 0.9872685989602664 | 1000 |
| high_quality_primary | combined_full | 0.893774537296691 | 0.8725112270867025 | 0.9153122197182116 | 0.986976486656099 | 0.983147559663063 | 0.9904727465042713 | 1000 |
| high_quality_primary | commitment_dynamics_full | 0.7730821118370192 | 0.7360008090289223 | 0.8085420488732363 | 0.9662994673822549 | 0.9571619038138423 | 0.974743536856228 | 1000 |
| high_quality_primary | commitment_dynamics_single | 0.758396871352564 | 0.7202023856000626 | 0.8005906151250208 | 0.9625580240833714 | 0.953366640992131 | 0.9716833333243574 | 1000 |
| high_quality_primary | layer_l33_diff | 0.5627108881175061 | 0.516443094643134 | 0.6071185657122774 | 0.9173858573019777 | 0.8987840505076479 | 0.9351595155811455 | 1000 |
| high_quality_primary | layer_l33_diff_in_full | 0.8779766867259857 | 0.8545908343785011 | 0.9009903387245551 | 0.9847504750185507 | 0.9806079924051525 | 0.9890147870265364 | 1000 |
| high_quality_primary | layer_l33_full | 0.8599263312667687 | 0.8310585632757398 | 0.8862481842053669 | 0.9811501717708607 | 0.9751165546988931 | 0.9865891178978072 | 1000 |
| high_quality_primary | layer_l33_single | 0.8589016385987783 | 0.8321317161637136 | 0.8847598619438485 | 0.9809299683278064 | 0.9746255110502273 | 0.9859718407262085 | 1000 |
| high_quality_primary | workspace_compact | 0.819917842688454 | 0.7825707961836906 | 0.8535698553641168 | 0.9722184761129928 | 0.9632389666505887 | 0.9793616195854739 | 1000 |
| high_quality_primary | workspace_full | 0.8712888996680359 | 0.8464854637041889 | 0.8945566755972243 | 0.9841606060673178 | 0.9796908095517302 | 0.9882253722411677 | 1000 |
| high_quality_primary | workspace_late_late_full | 0.8762971608737172 | 0.8529537137412675 | 0.9001468085409684 | 0.9841111904511811 | 0.9794765748302217 | 0.98827760649335 | 1000 |
| high_quality_primary | workspace_late_late_single | 0.8389625744645374 | 0.8078354615806765 | 0.8687651255833638 | 0.9774595485581454 | 0.9713122909499468 | 0.9834978322001534 | 1000 |
| high_quality_primary | workspace_noise_single | 0.8389625744645374 | 0.8087941516635515 | 0.8681772939863409 | 0.9774595485581454 | 0.970841126055762 | 0.9835356071428788 | 1000 |
| primary_with_llm_judge | baseline_output_confidence | 0.8244243122045812 | 0.7965478427799135 | 0.8495558879358458 | 0.9776200409240255 | 0.97072135433223 | 0.9828790612909102 | 1000 |
| primary_with_llm_judge | combined_compact | 0.870024845473276 | 0.8410621572672595 | 0.8949625243643364 | 0.9824673442117816 | 0.976586058623019 | 0.987689250734371 | 1000 |
| primary_with_llm_judge | combined_full | 0.8940189067991761 | 0.8709894250907478 | 0.9158632411762543 | 0.9870387803225593 | 0.9832761211468546 | 0.9905517082297879 | 1000 |
| primary_with_llm_judge | commitment_dynamics_full | 0.7734365531450733 | 0.7424605506153749 | 0.8076971948983257 | 0.9664364715939466 | 0.9584509019058498 | 0.9741025683439998 | 1000 |
| primary_with_llm_judge | commitment_dynamics_single | 0.758835292691795 | 0.7175961073616407 | 0.798557760355452 | 0.9627755649150279 | 0.9538055617876857 | 0.9721162008481946 | 1000 |
| primary_with_llm_judge | layer_l33_diff | 0.5634044358259604 | 0.5187106961883876 | 0.606907182391312 | 0.917197183459522 | 0.9004454279393853 | 0.9344243294870376 | 1000 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.8774360683553508 | 0.8513567963901909 | 0.9004415605218545 | 0.9846853081515717 | 0.9799997272941454 | 0.9885019268109249 | 1000 |
| primary_with_llm_judge | layer_l33_full | 0.8593170524784874 | 0.8317869708452231 | 0.8855002924764764 | 0.9810670089124154 | 0.9752612449652651 | 0.986379683612028 | 1000 |
| primary_with_llm_judge | layer_l33_single | 0.8589413404435826 | 0.8290546545540324 | 0.8855026878037707 | 0.9807786272969399 | 0.9747583945666906 | 0.9861391756755364 | 1000 |
| primary_with_llm_judge | workspace_compact | 0.8198339595200581 | 0.7831555747200859 | 0.8511007668367596 | 0.9722260854359766 | 0.963683397331449 | 0.9794655056569973 | 1000 |
| primary_with_llm_judge | workspace_full | 0.8712913586231972 | 0.8469634546468463 | 0.8932219647009673 | 0.984223193752563 | 0.9798548338546025 | 0.9881292433881693 | 1000 |
| primary_with_llm_judge | workspace_late_late_full | 0.8759938189310386 | 0.8505471612183064 | 0.901127742594081 | 0.9840417837468867 | 0.9788558068685398 | 0.9884921965871452 | 1000 |
| primary_with_llm_judge | workspace_late_late_single | 0.8390679917585747 | 0.8049751562952594 | 0.8674847897862743 | 0.9775135838873685 | 0.9713495713886596 | 0.9830529887992586 | 1000 |
| primary_with_llm_judge | workspace_noise_single | 0.8390679917585747 | 0.8073745746527557 | 0.8694350650665905 | 0.9775135838873685 | 0.970598851768978 | 0.983659724054193 | 1000 |
| strict | baseline_output_confidence | 0.8103665814151747 | 0.7721744981024355 | 0.8482010230313399 | 0.9949466375385307 | 0.993033904517473 | 0.9965666426846759 | 1000 |
| strict | combined_compact | 0.905541346973572 | 0.8750260872546266 | 0.9304570279528371 | 0.9975877257690429 | 0.9963486750095714 | 0.9985559059002092 | 1000 |
| strict | combined_full | 0.9186018755328218 | 0.8919385707205421 | 0.9410839559833105 | 0.9979747752426141 | 0.9970067779905907 | 0.9987594332232321 | 1000 |
| strict | commitment_dynamics_full | 0.8431031543052003 | 0.7878832702904616 | 0.8915180821352282 | 0.9953802324323427 | 0.9931955873918077 | 0.9974907536024853 | 1000 |
| strict | commitment_dynamics_single | 0.8316908212560387 | 0.7697494537749898 | 0.886077577750327 | 0.9948033727682586 | 0.9919970074023378 | 0.9972264011840885 | 1000 |
| strict | layer_l33_diff | 0.6685080988917306 | 0.5952718607224972 | 0.7338546684671654 | 0.9879373700887373 | 0.981794425417076 | 0.9928693172771366 | 1000 |
| strict | layer_l33_diff_in_full | 0.9088377379937482 | 0.8600142381773038 | 0.9520464054287872 | 0.997324710945179 | 0.9952471573041533 | 0.9989475527949249 | 1000 |
| strict | layer_l33_full | 0.8828871838590507 | 0.8331357938824352 | 0.9251525482759704 | 0.9964697743027648 | 0.993912961623389 | 0.9982813225894543 | 1000 |
| strict | layer_l33_single | 0.889434498437056 | 0.8432637033442892 | 0.9272409571328933 | 0.9968701849779071 | 0.9950891268369887 | 0.9984412981475773 | 1000 |
| strict | workspace_compact | 0.8704290991759022 | 0.8247809915973539 | 0.9089430303420841 | 0.9963728730628658 | 0.9944205179319353 | 0.9979440698193841 | 1000 |
| strict | workspace_full | 0.8908439897698209 | 0.8403592757392687 | 0.9300603968589518 | 0.9967637023895721 | 0.9942154457819866 | 0.9985254975620246 | 1000 |
| strict | workspace_late_late_full | 0.9118840579710144 | 0.8623578280357076 | 0.949699661625893 | 0.9974743508883034 | 0.9957349201901843 | 0.9987948794076994 | 1000 |
| strict | workspace_late_late_single | 0.869337880079568 | 0.8168175245553808 | 0.9171255078725873 | 0.9960250679790308 | 0.9932589938317959 | 0.9980081682255758 | 1000 |
| strict | workspace_noise_single | 0.869337880079568 | 0.8164729606588206 | 0.9153706844364439 | 0.9960250679790308 | 0.9932510049525669 | 0.9980239774254224 | 1000 |


## Permutation sanity checks

| label_regime | feature_set | real_roc_auc | perm_auc_mean | perm_auc_ci_low | perm_auc_ci_high | p_perm_ge_real | permutation_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| expanded_deterministic | baseline_output_confidence | 0.8200334086422393 | 0.5018761153001045 | 0.45791045678105563 | 0.5429215826646956 | 0.0 | 500 |
| expanded_deterministic | combined_compact | 0.8664243145494946 | 0.5002279659467384 | 0.45995092524583864 | 0.5436076529963957 | 0.0 | 500 |
| expanded_deterministic | combined_full | 0.8897855710615457 | 0.5003615385330569 | 0.45794152557868545 | 0.543870846775818 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_full | 0.7625290156227241 | 0.49836852397643416 | 0.45450513061291536 | 0.5442680780113489 | 0.0 | 500 |
| expanded_deterministic | commitment_dynamics_single | 0.750684133374242 | 0.5001765451497036 | 0.4559000498960242 | 0.5446457072374028 | 0.0 | 500 |
| expanded_deterministic | layer_l33_diff | 0.5657279396041169 | 0.49978840366813254 | 0.45486819391888333 | 0.5439095084466841 | 0.004 | 500 |
| expanded_deterministic | layer_l33_diff_in_full | 0.8707166122769013 | 0.5008103300265596 | 0.4572513488971739 | 0.5486952654561457 | 0.0 | 500 |
| expanded_deterministic | layer_l33_full | 0.8538108475815924 | 0.5005877875607042 | 0.46009038618283016 | 0.543452851356335 | 0.0 | 500 |
| expanded_deterministic | layer_l33_single | 0.8511920810980844 | 0.4996122614055803 | 0.4547333816797915 | 0.5402010096971838 | 0.0 | 500 |
| expanded_deterministic | workspace_compact | 0.8152917367845266 | 0.5020432762783145 | 0.4588695606360659 | 0.545400190906527 | 0.0 | 500 |
| expanded_deterministic | workspace_full | 0.8649150372980527 | 0.4995288203774123 | 0.45827917600280166 | 0.5460273002531991 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_full | 0.8636103027541986 | 0.4988652342478872 | 0.45016270442649015 | 0.5439295753259511 | 0.0 | 500 |
| expanded_deterministic | workspace_late_late_single | 0.8307595042628559 | 0.5000306504148189 | 0.4557598141760493 | 0.5423835733611015 | 0.0 | 500 |
| expanded_deterministic | workspace_noise_single | 0.8307595042628559 | 0.4990222920559951 | 0.45858877928292285 | 0.5420851269559397 | 0.0 | 500 |
| high_quality_primary | baseline_output_confidence | 0.8251413499871154 | 0.4989214412393324 | 0.45879075654454227 | 0.5428962726046292 | 0.0 | 500 |
| high_quality_primary | combined_compact | 0.8700459292719528 | 0.49976957147837686 | 0.4522115020236164 | 0.545051386215155 | 0.0 | 500 |
| high_quality_primary | combined_full | 0.893774537296691 | 0.49943296903184725 | 0.4516605023419381 | 0.5424879113549893 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_full | 0.7730821118370192 | 0.5008203422716042 | 0.4571579936638826 | 0.545642024525928 | 0.0 | 500 |
| high_quality_primary | commitment_dynamics_single | 0.758396871352564 | 0.5005372906277 | 0.4563846993375877 | 0.5413771960406845 | 0.0 | 500 |
| high_quality_primary | layer_l33_diff | 0.5627108881175061 | 0.4986969850388807 | 0.4540302557184217 | 0.5414670840217671 | 0.004 | 500 |
| high_quality_primary | layer_l33_diff_in_full | 0.8779766867259857 | 0.49960714253232474 | 0.4595263828045657 | 0.5405500144002667 | 0.0 | 500 |
| high_quality_primary | layer_l33_full | 0.8599263312667687 | 0.500613269466887 | 0.4578129784299162 | 0.5477268042018463 | 0.0 | 500 |
| high_quality_primary | layer_l33_single | 0.8589016385987783 | 0.4994310894180777 | 0.46085901380909794 | 0.5399229206772673 | 0.0 | 500 |
| high_quality_primary | workspace_compact | 0.819917842688454 | 0.4992290915705386 | 0.456302845189553 | 0.5414793621439723 | 0.0 | 500 |
| high_quality_primary | workspace_full | 0.8712888996680359 | 0.5002754543663124 | 0.4558875111791545 | 0.5461912810174168 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_full | 0.8762971608737172 | 0.5000613239150535 | 0.4586563035273074 | 0.5392654348122659 | 0.0 | 500 |
| high_quality_primary | workspace_late_late_single | 0.8389625744645374 | 0.4983115490139607 | 0.45635529247699747 | 0.5378817207560898 | 0.0 | 500 |
| high_quality_primary | workspace_noise_single | 0.8389625744645374 | 0.5014275727213472 | 0.4562419093237938 | 0.5408443861696807 | 0.0 | 500 |
| primary_with_llm_judge | baseline_output_confidence | 0.8244243122045812 | 0.5002043721973094 | 0.46160397224578836 | 0.5419244637013695 | 0.0 | 500 |
| primary_with_llm_judge | combined_compact | 0.870024845473276 | 0.5001766755544782 | 0.4585427523936492 | 0.5441353320809599 | 0.0 | 500 |
| primary_with_llm_judge | combined_full | 0.8940189067991761 | 0.5015927826930069 | 0.4571133044479457 | 0.5433763331717366 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_full | 0.7734365531450733 | 0.49725589625499933 | 0.4508796661010786 | 0.5405772785116955 | 0.0 | 500 |
| primary_with_llm_judge | commitment_dynamics_single | 0.758835292691795 | 0.4998754635801721 | 0.4590118621985214 | 0.5441116228335958 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_diff | 0.5634044358259604 | 0.5003844685492668 | 0.4557523330505393 | 0.542983123257787 | 0.004 | 500 |
| primary_with_llm_judge | layer_l33_diff_in_full | 0.8774360683553508 | 0.5007401163495334 | 0.4562271239849715 | 0.5453392770573263 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_full | 0.8593170524784874 | 0.5000244637013695 | 0.4580998515331475 | 0.5406020482365773 | 0.0 | 500 |
| primary_with_llm_judge | layer_l33_single | 0.8589413404435826 | 0.5004134832141559 | 0.45591352563325654 | 0.5418722730578112 | 0.0 | 500 |
| primary_with_llm_judge | workspace_compact | 0.8198339595200581 | 0.5004303902557266 | 0.45357842988728636 | 0.5446764786086534 | 0.0 | 500 |
| primary_with_llm_judge | workspace_full | 0.8712913586231972 | 0.5013979093443218 | 0.456463610471458 | 0.5404642619076476 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_full | 0.8759938189310386 | 0.49832689976972483 | 0.45459982123378984 | 0.5403764695188462 | 0.0 | 500 |
| primary_with_llm_judge | workspace_late_late_single | 0.8390679917585747 | 0.4998011574354623 | 0.4576280147860865 | 0.5401545267240334 | 0.0 | 500 |
| primary_with_llm_judge | workspace_noise_single | 0.8390679917585747 | 0.499803938916495 | 0.4579090413283239 | 0.5418566688886195 | 0.0 | 500 |
| strict | baseline_output_confidence | 0.8103665814151747 | 0.4965099289570901 | 0.4149820971867008 | 0.5787736572890024 | 0.0 | 500 |
| strict | combined_compact | 0.905541346973572 | 0.4998549360613811 | 0.41383063370275647 | 0.5797971014492753 | 0.0 | 500 |
| strict | combined_full | 0.9186018755328218 | 0.4986401818698494 | 0.4173100312588804 | 0.5842733731173628 | 0.0 | 500 |
| strict | commitment_dynamics_full | 0.8431031543052003 | 0.5003765842568912 | 0.41632480818414325 | 0.57149133276499 | 0.0 | 500 |
| strict | commitment_dynamics_single | 0.8316908212560387 | 0.5009183063370275 | 0.4153296391020176 | 0.5805822676896845 | 0.0 | 500 |
| strict | layer_l33_diff | 0.6685080988917306 | 0.49934624609263994 | 0.41542369991474853 | 0.5781781756180733 | 0.0 | 500 |
| strict | layer_l33_diff_in_full | 0.9088377379937482 | 0.4981777095765842 | 0.4113037794828076 | 0.5820815572605854 | 0.0 | 500 |
| strict | layer_l33_full | 0.8828871838590507 | 0.501728172776357 | 0.4219889173060528 | 0.585668940039784 | 0.0 | 500 |
| strict | layer_l33_single | 0.889434498437056 | 0.4984617902813299 | 0.419974992895709 | 0.5832253481102585 | 0.0 | 500 |
| strict | workspace_compact | 0.8704290991759022 | 0.5004989371980676 | 0.4129406081273089 | 0.5853907360045467 | 0.0 | 500 |
| strict | workspace_full | 0.8908439897698209 | 0.49872422847399833 | 0.40739244103438477 | 0.5866570048309179 | 0.0 | 500 |
| strict | workspace_late_late_full | 0.9118840579710144 | 0.4988408070474567 | 0.40664961636828645 | 0.5858005115089513 | 0.0 | 500 |
| strict | workspace_late_late_single | 0.869337880079568 | 0.498605171923842 | 0.4170528559249787 | 0.5897019039499857 | 0.0 | 500 |
| strict | workspace_noise_single | 0.869337880079568 | 0.4985702756464905 | 0.41478715544188693 | 0.5822341574310883 | 0.0 | 500 |


## H.3 quadrant analysis

| quadrant | n | accuracy | wrong_rate | mean_confidence | mean_workspace_noise |
| --- | --- | --- | --- | --- | --- |
| high_confidence__clean_workspace | 210 | 0.2714285714285714 | 0.7285714285714285 | 0.7989319301786877 | 0.9067705981320996 |
| high_confidence__noisy_workspace | 595 | 0.047058823529411764 | 0.9529411764705882 | 0.748622484167083 | 2.439723975940474 |
| low_confidence__clean_workspace | 237 | 0.31645569620253167 | 0.6835443037974683 | 0.45358176139588097 | 0.9102399042847308 |
| low_confidence__noisy_workspace | 927 | 0.02696871628910464 | 0.9730312837108953 | 0.47964920289008134 | 2.6103246681347985 |


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
