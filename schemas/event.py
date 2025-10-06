from pydantic import BaseModel
from typing import Optional

class RawEventCreate(BaseModel):
    user_id: Optional[int]
    timestamp: str
    camera_id: int
    status: str

class RawEventRead(BaseModel):
    event_id: int
    user_id: Optional[int]
    timestamp: str
    camera_id: int
    status: str