from core.security import require_role

@router.delete("/{user_id}", dependencies=[Depends(require_role("admin"))])
async def delete_user(user_id: int, session: AsyncSession = Depends(SessionLocal)):
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Cascade: delete events, attendance, etc.
    await session.execute(RawEvent.__table__.delete().where(RawEvent.user_id == user_id))
    await session.execute(AttendanceDaily.__table__.delete().where(AttendanceDaily.user_id == user_id))
    await session.execute(AttendanceSession.__table__.delete().where(AttendanceSession.user_id == user_id))
    await session.delete(user)
    await session.commit()
    return {"status": "deleted"}