from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models.camera import Camera
from schemas.camera import CameraCreate, CameraRead
from core.database import SessionLocal
from services.camera_health import check_camera_health
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=CameraRead)
async def register_camera(camera: CameraCreate, session: AsyncSession = Depends(SessionLocal)):
    cam = Camera(**camera.dict(), created_at=datetime.utcnow())
    session.add(cam)
    await session.commit()
    await session.refresh(cam)
    return cam

@router.get("/", response_model=list[CameraRead])
async def list_cameras(session: AsyncSession = Depends(SessionLocal)):
    result = await session.execute(Camera.__table__.select())
    cams = result.fetchall()
    return [CameraRead(**dict(c)) for c in cams]

@router.get("/{camera_id}", response_model=CameraRead)
async def get_camera(camera_id: int, session: AsyncSession = Depends(SessionLocal)):
    cam = await session.get(Camera, camera_id)
    if not cam:
        raise HTTPException(status_code=404, detail="Camera not found")
    return cam

@router.put("/{camera_id}", response_model=CameraRead)
async def update_camera(camera_id: int, camera: CameraCreate, session: AsyncSession = Depends(SessionLocal)):
    cam = await session.get(Camera, camera_id)
    if not cam:
        raise HTTPException(status_code=404, detail="Camera not found")
    for key, value in camera.dict().items():
        setattr(cam, key, value)
    await session.commit()
    await session.refresh(cam)
    return cam

@router.delete("/{camera_id}")
async def delete_camera(camera_id: int, session: AsyncSession = Depends(SessionLocal)):
    cam = await session.get(Camera, camera_id)
    if not cam:
        raise HTTPException(status_code=404, detail="Camera not found")
    await session.delete(cam)
    await session.commit()
    return {"status": "deleted"}

@router.get("/health/{camera_id}")
async def camera_health(camera_id: int, session: AsyncSession = Depends(SessionLocal)):
    cam = await session.get(Camera, camera_id)
    if not cam:
        raise HTTPException(status_code=404, detail="Camera not found")
    is_up, frame_rate = check_camera_health(cam.rtsp_url)
    cam.is_active = is_up
    cam.last_health_check = datetime.utcnow()
    cam.last_frame_rate = frame_rate
    await session.commit()
    await session.refresh(cam)
    return {
        "camera_id": cam.camera_id,
        "is_active": cam.is_active,
        "last_health_check": cam.last_health_check,
        "last_frame_rate": cam.last_frame_rate
    }