from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.holiday import Holiday
from schemas.holiday import HolidayCreate, HolidayRead
from core.database import SessionLocal
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=HolidayRead)
async def add_holiday(holiday: HolidayCreate, session: AsyncSession = Depends(SessionLocal)):
    hol = Holiday(date=datetime.strptime(holiday.date, "%Y-%m-%d").date(), description=holiday.description)
    session.add(hol)
    await session.commit()
    await session.refresh(hol)
    return hol

@router.get("/", response_model=list[HolidayRead])
async def list_holidays(session: AsyncSession = Depends(SessionLocal)):
    result = await session.execute(Holiday.__table__.select())
    holidays = result.fetchall()
    return [HolidayRead(**dict(h)) for h in holidays]