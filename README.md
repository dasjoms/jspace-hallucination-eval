# Evaluating J-Space Entropy as a Hallucination Predictor in Qwen3-4B

> **TL;DR:** We evaluate the predictive utility of "workspace noise" (J-space entropy) against output logprobs for detecting incorrect answers in Qwen3-4B across seven distinct datasets. Across fact-retrieval tasks (TriviaQA, PopQA, NQ-Open, HotpotQA), workspace noise can improve routing precision at low escalation budgets by intercepting high-confidence confabulations, though this edge is often modest or statistically indistinguishable from baseline logprobs. However, we document three specific boundary failures where the signal breaks down: (1) on TruthfulQA, the metric fails to detect errors on adversarially constructed misconceptions; (2) on GSM8K (math), the baseline entropy for correct answers shifts significantly upwards, breaking absolute thresholds; and (3) on CommonSenseQA, the multiple-choice format artificially compresses entropy, rendering the signal weaker than standard logprobs.

**Attribution:** This project builds upon the "Global Workspace in Language Models" theory and the Jacobian Lens mathematical framework introduced by Anthropic (July 6, 2026; https://transformer-circuits.pub/2026/workspace/index.html). It extends the initial open-source hypothesis by `solarkyle` (https://github.com/solarkyle/jspace), which linked workspace noise to hallucination prediction, by rigorously stress-testing the zero-shot transferability and format limitations of the metric.

---

## 1. Methodology

*   **Model:** `Qwen/Qwen3-4B`
*   **Extraction Tool:** Jacobian Lens (mapping residual streams to the unembedding vocabulary).
*   **Pipeline:** Extracts workspace entropy at late-layer checkpoints (Layer 34) prior to answer generation. Correctness is adjudicated using exact-match aliases and a fallback LLM Judge (`primary_with_llm_judge` regime).
*   **Threshold Protocol:** An absolute threshold for "High Confidence" (Output Prob >= `0.623`) and "High Workspace Noise" (Entropy >= `1.583`) was established on the baseline TriviaQA dev split. This exact threshold was applied unaltered to all subsequent datasets to test distribution shift and threshold stability.

## 2. The Dataset Sweep

We evaluated ~11,400 examples across seven distributions to isolate specific cognitive tasks:
1.  **TriviaQA:** Baseline closed-book factual recall.
2.  **PopQA:** Factual recall for low-frequency, long-tail entities.
3.  **NQ-Open:** Factual recall on organic search queries.
4.  **TruthfulQA:** Adversarial prompts targeting common human misconceptions.
5.  **HotpotQA (Distractor):** Multi-hop factual reasoning.
6.  **GSM8K:** Mathematical multi-step derivation.
7.  **CommonSenseQA:** Multiple-choice general reasoning.

---

## 3. Observational Findings

### Finding 1: Routing Utility on Fact Retrieval
In fact-retrieval datasets (PopQA, NQ-Open, HotpotQA), filtering high-confidence predictions by workspace noise can yield higher precision for identifying incorrect answers than output logprobs alone at tight routing budgets (5%-10%). However, on the primary calibration set (TriviaQA), global AUC separation was highly significant (0.755 vs 0.630) despite the lack of a formal routing table.

*   **Data Highlight (PopQA Routing):**

|   Budget (Escalation %) |   Recall (Confidence) |   Precision (Confidence) |   Recall (Workspace Noise) |   Precision (Workspace Noise) |
|------------------------:|----------------------:|-------------------------:|---------------------------:|------------------------------:|
|                    5.0% |                  4.9% |                    87.5% |                       5.6% |                        **100.0%** |
|                   10.0% |                 10.3% |                    92.5% |                      10.8% |                         **97.5%** |
|                   20.0% |                 20.1% |                    90.1% |                      21.8% |                         **97.5%** |
|                   30.0% |                 30.3% |                    90.5% |                      32.1% |                         **95.9%** |

*Table: PopQA routing performance. Note: PopQA has an inherently massive base error rate (~90.6%). At a 5% budget, output confidence actually performed worse than chance (87.5% precision). Workspace noise restored precision to 100% (on a small sample of 40 queries routed from the high-confidence subset), demonstrating utility in extreme low-frequency fact retrieval.*

*   **Limitation:** Workspace noise does not consistently outperform output logprobs as a *global* predictor of correctness (global ROC-AUC bounds frequently overlap). Its primary utility is concentrated in resolving the specific "high output confidence / incorrect" quadrant.

### Finding 2: Signal Failure on Adversarial Datasets (TruthfulQA)
The predictive utility of workspace noise collapsed entirely on the TruthfulQA dataset (Workspace ROC-AUC ~0.617 vs Baseline Confidence ROC-AUC ~0.743).

*   **Data Highlight (TruthfulQA Blindspot):**

| | **Clean Workspace (Low Noise)** | **Noisy Workspace (High Noise)** |
| :--- | :---: | :---: |
| **High Output Confidence** | **84.9% Error Rate** *(The Blindspot)* | 91.5% Error Rate |
| **Low Output Confidence** | 89.5% Error Rate | 97.2% Error Rate |

*Table: TruthfulQA Error Rates by Quadrant. In fact-retrieval datasets, the top-left quadrant is the "safest" operating point (lowest relative error rate). In TruthfulQA, the model is wrong 84.9% of the time even when highly confident and internally "clean", demonstrating that internalized myths bypass J-space noise detection entirely.*

*   **Conclusion:** The workspace noise metric fails to identify incorrect answers when the prompt is designed to elicit widely represented training-data misconceptions. Internalized falsehoods produce clean, converged internal representations.

### Finding 3: Threshold Instability Across Task Formats (GSM8K & CommonSenseQA)
The absolute entropy threshold established on factual recall (TriviaQA) did not transfer to mathematical derivation or multiple-choice formats, demonstrating severe distribution shift.

*   **Computation (GSM8K):** On GSM8K, the mean noise score for *correct* answers shifted to **1.636**, exceeding the TriviaQA-derived threshold (1.583) used to flag errors. Doing math inherently raises the baseline entropy of the internal workspace.
*   **Format Compression (CommonSenseQA):** On CommonSenseQA, the multiple-choice format (A, B, C, D, E) correlated with a severely compressed vocabulary distribution. The noise signal became significantly weaker globally than baseline output confidence (Workspace AUC 0.589 vs Confidence AUC 0.844).
*   **Conclusion:** The baseline entropy of the model's internal representations shifts significantly depending on the task type (memory retrieval vs. computation) and the constraints of the prompt format (open-ended vs. multiple-choice).

### Finding 4: Layer 34 Final Commitment
Across all seven datasets, the separation gap between correct and incorrect answers (measured by Cohen's d) peaked maximally at the final layer (**Layer 34**). While our operational metric (`workspace_noise_score`) averaged entropy across the late-late band (Layers 30-34), the maximum separation gap was consistently isolated to the absolute entropy level at the final representation layer (Layer 34) immediately prior to output generation.

---

## 4. Methodological Limitations

*   **Top-K Entropy Approximation:** Entropy calculations were performed over the top-50 tokens of the vocabulary projection, not the full vocabulary. This represents "effective concepts" (concentration among top candidates) rather than true Shannon entropy.
*   **Confidence Baseline Definition:** Output confidence was measured via the probability of the first content token. For heavily generative tasks (e.g., GSM8K), this token often reflects prompt-continuation fluency rather than answer certainty.
*   **Self-Judging Circularity:** The `primary_with_llm_judge` regime utilized Qwen3-4B to adjudicate ambiguous answers generated by Qwen3-4B. While mitigated by strict confidence requirements, this introduces potential correlated error risks.
*   **Sequence & Generation Truncation:** Due to hardware constraints, prompt sequences were restricted to 512 tokens. Furthermore, nearly every generation mechanically hit the `max_new_tokens` limit. This introduces a dual selection bias toward shorter reasoning tasks and makes automated answer parsing/labeling more fragile.
*   **Single Model Evaluation:** All observations are currently limited to the Qwen3-4B architecture. Cross-model validation is required to determine if these layer dynamics and thresholds generalize to other transformer families or larger parameter counts.

---


## 5. Artifacts and Reproducibility

The core execution environment is provided in `experiment_pipeline.ipynb`. 
All underlying raw data, metrics, routing tables, and label judge records have been released for complete transparency. 

### Data Visualization
The repository contains the artifact folders for all seven dataset runs. Inside each artifact folder, you can navigate to the `plots/` directory to view the auto-generated graphical representations of the data, including:
*   `confidence_workspace_quadrants.png`: Visualizes the "Clean-Wrong" vs "Noisy-Wrong" error distributions.
*   `roc_curves.png`: Compares the predictive power of J-space features against output logprobs.
*   `entropy_vs_correctness.png`: Shows the absolute shift in baseline entropy across different datasets.

**License:** The codebase is released under the MIT License. Dataset artifacts and aggregate metrics are released under CC-BY 4.0.
