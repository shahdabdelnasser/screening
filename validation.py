import numpy as np
import pandas as pd

def validate_dataframe(df: pd.DataFrame, expected_features: list):
    """
    Ensures:
    - correct features
    - no missing values
    - no infinite values
    """

    missing = set(expected_features) - set(df.columns)
    extra = set(df.columns) - set(expected_features)

    if missing:
        return False, {"error": f"Missing features: {list(missing)}"}

    # enforce strict ordering
    df = df.reindex(columns=expected_features)

    if df.isnull().values.any():
        return False, {"error": "Null values detected"}

    if np.isinf(df.values).any():
        return False, {"error": "Infinite values detected"}

    return True, df