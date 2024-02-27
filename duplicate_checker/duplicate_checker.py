import pandas as pd
from typing import List, Dict, Any


def count_and_sample_duplicates_by_columns(
    df: pd.DataFrame, columns: List[str]
) -> Dict[str, Any]:
    """
    Counts and samples duplicates in a DataFrame based on specified columns.

    Parameters:
    - df (pd.DataFrame): The DataFrame to check for duplicates.
    - columns (List[str]): The list of columns to consider for identifying duplicates.

    Returns:
    - Dict[str, Any]: A dictionary containing:
        - 'count': The number of duplicate cases found (int).
        - 'samples': A DataFrame with the count of duplicate rows based on the specified columns (pd.DataFrame).
    """
    if df.empty or not all(col in df.columns for col in columns):
        return {
            "count": 0,
            "samples": pd.DataFrame(columns=columns + ["number_of_duplicates"]),
        }

    duplicate_rows = df[df.duplicated(subset=columns, keep=False)]
    duplicate_counts = (
        duplicate_rows.groupby(columns).size().reset_index(name="number_of_duplicates")
    )

    result = {
        "count": duplicate_counts["number_of_duplicates"].sum(),
        "samples": duplicate_counts,
    }

    return result
