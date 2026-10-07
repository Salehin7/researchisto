import pandas as pd


def fill_missing_values(df, strategy="median"):
    """
    Fill missing numeric values in a DataFrame.

    Supported strategies:
    - median
    - mean
    - zero
    """

    cleaned_df = df.copy()

    numeric_columns = cleaned_df.select_dtypes(
        include=["number"]
    ).columns

    for column in numeric_columns:

        if strategy == "median":
            value = cleaned_df[column].median()

        elif strategy == "mean":
            value = cleaned_df[column].mean()

        elif strategy == "zero":
            value = 0

        else:
            raise ValueError(
                f"Unsupported strategy: {strategy}"
            )

        cleaned_df[column] = cleaned_df[column].fillna(value)

    return cleaned_df