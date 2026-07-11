## Headline (single-feature, parsimonious)

- `workspace_noise_score` (1 feature, late-layer mean entropy): **AUC 0.839**
  vs `baseline_output_confidence` (3 features): **AUC 0.824** → delta **+0.015**
- 95% bootstrap CI for single-feature: [0.807, 0.869]
- Baseline CI upper bound: 0.850
- **CI strictly above baseline:** False (CI overlaps baseline)
