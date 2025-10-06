from core.security import require_role

@router.get("/report/daily", dependencies=[Depends(require_role("admin"))])
async def report_daily(...):
    ...