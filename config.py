from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os


@dataclass
class Settings:
    rapidapi_key: str
    rapidapi_host: str
    db_path: Path


def load_settings() -> Settings:
    project_root = Path(__file__).resolve().parent
    env_path = project_root / ".env"
    load_dotenv(env_path)

    key = os.getenv("RAPIDAPI_KEY", "")
    host = os.getenv("RAPIDAPI_HOST", "")
    db_path_env = os.getenv("DB_PATH")
    db_path = Path(db_path_env) if db_path_env else project_root / "leads.db"

    return Settings(rapidapi_key=key, rapidapi_host=host, db_path=db_path)

