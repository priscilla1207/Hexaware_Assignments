from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.services.request_service import RequestService
from app.services.assignment_service import AssignmentService
from app.schemas.request_schema import RequestCreate
from app.models.user import User

class EmployeeController:
    @staticmethod
    def request_asset(request: RequestCreate, current_user: User, db: Session = Depends(get_db)):
        request_service = RequestService(db)
        return request_service.create_request(current_user.id, request)
    
    @staticmethod
    def get_my_assets(current_user: User, db: Session = Depends(get_db)):
        assignment_service = AssignmentService(db)
        return assignment_service.get_user_assets(current_user.id)
