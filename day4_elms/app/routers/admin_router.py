from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.controllers.admin_controller import AdminController
from app.dependencies.rbac import require_roles
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.department_schema import DepartmentCreate, DepartmentResponse
from app.schemas.leave_schema import LeaveUpdate, LeaveResponse
from typing import List

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, current_user=Depends(require_roles("ADMIN")), db: Session = Depends(get_db)):
    return AdminController.create_user(user, db)

@router.get("/users", response_model=List[UserResponse])
def get_all_users(current_user=Depends(require_roles("ADMIN")), db: Session = Depends(get_db)):
    return AdminController.get_all_users(db)

@router.post("/departments", response_model=DepartmentResponse)
def create_department(dept: DepartmentCreate, current_user=Depends(require_roles("ADMIN")), db: Session = Depends(get_db)):
    return AdminController.create_department(dept, db)

@router.get("/departments", response_model=List[DepartmentResponse])
def get_all_departments(current_user=Depends(require_roles("ADMIN")), db: Session = Depends(get_db)):
    return AdminController.get_all_departments(db)

@router.get("/leaves")
def get_all_leaves(status: str = None, page: int = Query(1, ge=1), size: int = Query(20, ge=1), 
                    current_user=Depends(require_roles("ADMIN")), db: Session = Depends(get_db)):
    return AdminController.get_all_leaves(status, page, size, db)

@router.put("/leaves/{leave_id}", response_model=LeaveResponse)
def update_leave_status(leave_id: int, update: LeaveUpdate, current_user=Depends(require_roles("ADMIN")), db: Session = Depends(get_db)):
    return AdminController.update_leave_status(leave_id, update, current_user, db)
