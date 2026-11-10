
"""
Healthcare Data Analytics Project
Module: Data Transformation

Purpose:
Clean, validate and transform patient records.
"""

import logging
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

REQUIRED_COLUMNS = [
    "patient_id",
    "age",
    "gender",
    "department",
    "visit_date",
    "diagnosis",
    "treatment_cost",
    "admission_status"
]


def transform_data(df):
    """
    Clean and transform healthcare patient data.
    """

    logging.info("Starting data transformation")

    df = df.copy()

    # Check required columns
    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove records without patient IDs
    df = df.dropna(subset=["patient_id"])

    # Convert numeric columns
    df["age"] = pd.to_numeric(
        df["age"], errors="coerce"
    )

    df["treatment_cost"] = pd.to_numeric(
        df["treatment_cost"], errors="coerce"
    )

    # Convert dates
    df["visit_date"] = pd.to_datetime(
        df["visit_date"], errors="coerce"
    )

    # Remove invalid values
    df = df.dropna(
        subset=["age", "treatment_cost", "visit_date"]
    )

    # Validate age and treatment cost
    df = df[
        (df["age"].between(0, 120)) &
        (df["treatment_cost"] >= 0)
    ]

    # Standardize text columns
    text_columns = [
        "gender",
        "department",
        "diagnosis",
        "admission_status"
    ]

    for col in text_columns:
        df[col] = df[col].astype("string").str.strip().str.title()

    # Create additional analytical column
    df["visit_month"] = df["visit_date"].dt.to_period("M").astype(str)

    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 18, 35, 50, 65, 120],
        labels=[
            "0-18",
            "19-35",
            "36-50",
            "51-65",
            "Above 65"
        ],
        include_lowest=True
    )

    df = df.reset_index(drop=True)

    logging.info("Data transformation completed")
    logging.info("Clean records: %d", len(df))

    return df


if __name__ == "__main__":
    from extract import extract_data

    raw_data = extract_data()
    clean_data = transform_data(raw_data)

    print(clean_data.head())
