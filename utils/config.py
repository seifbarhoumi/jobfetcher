from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    CLIENT_ID: str = Field(..., env="CLIENT_ID")
    CLIENT_SECRET: str = Field(..., env="CLIENT_SECRET")
    #AUTH_URL: str = Field("https://entreprise.francetravail.fr/partenaire/connect/oauth2/token")
    #AUTH_URL: str = Field("https://entreprise.francetravail.fr/connexion/oauth2/access_token")
    AUTH_URL: str = Field("https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Femployeur")
    API_URL: str = Field("https://api.francetravail.io/offresdemploi/v1/offres")
    API_SCOPE: str = Field("api_offresdemploiv2")
    DEPARTMENT: str = Field("07")
    CONTRACT_TYPE: str = Field("CDI")
    TIMEOUT: int = 10

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

settings = Settings()
