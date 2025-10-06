from pydantic import BaseModel
from typing import Optional

class HolidayCreate(BaseModel):
    date: str
    description: Optional[str]

class HolidayRead(BaseModel):
    holiday_id: int
    date: str
    description: Optional[str]