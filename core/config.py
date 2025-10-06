import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change_this_in_prod")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:pass@localhost/attendance_db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    FACE_MODEL: str = os.getenv("FACE_MODEL", "ArcFace")  # ArcFace, DeepFace, FaceNet
    RTSP_FRAME_INTERVAL: int = 2  # seconds
    SESSION_TIMEOUT_MINUTES: int = 10
    SHIFT_END_HOUR: int = 18
    GRACE_MINUTES: int = 10

settings = Settings()