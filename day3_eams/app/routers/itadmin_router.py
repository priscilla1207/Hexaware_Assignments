from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.controllers.itadmin_controller import ITAdminController
from app.dependencies.rbac import require_roles
from app.schemas.asset_schema import AssetCreate, AssetResponse
from app.schemas.assignment_schema import AssignmentCreate, AssignmentResponse

router = APIRouter(prefix="/itadmin", tags=["IT Admin"])

@router.post("/assets", response_model=AssetResponse)
def create_asset(asset: AssetCreate, user=Depends(require_roles("SUPERADMIN", "IT_ADMIN")), db: Session = Depends(get_db)):
    return ITAdminController.create_asset(asset, db)

@router.get("/assets")
def get_assets(status: str = None, page: int = Query(1, ge=1), size: int = Query(20, ge=1), 
               user=Depends(require_roles("SUPERADMIN", "IT_ADMIN")), db: Session = Depends(get_db)):
    return ITAdminController.get_assets(status, page, size, db)

@router.post("/assignments", response_model=AssignmentResponse)
def assign_asset(assignment: AssignmentCreate, user=Depends(require_roles("SUPERADMIN", "IT_ADMIN")), db: Session = Depends(get_db)):
    return ITAdminController.assign_asset(assignment, db)
