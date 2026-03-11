### LeadScrape Real Estate – v1.0 Milestones

#### Milestone 1 – Project & GitHub Setup
- **1.1 Create repo + initial commit**
  - Create GitHub repo `leadscrape-real-estate`.
  - Initialize venv, `.gitignore`, `requirements.txt`, `README.md`.
  - Add `proposal.md` and initial `README`.
- **1.2 Basic project skeleton**
  - Add `main.py`, `config.py`, `db.py`, `api_client.py`, `models.py`, `utils.py`.
  - `config.py` loads `.env` with RapidAPI credentials.

#### Milestone 2 – Database Schema & Helper Layer
- **2.1 Define SQLite schema**
  - In `db.py`, create `frbo_leads` table with schema from proposal.
  - Add `init_db()` to create table if missing.
- **2.2 DB access helpers**
  - Implement `upsert_property(record: dict)` (UPSERT on `property_id`).
  - Add connection/utility functions as needed.
- **2.3 Document database**
  - Update `README.md` with schema and how to initialize DB.

#### Milestone 3 – RapidAPI Client & JSON Parsing
- **3.1 API client**
  - In `api_client.py`, implement `fetch_listings(params: dict) -> dict`.
  - Use headers `X-RapidAPI-Key` and `X-RapidAPI-Host` from `.env`.
  - Handle non-200 responses and timeouts.
- **3.2 Explore JSON structure**
  - Make a sample request, inspect JSON to find `zpid`, address, price, owner info.
- **3.3 Parsing function**
  - Implement `parse_results(response_json) -> list[dict]` returning raw property dicts.
- **3.4 Document API usage**
  - Update `README.md` with how to get a RapidAPI key and example `.env`.

#### Milestone 4 – Data Normalization & Filtering
- **4.1 Normalization helpers**
  - In `utils.py`, implement `normalize_phone()` (E.164) and `normalize_price()` (int).
- **4.2 Business rules**
  - Implement `transform_record(raw) -> dict | None`:
    - 4+ beds, furnished keyword, For Rent By Owner.
    - Requires plausible owner name + phone.
- **4.3 Quick checks**
  - Add simple tests or scripts to validate normalization functions.

#### Milestone 5 – Main Pipeline Orchestration
- **5.1 Main script flow**
  - In `main.py`, wire together:
    - `init_db()`
    - `fetch_listings()` with correct params
    - `parse_results()` → `transform_record()` → `upsert_property()`
- **5.2 Progress feedback**
  - Add basic logging or a progress bar for processed listings.
- **5.3 Idempotency test**
  - Run `python main.py` multiple times to verify UPSERT behavior and `leads.db` contents.

#### Milestone 6 – Polish & Robustness for v1.0
- **6.1 Error handling & resilience**
  - Add retry/backoff on API failures and 2-second sleeps between calls.
- **6.2 Logging & configuration**
  - Replace ad-hoc prints with `logging` (optional).
  - Make key filters configurable via `config.py` or CLI flags.
- **6.3 Final documentation**
  - Update `README.md` with:
    - What v1.0 does.
    - Setup steps (clone, venv, install, `.env`, run).
    - Future work (Twilio v2.0, scheduling, dashboards).

#### Milestone 7 – GitHub Storytelling
- **7.1 Commit hygiene**
  - Use small, descriptive commits aligned with milestones.
- **7.2 Issues & Milestones**
  - Create a GitHub Milestone `v1.0 – LeadScrape pipeline` and related Issues.
- **7.3 Final check-in**
  - Optionally tag a `v1.0` release and polish repo description.

