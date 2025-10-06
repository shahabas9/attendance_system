from sqlalchemy import Column, Date, String, Integer
from models.base import Base

class Holiday(Base):
    __tablename__ = "holidays"
    holiday_id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True, nullable=False)
    description = Column(String, nullable=True)