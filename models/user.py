from sqlalchemy import Column, String, Integer, DateTime, JSON
from models.base import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    roll_no = Column(String, unique=True, nullable=True)
    class_name = Column(String, nullable=True)
    user_type = Column(String, nullable=False)  # student/employee/admin
    embeddings = Column(JSON, default=[])
    created_at = Column(DateTime)