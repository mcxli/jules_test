from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class LoginCredentials(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

@router.post("/login")
async def login(credentials: LoginCredentials):
    if not credentials.username or not credentials.password:
        raise HTTPException(status_code=400, detail="Username and password are required")
    return {"message": "Login successful"}
