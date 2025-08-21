## Data Preprocessing

This stage focuses on preparing raw ingested data for analysis.

- **Cleaning Functions** (in `src/cleaning.py`):
  - `fill_missing_median()` → replaces missing numeric values with the column median.
  - `drop_missing()` → removes columns with more than 50% missing values (threshold configurable).
  - `normalize_data()` → scales numeric features to the [0,1] range for comparability.

- **Notebook**: `notebooks/hw06_data_preprocessing.ipynb`
  - Loads the latest raw dataset from `data/raw/`
  - Applies cleaning pipeline
  - Saves cleaned output to `data/processed/cleaned_<timestamp>.csv`
  - Compares before vs. after (shapes, missing values, dtypes)

- **Assumptions & Risks**:
  - Median imputation assumes distributions aren’t heavily skewed.
  - Dropping columns may remove useful signals if missingness is not random.
  - Normalization assumes continuous numeric features.