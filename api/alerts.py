from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import SessionLocal
from models.event import RawEvent
from models.camera import Camera
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/alerts/unknown_faces")
async def alert_unknown_faces(minutes: int = 10, session: AsyncSession = Depends(SessionLocal)):
    since = datetime.utcnow() - timedelta(minutes=minutes)
    result = await session.execute(
        RawEvent.__table__.select().where(
            RawEvent.timestamp >= since,
            RawEvent.status == "unknown"
        )
    )
    count = len(result.fetchall())
    return {"unknown_faces_last_10_min": count, "alert": count > 5}

@router.get("/alerts/camera_failures")
async def alert_camera_failures(session: AsyncSession = Depends(SessionLocal)):
    result = await session.execute(Camera.__table__.select().where(Camera.is_active == False))
    failed = result.fetchall()
    return {"failed_cameras": [dict(f) for f in failed], "alert": len(failed) > 0}