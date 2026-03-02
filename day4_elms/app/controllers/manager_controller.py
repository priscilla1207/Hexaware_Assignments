from fastapi import Depends, Query
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.services.leave_service import LeaveService
from app.schemas.leave_schema import LeaveUpdate
from app.models.user import User

class ManagerController:
    @staticmethod
    def get_department_leaves(current_user: User, status: str = None, page: int = Query(1, ge=1), size: int = Query(20, ge=1), db: Session = Depends(get_db)):
        leave_service = LeaveService(db)
        return leave_service.get_department_leaves(current_user.department_id, status=status, page=page, size=size)
    
    @staticmethod
    def approve_reject_leave(leave_id: int, update: LeaveUpdate, current_user: User, db: Session = Depends(get_db)):
        leave_service = LeaveService(db)
        return leave_service.approve_reject_leave(leave_id, update.status, current_user.id, current_user.department_id)
