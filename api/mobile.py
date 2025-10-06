from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, timedelta
from core.database import SessionLocal
from models.attendance import AttendanceDaily, AttendanceSession
from models.user import User

router = APIRouter()

@router.get("/student/today")
async def today_logs(user_id: int, session: AsyncSession = Depends(SessionLocal)):
    """
    Student view: today's IN/OUT logs and total hours
    """
    today = date.today()
    # Daily summary
    result = await session.execute(
        AttendanceDaily.__table__.select().where(
            AttendanceDaily.user_id == user_id,
            AttendanceDaily.date == today
        )
    )
    att = result.fetchone()
    # Sessions
    result_sessions = await session.execute(
        AttendanceSession.__table__.select().where(
            AttendanceSession.user_id == user_id,
            AttendanceSession.in_time >= today,
            AttendanceSession.out_time <= today + timedelta(days=1)
        )
    )
    sessions = result_sessions.fetchall()
    return {
        "summary": dict(att) if att else {},
        "sessions": [dict(s) for s in sessions]
    }

@router.get("/student/history")
async def attendance_history(user_id: int, session: AsyncSession = Depends(SessionLocal)):
    """
    Student view: attendance history
    """
    result = await session.execute(
        AttendanceDaily.__table__.select().where(
            AttendanceDaily.user_id == user_id
        ).order_by(AttendanceDaily.date.desc())
    )
    history = result.fetchall()
    return [dict(h) for h in history]