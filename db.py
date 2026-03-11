from pathlib import Path
import sqlite3

from config import Settings

def get_connection(settings: Settings) -> sqlite3.Connection:
    db_path = Path(settings.db_path)
    return sqlite3.connect(db_path)


def init_db(settings) -> None:
    with get_connection(settings) as conn:
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


def upsert_property(settings: Settings, record: dict) -> None:
    """
    Insert a property row or update it if the property_id already exists.
    Expects keys matching the frbo_leads schema.
    """
    with get_connection(settings) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO frbo_leads (
                property_id,
                address,
                price,
                bedrooms,
                owner_name,
                owner_phone,
                listing_url,
                status
            )
            VALUES (
                :property_id,
                :address,
                :price,
                :bedrooms,
                :owner_name,
                :owner_phone,
                :listing_url,
                COALESCE(:status, 'new')
            )
            ON CONFLICT(property_id) DO UPDATE SET
                address = excluded.address,
                price = excluded.price,
                bedrooms = excluded.bedrooms,
                owner_name = excluded.owner_name,
                owner_phone = excluded.owner_phone,
                listing_url = excluded.listing_url,
                status = COALESCE(excluded.status, frbo_leads.status),
                extracted_at = CURRENT_TIMESTAMP;
            """,
            record,
        )
        conn.commit()

