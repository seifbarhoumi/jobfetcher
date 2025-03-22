from utils.config import settings
from dotenv import load_dotenv
import os

load_dotenv()
def test_config():
    print("CLIENT_ID:", os.getenv("CLIENT_ID"))
    assert isinstance(settings.CLIENT_ID, str) and settings.CLIENT_ID != ""
    assert isinstance(settings.CLIENT_SECRET, str) and settings.CLIENT_SECRET != ""
    assert settings.AUTH_URL.startswith("https")
    assert settings.API_URL.startswith("https")
    assert settings.DEPARTMENT == "07"
    assert settings.CONTRACT_TYPE == "CDI"
    assert settings.TIMEOUT > 0
