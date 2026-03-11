from dataclasses import dataclass
from typing import Optional


@dataclass
class Listing:
    property_id: str
    address: str
    price: int
    bedrooms: int
    owner_name: Optional[str]
    owner_phone: Optional[str]
    listing_url: str
    status: str = "new"

