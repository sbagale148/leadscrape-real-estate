### Project Proposal: LeadScrape Real Estate (v1.0)

#### Objective
Build an automated, resilient data extraction pipeline that:
- Queries real estate APIs for specific criteria:
  - 4+ beds  
  - Furnished  
  - For Rent By Owner
- Sanitizes and normalizes the resulting data
- Stores it in a relational database for future automated outreach

---

#### 1. Tech Stack & Environment
Keeping the stack lightweight but industry-standard ensures the project is scalable and easy to deploy.

- **Language**: Python 3.10+ (standard for data pipelines)
- **Virtual Environment**: `venv` or `conda` to manage dependencies
- **Dependencies**:
  - `requests` (handling HTTP API calls)
  - `sqlite3` (built-in Python library for database management)
  - `python-dotenv` (securing API keys in a `.env` file)
  - `pandas` (optional, but excellent for quick data manipulation and debugging)
- **Data Source**:
  - A Zillow API wrapper from RapidAPI (e.g., "Zillow Working API" or similar).
  - This bypasses the need to build complex web scrapers that get blocked by Zillow's security.

---

#### 2. Database Schema Design (SQLite)
Before writing any scraper code, the data destination must be defined. SQLite is ideal here because it’s serverless and writes directly to a local `.db` file.

- **Table Name**: `frbo_leads`

**Columns**

| Column Name   | Data Type | Constraints            | Description                                                  |
|--------------|-----------|------------------------|--------------------------------------------------------------|
| `property_id`| TEXT      | PRIMARY KEY            | Unique Zillow Property ID (`zpid`). Prevents duplicates.     |
| `address`    | TEXT      | NOT NULL               | Full property address.                                       |
| `price`      | INTEGER   | NOT NULL               | Monthly rental price.                                        |
| `bedrooms`   | INTEGER   | NOT NULL               | Number of bedrooms (validation check for 4+).                |
| `owner_name` | TEXT      | NULLABLE               | Name of the owner/property manager.                          |
| `owner_phone`| TEXT      | NULLABLE               | Extracted contact number.                                    |
| `listing_url`| TEXT      | NOT NULL               | Direct link to the Zillow listing.                           |
| `status`     | TEXT      | DEFAULT `'new'`        | Lead state (e.g., `'new'`, `'contacted_v2'`).                |
| `extracted_at`| DATETIME | DEFAULT CURRENT_TIMESTAMP | When the record was pulled.                             |

---

#### 3. The Extraction Pipeline (Step-by-Step Logic)

**Step 1: The Request Engine**
- Construct an HTTP GET request to the chosen RapidAPI endpoint.
- **Headers**:
  - `X-RapidAPI-Key`
  - `X-RapidAPI-Host`
- **Query Parameters** (example):
  - `status_type`: `"ForRent"`
  - `beds_min`: `4`
  - `keyword`: `"furnished"`
  - `listing_type`: `"fsbo"` or `"frbo"` (For Rent By Owner - exact parameter depends on the specific API).

**Step 2: JSON Parsing & Error Handling**
- Real estate APIs return massive, deeply nested JSON objects.
- Use safe navigation and `try`/`except` blocks.
- **Targeting**:
  - Iterate through the `results` array (or equivalent) in the JSON response.
- **Validation**:
  - Verify that the listing contains phone numbers and owner names.
  - If a property is listed by a large property management corporation (often lacking a direct owner phone number), flag or discard it to keep leads highly targeted.

**Step 3: Data Normalization (Crucial for v2.0)**
- Data from the internet is messy; clean it before writing to the database.
- **Phone Number Formatting**:
  - Use Regex to strip spaces, parentheses, and dashes from the `owner_phone` field.
  - Convert `(555) 123-4567` into `+15551234567` (E.164 standard).
  - This is required for the planned Twilio SMS integration in Version 2.0.
- **Price Formatting**:
  - Strip dollar signs and commas.
  - Convert string prices like `"$4,500"` into integers like `4500`.

**Step 4: The Upsert Operation**
- Handle duplicates gracefully using an UPSERT pattern.
- **Logic**:
  - Attempt to insert the new property using its `zpid` as `property_id`.
  - If the `property_id` already exists:
    - Update the `price` (in case the owner lowered the rent).
    - Update the `extracted_at` timestamp.

---

#### 4. Development Strategy: Division of Labor
This can be built as a joint effort with a clean division of responsibilities, mirroring a real agile team.

- **Developer A (Data Engineering)**:
  - Focus on the RapidAPI integration.
  - Implement the requests logic.
  - Handle API rate limits (e.g., pause the script for 2 seconds between calls).
  - Write the JSON parsing logic to extract needed variables.

- **Developer B (Database & Architecture)**:
  - Focus on backend storage.
  - Write SQLite creation scripts.
  - Implement INSERT/UPSERT SQL queries.
  - Implement data normalization functions (Regex for phone numbers, string-to-integer conversions for prices).

---

#### 5. Expected Output for v1.0
By the end of v1.0, running:

```bash
python main.py
```

should result in:

- A mostly silent execution that prints a simple progress bar or progress logs to the console.
- Creation (or updating) of a local `leads.db` file.
- A clean `frbo_leads` table filled with:
  - 4-bedroom (or more), furnished, owner-listed properties
  - Formatted owner phone numbers
- Data ready to be plugged into the Twilio SMS engine for **Version 2.0**.

