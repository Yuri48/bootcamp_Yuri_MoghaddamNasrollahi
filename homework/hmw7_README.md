# Stage 07 — Outliers + Risk Assumptions

## What I did
- Implemented reusable functions for outlier detection: 
  - `detect_outliers_iqr(series, k=1.5)`
  - `detect_outliers_zscore(series, threshold=3.0)`
  - (Stretch) `winsorize_series(series, lower=0.05, upper=0.95)`
- Applied IQR and Z-score to the `y` column and created boolean flags (`is_outlier_iqr`, `is_outlier_z`).
- Ran sensitivity analysis:
  - Compared regression slope/intercept/R²/MAE/RMSE with **all data**, **IQR-filtered**, and **winsorized**.
- Added a reflection section in the notebook discussing:
  - Which methods/thresholds were chosen and why
  - Assumptions behind each method
  - Observed impacts on results
  - Risks if assumptions are wrong

## Outputs
- Notebook: `notebooks/stage07_outliers-risk-assumptions_homework-starter.ipynb`
- Figures: saved in `deliverables/images/`
- Processed comparison tables: saved in `data/processed/`

## Key Takeaways
- Outliers inflated error and reduced R² in regression.
- Filtering or winsorizing improved fit while only slightly shifting coefficients.
- Median remained stable, but mean and variance were highly sensitive.
- Documented risks around misclassifying “true” structural points as noise.
