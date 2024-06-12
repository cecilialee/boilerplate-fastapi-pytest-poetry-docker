"""Example configurations"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Load settings from Dotenv files
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI + Docker Boilerplate"


settings = Settings()
