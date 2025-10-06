from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    # Could check DB, cache, camera status, etc.
    return {"status": "ok"}