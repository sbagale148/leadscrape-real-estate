### LeadScrape Real Estate

Automated, resilient data extraction pipeline that queries real estate APIs (via a Zillow wrapper on RapidAPI) for:

- **4+ bedroom** listings  
- **Furnished** properties  
- **For Rent By Owner** (FRBO/FSBO)

The pipeline sanitizes and normalizes the data, then stores it in a SQLite database for future automated outreach (e.g., Twilio SMS in v2.0).

---

### Project Structure (v1.0 Plan)

- `proposal.md` – High-level project proposal and requirements.
- `MILESTONES.md` – Implementation milestones and roadmap.
- `main.py` – Entry point; orchestrates the extraction pipeline.
- `config.py` – Configuration and environment loading (RapidAPI keys, query params).
- `db.py` – SQLite schema definition and data access helpers.
- `api_client.py` – RapidAPI client and raw JSON handling.
- `models.py` – Optional data models / typed structures for listings.
- `utils.py` – Normalization and utility functions (phone, price, etc.).

---

### Database (SQLite)

- Uses a single SQLite database file (default: `leads.db` in the project root).
- The main table is `frbo_leads` with columns defined in `proposal.md`.
- You can override the database file location by setting `DB_PATH` in your `.env`.

---

### Getting Started (Target)

1. Create and activate a virtual environment:
   - `python -m venv .venv`
   - Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Create a `.env` file with your RapidAPI credentials (see `proposal.md` for details).
4. Run the pipeline (once implemented):
   - `python main.py`

This repository is being built and documented as a real-world data engineering project by **@sbagale148**.

