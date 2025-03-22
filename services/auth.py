import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from utils.config import settings
from utils.logger import logger


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=4))
def get_access_token():
    """Récupère le token d'accès OAuth2 depuis l'API de France Travail avec gestion des erreurs."""
    data = {
        "grant_type": "client_credentials",
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
        "scope": settings.API_SCOPE
    }
    print("🔍 Données envoyées :", data)

    try:
        response = requests.post(settings.AUTH_URL, data=data, timeout=10)
        response.raise_for_status()  # Lève une exception si code 4xx ou 5xx

        json_response = response.json()
        access_token = json_response.get("access_token")

        if not access_token:
            logger.error("⚠️ Réponse reçue, mais le token est absent !")
            logger.debug(f"🔍 Réponse brute : {json_response}")
            raise ValueError("Le token d'accès est introuvable dans la réponse.")

        logger.info("✅ Token récupéré avec succès.")
        return access_token

    except requests.exceptions.HTTPError as e:
        status_code = response.status_code
        errors = {
            400: "❌ Erreur 400 : Requête invalide. Vérifiez les paramètres envoyés.",
            401: "❌ Erreur 401 : Identifiants invalides. Vérifiez CLIENT_ID et CLIENT_SECRET.",
            403: "❌ Erreur 403 : Accès refusé. Vérifiez les permissions de votre application.",
            429: f"⚠️ Erreur 429 : Trop de requêtes. Réessayez après {response.headers.get('Retry-After', 'inconnu')} secondes.",
            500: "❌ Erreur 500 : Problème serveur sur l'API de France Travail."
        }
        logger.error(errors.get(status_code, f"❌ Erreur {status_code} : Impossible d'obtenir le token."))
        logger.debug(f"🔍 Réponse brute : {response.text[:500]}")
        raise

    except requests.exceptions.ConnectionError:
        logger.critical("❌ Erreur : Impossible de se connecter à l'API. Vérifiez votre connexion internet.")
        raise
    except requests.exceptions.Timeout:
        logger.critical("❌ Erreur : Temps de réponse trop long. L'API ne répond pas.")
        raise
    except requests.exceptions.RequestException as e:
        logger.critical(f"❌ Erreur inattendue : {e}")
        raise
