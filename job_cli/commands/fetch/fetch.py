import typer

from services.data_handler import process_and_store_data
from services.offres import get_offres
from utils.config import settings
from utils.logger import logger


def fetch_job(
        departement: str = typer.Option(settings.DEPARTMENT, "--departement", "-d", help="Code du département (ex: 75, 07)"),
        type_contrat: str = typer.Option(settings.CONTRACT_TYPE, "--type-contrat", "-t", help="Type de contrat (CDI, CDD, INTERIM)"),
        export_csv: bool = typer.Option(False, "--export-csv", help="Exporter les offres en CSV")
):
    """Exécute le script principal."""
    logger.info(f"🚀 Démarrage du script avec filtre: Département={departement}, Type Contrat={type_contrat}")

    offres = get_offres(departement=departement, type_contrat=type_contrat)

    if not offres:
        logger.warning("Aucune offre trouvée.")
        return

    process_and_store_data(offres, departement, type_contrat, export_csv)

    logger.info("🎯 Script terminé avec succès.")
