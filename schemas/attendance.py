from pydantic import BaseModel
from typing import Optional

class AttendanceSessionRead(BaseModel):
    session_id: int
    user_id: int
    in_time: str
    out_time: str
    duration: str

class AttendanceDailyRead(BaseModel):
    date: str
    user_id: int
    first_in: str
    last_out: str
    total_duration: str
    status: str