from sqlalchemy.orm import Session
from app.models.asset_request import AssetRequest
from app.schemas.request_schema import RequestCreate

class RequestRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, employee_id: int, request: RequestCreate) -> AssetRequest:
        db_request = AssetRequest(
            employee_id=employee_id,
            asset_type=request.asset_type,
            reason=request.reason
        )
        self.db.add(db_request)
        self.db.commit()
        self.db.refresh(db_request)
        return db_request
    
    def get_by_id(self, request_id: int) -> AssetRequest:
        return self.db.query(AssetRequest).filter(AssetRequest.id == request_id).first()
    
    def get_all(self, status: str = None):
        query = self.db.query(AssetRequest)
        if status:
            query = query.filter(AssetRequest.status == status)
        return query
    
    def update_status(self, request_id: int, status: str, approved_by: int = None):
        request = self.get_by_id(request_id)
        if request:
            request.status = status
            request.approved_by = approved_by
            self.db.commit()
            self.db.refresh(request)
        return request
