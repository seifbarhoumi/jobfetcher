import csv
import numpy as np
from utils.logger import logger

def save_csv(filename, data, headers):
    """Save data to a CSV file using the built-in csv module."""
    try:
        # 🔍 Convertir tous les éléments en chaînes de caractères
        clean_data = [[str(item) if not isinstance(item, (list, dict, np.ndarray)) else str(item.tolist()) for item in row] for row in data]

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
            writer.writerows(clean_data)

        logger.info(f"✅ CSV file created successfully: {filename}")

    except Exception as e:
        logger.error(f"❌ Error while saving {filename}: {e}")