from dataclasses import dataclass
from pathlib import Path
import sqlite3


@dataclass
class DbSettings:
    db_path: Path


def get_connection(settings: DbSettings) -> sqlite3.Connection:
    return sqlite3.connect(settings.db_path)


def init_db(settings) -> None:
    db_settings = DbSettings(db_path=Path("leads.db"))
    with get_connection(db_settings) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS frbo_leads (
                property_id TEXT PRIMARY KEY,
                address TEXT NOT NULL,
                price INTEGER NOT NULL,
                bedrooms INTEGER NOT NULL,
                owner_name TEXT,
                owner_phone TEXT,
                listing_url TEXT NOT NULL,
                status TEXT DEFAULT 'new',
                extracted_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        conn.commit()

