from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.services.leave_service import LeaveService
from app.schemas.leave_schema import LeaveCreate
from app.models.user import User

class EmployeeController:
    @staticmethod
    def apply_leave(leave: LeaveCreate, current_user: User, db: Session = Depends(get_db)):
        leave_service = LeaveService(db)
        return leave_service.apply_leave(current_user.id, leave)
    
    @staticmethod
    def get_my_leaves(current_user: User, db: Session = Depends(get_db)):
        leave_service = LeaveService(db)
        return leave_service.get_employee_leaves(current_user.id)
