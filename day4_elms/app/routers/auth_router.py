from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.controllers.auth_controller import AuthController
from app.schemas.user_schema import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    return AuthController.login(credentials, db)
