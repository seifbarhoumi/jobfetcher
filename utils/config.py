from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    CLIENT_ID: str = Field(..., env="CLIENT_ID")
    CLIENT_SECRET: str = Field(..., env="CLIENT_SECRET")
    AUTH_URL: str = Field("https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=/partenaire")
    API_URL: str = Field("https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search")
    API_SCOPE: str = Field("api_offresdemploiv2 o2dsoffre")
    DEPARTMENT: str = Field("69") #01 02 03 ... 101
    CONTRACT_TYPE: str = Field("CDI") #CDI|CDD|MIS
    TIMEOUT: int = 10

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

settings = Settings()

