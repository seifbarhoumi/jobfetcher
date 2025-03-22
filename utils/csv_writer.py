import pandas as pd
from utils.logger import logger


def save_csv(filename, data, headers):
    """Save data to a CSV file using pandas."""
    try:
        df = pd.DataFrame(data, columns=headers)
        df.to_csv(filename, index=False, encoding="utf-8")

        logger.info(f"✅ CSV file created successfully: {filename}")

    except Exception as e:
        logger.error(f"❌ Error while saving {filename}: {e}")
