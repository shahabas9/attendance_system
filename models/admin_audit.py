from sqlalchemy import Column, Integer, DateTime, String
from models.base import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"
    log_id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
    performed_by = Column(String)
    timestamp = Column(DateTime)
    details = Column(String)