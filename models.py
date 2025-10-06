from pydantic import BaseModel
from typing import List, Optional

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: str
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ImageOut(BaseModel):
    filename: str
    faces_detected: int