from typing import Any, Dict

import requests

from config import Settings


def fetch_listings(settings: Settings, params: Dict[str, Any]) -> Dict[str, Any]:
    url = "https://example-rapidapi-endpoint.com"  # placeholder, to be replaced in later milestones
    headers = {
        "X-RapidAPI-Key": settings.rapidapi_key,
        "X-RapidAPI-Host": settings.rapidapi_host,
    }
    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    return response.json()

