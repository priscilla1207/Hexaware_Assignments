from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.services.asset_service import AssetService
from app.repositories.user_repo import UserRepository
from app.repositories.department_repo import DepartmentRepository
from app.schemas.asset_schema import AssetCreate
from app.schemas.user_schema import UserCreate
from app.schemas.department_schema import DepartmentCreate

class SuperAdminController:
    @staticmethod
    def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
        asset_service = AssetService(db)
        return asset_service.create_asset(asset)
    
    @staticmethod
    def create_user(user: UserCreate, db: Session = Depends(get_db)):
        user_repo = UserRepository(db)
        return user_repo.create(user)
    
    @staticmethod
    def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
        dept_repo = DepartmentRepository(db)
        return dept_repo.create(dept)
