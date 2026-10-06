import pandas as pd


def analyze_dataset(file_path):
    df = pd.read_csv(file_path)

    columns = []
    issues = []

    # Analyze each column
    for column in df.columns:

        missing_values = int(df[column].isnull().sum())
        unique_values = int(df[column].nunique())
        data_type = str(df[column].dtype)

        column_info = {
            "name": column,
            "data_type": data_type,
            "missing_values": missing_values,
            "unique_values": unique_values,
        }

        columns.append(column_info)

        # Check for missing values
        if missing_values > 0:
            issues.append({
                "type": "missing_values",
                "column": column,
                "count": missing_values,
                "message": f"{column} contains {missing_values} missing values."
            })

    # Check for duplicate rows
    duplicate_rows = int(df.duplicated().sum())

    if duplicate_rows > 0:
        issues.append({
            "type": "duplicate_rows",
            "column": None,
            "count": duplicate_rows,
            "message": f"The dataset contains {duplicate_rows} duplicate rows."
        })

    result = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": duplicate_rows,
        "column_analysis": columns,
        "issues": issues,
    }

    return result