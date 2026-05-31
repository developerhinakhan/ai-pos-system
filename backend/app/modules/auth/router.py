from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.auth.schema import RegisterRequest, LoginRequest, TokenResponse
from app.modules.auth.service import auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=TokenResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return auth_service.register(db, data)


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return auth_service.login(db, data)