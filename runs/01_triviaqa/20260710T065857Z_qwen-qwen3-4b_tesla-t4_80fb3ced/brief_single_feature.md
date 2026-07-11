## Headline (single-feature, parsimonious)

- `workspace_noise_score` (1 feature, late-layer mean entropy): **AUC 0.755**
  vs `baseline_output_confidence` (3 features): **AUC 0.630** → delta **+0.125**
- 95% bootstrap CI for single-feature: [0.734, 0.777]
- Baseline CI upper bound: 0.655
- **CI strictly above baseline:** True (statistically distinguishable at 95%)
