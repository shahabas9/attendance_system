from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models.zone import Zone
from schemas.zone import ZoneCreate, ZoneRead
from core.database import SessionLocal

router = APIRouter()

@router.post("/", response_model=ZoneRead)
async def create_zone(zone: ZoneCreate, session: AsyncSession = Depends(SessionLocal)):
    zn = Zone(**zone.dict())
    session.add(zn)
    await session.commit()
    await session.refresh(zn)
    return zn

@router.get("/", response_model=list[ZoneRead])
async def list_zones(session: AsyncSession = Depends(SessionLocal)):
    result = await session.execute(Zone.__table__.select())
    zones = result.fetchall()
    return [ZoneRead(**dict(z)) for z in zones]

@router.get("/{zone_id}", response_model=ZoneRead)
async def get_zone(zone_id: int, session: AsyncSession = Depends(SessionLocal)):
    zn = await session.get(Zone, zone_id)
    if not zn:
        raise HTTPException(status_code=404, detail="Zone not found")
    return zn

@router.put("/{zone_id}", response_model=ZoneRead)
async def update_zone(zone_id: int, zone: ZoneCreate, session: AsyncSession = Depends(SessionLocal)):
    zn = await session.get(Zone, zone_id)
    if not zn:
        raise HTTPException(status_code=404, detail="Zone not found")
    for key, value in zone.dict().items():
        setattr(zn, key, value)
    await session.commit()
    await session.refresh(zn)
    return zn

@router.delete("/{zone_id}")
async def delete_zone(zone_id: int, session: AsyncSession = Depends(SessionLocal)):
    zn = await session.get(Zone, zone_id)
    if not zn:
        raise HTTPException(status_code=404, detail="Zone not found")
    await session.delete(zn)
    await session.commit()
    return {"status": "deleted"}