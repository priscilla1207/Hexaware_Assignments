from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.request_repo import RequestRepository
from app.services.assignment_service import AssignmentService
from app.schemas.request_schema import RequestCreate, RequestApprove
from app.schemas.assignment_schema import AssignmentCreate

class RequestService:
    def __init__(self, db: Session):
        self.request_repo = RequestRepository(db)
        self.assignment_service = AssignmentService(db)
    
    def create_request(self, employee_id: int, request: RequestCreate):
        return self.request_repo.create(employee_id, request)
    
    def get_requests(self, status: str = None, page: int = 1, size: int = 20):
        from app.core.pagination import paginate
        query = self.request_repo.get_all(status=status)
        return paginate(query, page, size)
    
    def approve_request(self, request_id: int, approval: RequestApprove, approved_by: int):
        request = self.request_repo.get_by_id(request_id)
        if not request:
            raise HTTPException(status_code=404, detail="Request not found")
        
        if request.status != "PENDING":
            raise HTTPException(status_code=400, detail="Request already processed")
        
        # Assign asset
        assignment = AssignmentCreate(asset_id=approval.asset_id, user_id=request.employee_id)
        self.assignment_service.assign_asset(assignment)
        
        # Update request status
        return self.request_repo.update_status(request_id, "APPROVED", approved_by)
    
    def reject_request(self, request_id: int, rejected_by: int):
        request = self.request_repo.get_by_id(request_id)
        if not request:
            raise HTTPException(status_code=404, detail="Request not found")
        
        return self.request_repo.update_status(request_id, "REJECTED", rejected_by)
