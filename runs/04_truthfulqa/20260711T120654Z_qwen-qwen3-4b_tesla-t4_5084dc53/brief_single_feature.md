## Headline (single-feature, parsimonious)

- `workspace_noise_score` (1 feature, late-layer mean entropy): **AUC 0.617**
  vs `baseline_output_confidence` (3 features): **AUC 0.743** → delta **-0.126**
- 95% bootstrap CI for single-feature: [0.534, 0.691]
- Baseline CI upper bound: 0.803
- **CI strictly above baseline:** False (CI overlaps baseline)
