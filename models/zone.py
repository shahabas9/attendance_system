from sqlalchemy import Column, String, Integer
from models.base import Base

class Zone(Base):
    __tablename__ = "zones"
    zone_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)