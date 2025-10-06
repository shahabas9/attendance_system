from pydantic import BaseModel
from typing import Optional

class ZoneCreate(BaseModel):
    name: str
    description: Optional[str]

class ZoneRead(BaseModel):
    zone_id: int
    name: str
    description: Optional[str]