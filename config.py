from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os


@dataclass
class Settings:
    rapidapi_key: str
    rapidapi_host: str


def load_settings() -> Settings:
    project_root = Path(__file__).resolve().parent
    env_path = project_root / ".env"
    load_dotenv(env_path)

    key = os.getenv("RAPIDAPI_KEY", "")
    host = os.getenv("RAPIDAPI_HOST", "")

    return Settings(rapidapi_key=key, rapidapi_host=host)

