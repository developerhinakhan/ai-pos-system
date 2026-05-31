from sqlalchemy.orm import Session
from app.modules.users.model import User


class AuthRepo:

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create_user(self, db: Session, user_data: dict):
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


auth_repo = AuthRepo()