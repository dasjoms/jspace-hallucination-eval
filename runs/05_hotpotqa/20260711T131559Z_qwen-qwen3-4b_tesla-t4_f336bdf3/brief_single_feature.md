## Headline (single-feature, parsimonious)

- `workspace_noise_score` (1 feature, late-layer mean entropy): **AUC 0.704**
  vs `baseline_output_confidence` (3 features): **AUC 0.660** → delta **+0.045**
- 95% bootstrap CI for single-feature: [0.673, 0.734]
- Baseline CI upper bound: 0.694
- **CI strictly above baseline:** False (CI overlaps baseline)
