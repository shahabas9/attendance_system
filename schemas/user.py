from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    roll_no: Optional[str]
    class_name: Optional[str]
    user_type: str

class UserRead(BaseModel):
    user_id: int
    name: str
    roll_no: Optional[str]
    class_name: Optional[str]
    user_type: str

class UserEmbedding(BaseModel):
    user_id: int
    embeddings: List[List[float]]