import requests
from tenacity import retry, stop_after_attempt, wait_fixed

from services.auth import get_access_token
from utils.config import settings
from utils.logger import logger


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_offres(departement: str, type_contrat: str):
    """Récupère les offres d'emploi filtrées selon la config"""

    token = get_access_token()
    if token:
        print("🔑 Token obtenu :", token)
    else:
        print("⚠️ Impossible de récupérer le token.")

    headers = {"Authorization": f"Bearer {token}"}
    params = {"departement": departement,
              "typeContrat": type_contrat
              }

    logger.info(f"📡 Requête API : {params}")

    try:
        response = requests.get(settings.API_URL, headers=headers, params=params, timeout=settings.TIMEOUT)
        response.raise_for_status()
        offres = response.json().get("resultats", [])
        logger.info(f"✅ {len(offres)} offres récupérées.")
        return offres

    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Erreur API : {e}")
        return []
