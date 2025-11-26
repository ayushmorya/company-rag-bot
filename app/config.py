from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Google Gemini
    gemini_api_key: str

    # Models
    gemini_chat_model: str = "gemini-2.5-pro"
    gemini_embedding_model: str = "models/text-embedding-004"

    # Paths
    data_dir: Path = Path("data")
    vectordb_dir: Path = Path("data") / "chroma_db"

    # Tell Pydantic where to read env variables from
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    # ensure directories exist
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    settings.vectordb_dir.mkdir(parents=True, exist_ok=True)
    return settings
