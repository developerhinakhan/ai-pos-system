from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.auth.repo import auth_repo
from app.modules.auth.schema import RegisterRequest, LoginRequest
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    def register(self, db: Session, data: RegisterRequest):
        # Check if email already exists
        existing_user = auth_repo.get_user_by_email(db, data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Hash password
        hashed = hash_password(data.password)

        # Create user
        user_data = {
            "name": data.name,
            "email": data.email,
            "password": hashed,
            "contact_no": data.contact_no,
            "address": data.address
        }
        user = auth_repo.create_user(db, user_data)

        # Create token
        token = create_access_token({"sub": user.email})

        return {"access_token": token, "token_type": "bearer"}

    def login(self, db: Session, data: LoginRequest):
        # Find user
        user = auth_repo.get_user_by_email(db, data.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Verify password
        if not verify_password(data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Wrong password"
            )

        # Check if active
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Account is disabled"
            )

        # Create token
        token = create_access_token({"sub": user.email})

        return {"access_token": token, "token_type": "bearer"}


auth_service = AuthService()