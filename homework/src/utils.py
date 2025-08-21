from typing import Dict, Any
import pandas as pd

def get_summary_stats(df: pd.DataFrame,
                      group_col: str = "category",
                      value_col: str = "value") -> Dict[str, Any]:
    """
    Return summary stats:
      - describe() for numeric columns (handles old/new pandas versions)
      - groupby aggregations for mean, sum, count
    """
    try:
        desc = df.describe(numeric_only=True)
    except TypeError:
        desc = df.select_dtypes(include="number").describe()

    group = (
        df.groupby(group_col)[value_col]
          .agg(mean_value="mean", sum_value="sum", count="size")
          .reset_index()
    )
    return {"describe": desc, "group": group}