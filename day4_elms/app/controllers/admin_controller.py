from fastapi import Depends, Query
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.services.user_service import UserService
from app.services.department_service import DepartmentService
from app.services.leave_service import LeaveService
from app.schemas.user_schema import UserCreate
from app.schemas.department_schema import DepartmentCreate
from app.schemas.leave_schema import LeaveUpdate

class AdminController:
    @staticmethod
    def create_user(user: UserCreate, db: Session = Depends(get_db)):
        user_service = UserService(db)
        return user_service.create_user(user)
    
    @staticmethod
    def get_all_users(db: Session = Depends(get_db)):
        user_service = UserService(db)
        return user_service.get_all_users()
    
    @staticmethod
    def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
        dept_service = DepartmentService(db)
        return dept_service.create_department(dept)
    
    @staticmethod
    def get_all_departments(db: Session = Depends(get_db)):
        dept_service = DepartmentService(db)
        return dept_service.get_all_departments()
    
    @staticmethod
    def get_all_leaves(status: str = None, page: int = Query(1, ge=1), size: int = Query(20, ge=1), db: Session = Depends(get_db)):
        leave_service = LeaveService(db)
        return leave_service.get_all_leaves(status=status, page=page, size=size)
    
    @staticmethod
    def update_leave_status(leave_id: int, update: LeaveUpdate, current_user, db: Session = Depends(get_db)):
        leave_service = LeaveService(db)
        return leave_service.approve_reject_leave(leave_id, update.status, current_user.id)
