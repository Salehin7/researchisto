import pandas as pd

from processor.cleaner import fill_missing_values


def test_fill_missing_values():

    df = pd.DataFrame({
        "Age": [20, 30, None, 40],
        "Salary": [30000, None, 50000, 60000]
    })

    result = fill_missing_values(df)

    assert result["Age"].isna().sum() == 0
    assert result["Salary"].isna().sum() == 0