from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.leave_repo import LeaveRepository
from app.repositories.user_repo import UserRepository
from app.schemas.leave_schema import LeaveCreate, LeaveUpdate
from datetime import date

class LeaveService:
    def __init__(self, db: Session):
        self.leave_repo = LeaveRepository(db)
        self.user_repo = UserRepository(db)
    
    def apply_leave(self, employee_id: int, leave: LeaveCreate):
        # Validate dates
        if leave.start_date > leave.end_date:
            raise HTTPException(status_code=400, detail="Start date must be before end date")
        
        if leave.start_date < date.today():
            raise HTTPException(status_code=400, detail="Cannot apply for past dates")
        
        # Check for overlapping leave
        if self.leave_repo.check_overlap(employee_id, leave.start_date, leave.end_date):
            raise HTTPException(status_code=400, detail="Overlapping leave request exists")
        
        return self.leave_repo.create(employee_id, leave)
    
    def get_employee_leaves(self, employee_id: int):
        return self.leave_repo.get_by_employee(employee_id)
    
    def get_all_leaves(self, status: str = None, page: int = 1, size: int = 20):
        from app.core.pagination import paginate
        query = self.leave_repo.get_all(status=status)
        return paginate(query, page, size)
    
    def get_department_leaves(self, department_id: int, status: str = None, page: int = 1, size: int = 20):
        from app.core.pagination import paginate
        query = self.leave_repo.get_by_department(department_id, status=status)
        return paginate(query, page, size)
    
    def approve_reject_leave(self, leave_id: int, status: str, approved_by: int, manager_dept_id: int = None):
        leave = self.leave_repo.get_by_id(leave_id)
        if not leave:
            raise HTTPException(status_code=404, detail="Leave request not found")
        
        if leave.status != "PENDING":
            raise HTTPException(status_code=400, detail="Leave already processed")
        
        # If manager, check if leave belongs to their department
        if manager_dept_id:
            employee = self.user_repo.get_by_id(leave.employee_id)
            if employee.department_id != manager_dept_id:
                raise HTTPException(status_code=403, detail="Cannot approve leave from other departments")
        
        if status not in ["APPROVED", "REJECTED"]:
            raise HTTPException(status_code=400, detail="Invalid status")
        
        return self.leave_repo.update_status(leave_id, status, approved_by)
