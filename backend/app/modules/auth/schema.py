from pydantic import BaseModel, EmailStr
from typing import Optional


# Input schemas
class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    contact_no: Optional[str] = None
    address: Optional[str] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# Output schemas
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True