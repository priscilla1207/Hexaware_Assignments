from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.services.auth_service import AuthService
from app.schemas.user_schema import LoginRequest

class AuthController:
    @staticmethod
    def login(credentials: LoginRequest, db: Session = Depends(get_db)):
        auth_service = AuthService(db)
        return auth_service.login(credentials)
