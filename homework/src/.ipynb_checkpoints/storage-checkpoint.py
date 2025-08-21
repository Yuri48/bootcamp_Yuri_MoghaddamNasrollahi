# src/storage.py
import os
from typing import Optional
import pandas as pd

def _ensure_parent(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

def write_df(df: pd.DataFrame, path: str) -> None:
    """
    Save a DataFrame based on file suffix (.csv or .parquet).
    Creates parent directories if needed.
    """
    _ensure_parent(path)
    suffix = os.path.splitext(path)[1].lower()
    if suffix == ".csv":
        df.to_csv(path, index=False)
    elif suffix == ".parquet":
        try:
            df.to_parquet(path, index=False)  # requires pyarrow
        except Exception as e:
            raise RuntimeError("Parquet write failed. Is 'pyarrow' installed?") from e
    else:
        raise ValueError(f"Unsupported file type: {suffix}")

def read_df(path: str) -> pd.DataFrame:
    """
    Load a DataFrame based on file suffix (.csv or .parquet).
    """
    suffix = os.path.splitext(path)[1].lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    elif suffix == ".parquet":
        try:
            return pd.read_parquet(path)
        except Exception as e:
            raise RuntimeError("Parquet read failed. Is 'pyarrow' installed?") from e
    else:
        raise ValueError(f"Unsupported file type: {suffix}")