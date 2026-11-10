
"""
Healthcare Data Analytics Project
Module: Data Loading

Purpose:
Save transformed patient data into CSV format.
"""

import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "cleaned_patients.csv"


def load_data(df, output_file=OUTPUT_FILE):
    """
    Load transformed data into a CSV file.
    """

    logging.info("Starting healthcare data loading")

    if df.empty:
        raise ValueError("No data available to load")

    try:
        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_csv(output_file, index=False)

        logging.info("Data loaded successfully")
        logging.info("Output file: %s", output_file)
        logging.info("Total records loaded: %d", len(df))

        return output_file

    except Exception:
        logging.exception("Data loading failed")
        raise


if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    raw_data = extract_data()
    clean_data = transform_data(raw_data)
    load_data(clean_data)
