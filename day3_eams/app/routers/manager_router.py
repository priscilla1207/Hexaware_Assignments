from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.controllers.manager_controller import ManagerController
from app.dependencies.rbac import require_roles

router = APIRouter(prefix="/manager", tags=["Manager"])

@router.get("/department-assets")
def get_department_assets(user=Depends(require_roles("MANAGER")), db: Session = Depends(get_db)):
    return ManagerController.get_department_assets(user, db)
