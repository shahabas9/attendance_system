from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from core.database import SessionLocal
from services.attendance import attendance_batch_job
from models.attendance import AttendanceDaily, AttendanceSession

router = APIRouter()

@router.post("/process/{day}")
async def process_attendance(day: date, session: AsyncSession = Depends(SessionLocal)):
    await attendance_batch_job(session, day)
    return {"status": "Attendance processed"}

@router.get("/daily/{user_id}/{day}")
async def get_daily_attendance(user_id: int, day: date, session: AsyncSession = Depends(SessionLocal)):
    result = await session.execute(
        AttendanceDaily.__table__.select().where(
            AttendanceDaily.user_id == user_id,
            AttendanceDaily.date == day
        )
    )
    att = result.fetchone()
    return dict(att) if att else {}

@router.get("/sessions/{user_id}/{day}")
async def get_attendance_sessions(user_id: int, day: date, session: AsyncSession = Depends(SessionLocal)):
    result = await session.execute(
        AttendanceSession.__table__.select().where(
            AttendanceSession.user_id == user_id,
            AttendanceSession.in_time >= day,
            AttendanceSession.out_time <= day + timedelta(days=1)
        )
    )
    sessions = result.fetchall()
    return [dict(s) for s in sessions]