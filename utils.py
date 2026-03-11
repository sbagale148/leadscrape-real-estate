import re
from typing import Optional


def normalize_phone(raw: str) -> Optional[str]:
    digits = re.sub(r"\D", "", raw or "")
    if not digits:
        return None
    if len(digits) == 10:
        return f"+1{digits}"
    if len(digits) == 11 and digits.startswith("1"):
        return f"+{digits}"
    return f"+{digits}"


def normalize_price(raw) -> Optional[int]:
    if raw is None:
        return None
    text = str(raw)
    digits = re.sub(r"[^\d]", "", text)
    return int(digits) if digits else None

