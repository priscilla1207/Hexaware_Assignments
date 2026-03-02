from fastapi import Depends, Query
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.services.asset_service import AssetService
from app.services.assignment_service import AssignmentService
from app.services.request_service import RequestService
from app.schemas.asset_schema import AssetCreate
from app.schemas.assignment_schema import AssignmentCreate, AssignmentReturn
from app.schemas.request_schema import RequestApprove

class ITAdminController:
    @staticmethod
    def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
        asset_service = AssetService(db)
        return asset_service.create_asset(asset)
    
    @staticmethod
    def get_assets(status: str = None, page: int = Query(1, ge=1), size: int = Query(20, ge=1), db: Session = Depends(get_db)):
        asset_service = AssetService(db)
        return asset_service.get_assets(status=status, page=page, size=size)
    
    @staticmethod
    def assign_asset(assignment: AssignmentCreate, db: Session = Depends(get_db)):
        assignment_service = AssignmentService(db)
        return assignment_service.assign_asset(assignment)
