from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.controllers.employee_controller import EmployeeController
from app.dependencies.rbac import require_roles
from app.schemas.leave_schema import LeaveCreate, LeaveResponse
from typing import List

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.post("/leaves", response_model=LeaveResponse)
def apply_leave(leave: LeaveCreate, current_user=Depends(require_roles("EMPLOYEE")), db: Session = Depends(get_db)):
    return EmployeeController.apply_leave(leave, current_user, db)

@router.get("/leaves", response_model=List[LeaveResponse])
def get_my_leaves(current_user=Depends(require_roles("EMPLOYEE")), db: Session = Depends(get_db)):
    return EmployeeController.get_my_leaves(current_user, db)
