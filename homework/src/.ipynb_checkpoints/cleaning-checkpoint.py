# src/cleaning.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df: pd.DataFrame, cols=None) -> pd.DataFrame:
    """
    Fill missing numeric values with median.
    If cols is None, apply to all numeric columns.
    """
    df_copy = df.copy()
    cols = cols or df_copy.select_dtypes(include="number").columns
    for col in cols:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy

def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Drop columns with missing fraction above threshold.
    Default: drop if >50% missing.
    """
    df_copy = df.copy()
    limit = int((1 - threshold) * len(df_copy))
    return df_copy.dropna(axis=1, thresh=limit)

def normalize_data(df: pd.DataFrame, cols=None) -> pd.DataFrame:
    """
    Scale selected numeric columns to [0,1].
    """
    df_copy = df.copy()
    cols = cols or df_copy.select_dtypes(include="number").columns
    scaler = MinMaxScaler()
    df_copy[cols] = scaler.fit_transform(df_copy[cols])
    return df_copy