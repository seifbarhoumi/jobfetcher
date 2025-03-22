from utils.csv_writer import save_csv
from utils.logger import logger


def process_and_store_data(offres, export_csv):
    """Transforme et stocke les données des offres."""

    offres_data = [[o.get("id"), o.get("titre", "N/A"), o.get("salaire", {}).get("libelle", "N/A")] for o in offres]
    entreprises_data = [[o.get("id"), o.get("entreprise", {}).get("nom", "N/A")] for o in offres]
    competences_data = [[o.get("id"), c.get("libelle", "N/A")] for o in offres for c in o.get("competences", [])]

    logger.info("📊 Transformation des données terminée.")

    if export_csv:
        save_csv("offres_d_emploi.csv", offres_data, ["ID", "Titre", "Salaire"])
        save_csv("entreprises.csv", entreprises_data, ["Offre_ID", "Entreprise"])
        save_csv("competences.csv", competences_data, ["Offre_ID", "Compétence"])
        logger.info("✅ Données exportées en CSV.")

    logger.info("📂 Stockage des données terminé.")
