## Headline (single-feature, parsimonious)

- `workspace_noise_score` (1 feature, late-layer mean entropy): **AUC 0.718**
  vs `baseline_output_confidence` (3 features): **AUC 0.718** → delta **+0.001**
- 95% bootstrap CI for single-feature: [0.691, 0.746]
- Baseline CI upper bound: 0.747
- **CI strictly above baseline:** False (CI overlaps baseline)
