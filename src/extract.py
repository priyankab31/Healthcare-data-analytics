
"""
Healthcare Data Analytics Project
Module: Data Extraction

Purpose:
Extract patient records from a CSV source.
"""

import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "data" / "raw" / "patients.csv"


def extract_data(file_path=RAW_FILE):
    """
    Extract patient data from CSV file.
    """

    logging.info("Starting healthcare data extraction")

    try:
        if not file_path.exists():
            raise FileNotFoundError(
                f"Source file not found: {file_path}"
            )

        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError("Source file contains no records")

        logging.info("Data extraction completed successfully")
        logging.info("Total records extracted: %d", len(df))

        return df

    except Exception:
        logging.exception("Data extraction failed")
        raise


if __name__ == "__main__":
    patient_data = extract_data()
    print(patient_data.head())

