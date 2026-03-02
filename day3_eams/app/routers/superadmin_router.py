from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.controllers.superadmin_controller import SuperAdminController
from app.dependencies.rbac import require_roles
from app.schemas.asset_schema import AssetCreate, AssetResponse
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.department_schema import DepartmentCreate, DepartmentResponse

router = APIRouter(prefix="/superadmin", tags=["SuperAdmin"])

@router.post("/assets", response_model=AssetResponse)
def create_asset(asset: AssetCreate, user=Depends(require_roles("SUPERADMIN")), db: Session = Depends(get_db)):
    return SuperAdminController.create_asset(asset, db)

@router.post("/users", response_model=UserResponse)
def create_user(user_data: UserCreate, user=Depends(require_roles("SUPERADMIN")), db: Session = Depends(get_db)):
    return SuperAdminController.create_user(user_data, db)

@router.post("/departments", response_model=DepartmentResponse)
def create_department(dept: DepartmentCreate, user=Depends(require_roles("SUPERADMIN")), db: Session = Depends(get_db)):
    return SuperAdminController.create_department(dept, db)
