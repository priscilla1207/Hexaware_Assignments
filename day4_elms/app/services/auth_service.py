from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.user_repo import UserRepository
from app.core.security import verify_password, create_access_token
from app.schemas.user_schema import LoginRequest

class AuthService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)
    
    def login(self, credentials: LoginRequest):
        user = self.user_repo.get_by_email(credentials.email)
        if not user or not verify_password(credentials.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        access_token = create_access_token(data={"sub": user.email, "role": user.role})
        return {"access_token": access_token, "token_type": "bearer"}
