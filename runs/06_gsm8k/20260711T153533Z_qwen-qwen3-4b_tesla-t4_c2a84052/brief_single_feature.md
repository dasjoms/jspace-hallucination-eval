## Headline (single-feature, parsimonious)

- `workspace_noise_score` (1 feature, late-layer mean entropy): **AUC 0.744**
  vs `baseline_output_confidence` (3 features): **AUC 0.805** → delta **-0.062**
- 95% bootstrap CI for single-feature: [0.714, 0.775]
- Baseline CI upper bound: 0.836
- **CI strictly above baseline:** False (CI overlaps baseline)
