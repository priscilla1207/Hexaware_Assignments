from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import get_password_hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user: UserCreate) -> User:
        hashed_password = get_password_hash(user.password)
        db_user = User(
            name=user.name,
            email=user.email,
            password=hashed_password,
            role=user.role,
            department_id=user.department_id
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()
