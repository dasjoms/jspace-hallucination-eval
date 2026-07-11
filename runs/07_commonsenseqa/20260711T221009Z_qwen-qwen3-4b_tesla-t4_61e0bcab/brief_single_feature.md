## Headline (single-feature, parsimonious)

- `workspace_noise_score` (1 feature, late-layer mean entropy): **AUC 0.589**
  vs `baseline_output_confidence` (3 features): **AUC 0.844** → delta **-0.256**
- 95% bootstrap CI for single-feature: [0.551, 0.624]
- Baseline CI upper bound: 0.867
- **CI strictly above baseline:** False (CI overlaps baseline)
