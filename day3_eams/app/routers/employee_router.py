from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.base import get_db
from app.controllers.employee_controller import EmployeeController
from app.dependencies.rbac import require_roles
from app.schemas.request_schema import RequestCreate, RequestResponse

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.post("/requests", response_model=RequestResponse)
def request_asset(request: RequestCreate, user=Depends(require_roles("EMPLOYEE")), db: Session = Depends(get_db)):
    return EmployeeController.request_asset(request, user, db)

@router.get("/my-assets")
def get_my_assets(user=Depends(require_roles("EMPLOYEE")), db: Session = Depends(get_db)):
    return EmployeeController.get_my_assets(user, db)
