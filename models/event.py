from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from models.base import Base

class RawEvent(Base):
    __tablename__ = "raw_events"
    event_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    timestamp = Column(DateTime, nullable=False)
    camera_id = Column(Integer, ForeignKey("cameras.camera_id"))
    status = Column(String)  # in/out/unknown