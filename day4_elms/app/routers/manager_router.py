from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.controllers.manager_controller import ManagerController
from app.dependencies.rbac import require_roles
from app.schemas.leave_schema import LeaveUpdate, LeaveResponse

router = APIRouter(prefix="/manager", tags=["Manager"])

@router.get("/leaves")
def get_department_leaves(status: str = None, page: int = Query(1, ge=1), size: int = Query(20, ge=1),
                          current_user=Depends(require_roles("MANAGER")), db: Session = Depends(get_db)):
    return ManagerController.get_department_leaves(current_user, status, page, size, db)

@router.put("/leaves/{leave_id}", response_model=LeaveResponse)
def approve_reject_leave(leave_id: int, update: LeaveUpdate, current_user=Depends(require_roles("MANAGER")), db: Session = Depends(get_db)):
    return ManagerController.approve_reject_leave(leave_id, update, current_user, db)
