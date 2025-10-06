from sqlalchemy import Column, String, Integer, DateTime, Boolean
from models.base import Base

class Camera(Base):
    __tablename__ = "cameras"
    camera_id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    type = Column(String)  # entry/exit/internal
    rtsp_url = Column(String, nullable=False)
    zone = Column(String)
    created_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    last_health_check = Column(DateTime, nullable=True)
    last_frame_rate = Column(Integer, nullable=True)