from models.event import RawEvent
from core.database import SessionLocal
from datetime import datetime, timedelta

async def delete_old_events(session: SessionLocal, retention_days: int = 365):
    cutoff = datetime.utcnow() - timedelta(days=retention_days)
    await session.execute(RawEvent.__table__.delete().where(RawEvent.timestamp < cutoff))
    await session.commit()