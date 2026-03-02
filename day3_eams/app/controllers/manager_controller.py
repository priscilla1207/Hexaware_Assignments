from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.services.asset_service import AssetService
from app.models.user import User

class ManagerController:
    @staticmethod
    def get_department_assets(current_user: User, db: Session = Depends(get_db)):
        asset_service = AssetService(db)
        return asset_service.get_assets(department_id=current_user.department_id)
