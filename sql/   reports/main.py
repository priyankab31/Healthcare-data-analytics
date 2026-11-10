
"""
Healthcare Data Analytics Project
Main ETL Pipeline

Author: Priya Bagade

Description:
Orchestrates healthcare patient data extraction,
transformation and loading.
"""

import logging

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    try:
        logging.info("===================================")
        logging.info("HEALTHCARE ETL PIPELINE STARTED")
        logging.info("===================================")

        # STEP 1: Extract
        logging.info("STEP 1: Extracting patient data")

        raw_data = extract_data()

        logging.info(
            "Extracted records: %d", len(raw_data)
        )

        # STEP 2: Transform
        logging.info("STEP 2: Transforming patient data")

        clean_data = transform_data(raw_data)

        logging.info(
            "Transformed records: %d", len(clean_data)
        )

        # STEP 3: Load
        logging.info("STEP 3: Loading processed data")

        output_file = load_data(clean_data)

        logging.info("Output generated: %s", output_file)

        logging.info("===================================")
        logging.info("ETL PIPELINE COMPLETED SUCCESSFULLY")
        logging.info("===================================")

    except Exception:
        logging.exception("Healthcare ETL pipeline failed")
        raise


if __name__ == "__main__":
    main()
