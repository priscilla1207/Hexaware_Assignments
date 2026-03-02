from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user_schema import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)
    
    def create_user(self, user: UserCreate):
        return self.user_repo.create(user)
    
    def get_all_users(self):
        return self.user_repo.get_all()
