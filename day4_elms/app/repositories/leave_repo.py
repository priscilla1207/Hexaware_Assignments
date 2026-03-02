from sqlalchemy.orm import Session
from app.models.leave_request import LeaveRequest
from app.schemas.leave_schema import LeaveCreate
from typing import Optional

class LeaveRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, employee_id: int, leave: LeaveCreate) -> LeaveRequest:
        db_leave = LeaveRequest(
            employee_id=employee_id,
            start_date=leave.start_date,
            end_date=leave.end_date,
            reason=leave.reason
        )
        self.db.add(db_leave)
        self.db.commit()
        self.db.refresh(db_leave)
        return db_leave
    
    def get_by_id(self, leave_id: int) -> LeaveRequest:
        return self.db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    
    def get_by_employee(self, employee_id: int):
        return self.db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id).all()
    
    def get_all(self, status: Optional[str] = None):
        query = self.db.query(LeaveRequest)
        if status:
            query = query.filter(LeaveRequest.status == status)
        return query
    
    def get_by_department(self, department_id: int, status: Optional[str] = None):
        from app.models.user import User
        query = self.db.query(LeaveRequest).join(User).filter(User.department_id == department_id)
        if status:
            query = query.filter(LeaveRequest.status == status)
        return query
    
    def update_status(self, leave_id: int, status: str, approved_by: int):
        leave = self.get_by_id(leave_id)
        if leave:
            leave.status = status
            leave.approved_by = approved_by
            self.db.commit()
            self.db.refresh(leave)
        return leave
    
    def check_overlap(self, employee_id: int, start_date, end_date) -> bool:
        overlapping = self.db.query(LeaveRequest).filter(
            LeaveRequest.employee_id == employee_id,
            LeaveRequest.status != "REJECTED",
            LeaveRequest.start_date <= end_date,
            LeaveRequest.end_date >= start_date
        ).first()
        return overlapping is not None
