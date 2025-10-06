from pydantic import BaseModel
from typing import Optional

class CameraCreate(BaseModel):
    location: str
    type: str
    rtsp_url: str
    zone: str

class CameraRead(BaseModel):
    camera_id: int
    location: str
    type: str
    rtsp_url: str
    zone: str
    is_active: bool
    last_health_check: Optional[str]
    last_frame_rate: Optional[int]