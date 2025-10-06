from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey, String, Interval
from models.base import Base

class AttendanceSession(Base):
    __tablename__ = "attendance_sessions"
    session_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    in_time = Column(DateTime)
    out_time = Column(DateTime)
    duration = Column(Interval)

class AttendanceDaily(Base):
    __tablename__ = "attendance_daily"
    date = Column(Date, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    first_in = Column(DateTime)
    last_out = Column(DateTime)
    total_duration = Column(Interval)
    status = Column(String)