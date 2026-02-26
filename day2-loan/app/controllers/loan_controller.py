from fastapi import APIRouter, Depends, status
from app.schemas.loan_schema import LoanCreate, LoanResponse, LoanStatusResponse
from app.services.loan_service import LoanService
from app.dependencies.loan_dependency import get_loan_service

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("", response_model=LoanResponse, status_code=status.HTTP_201_CREATED)
def submit_loan_application(loan: LoanCreate, service: LoanService = Depends(get_loan_service)):
    return service.submit_application(loan)

@router.get("/{loan_id}", response_model=LoanResponse)
def get_loan_application(loan_id: int, service: LoanService = Depends(get_loan_service)):
    return service.get_loan(loan_id)

@router.get("", response_model=list[LoanResponse])
def get_all_loan_applications(service: LoanService = Depends(get_loan_service)):
    return service.get_all_loans()

@router.put("/{loan_id}/approve", response_model=LoanStatusResponse)
def approve_loan(loan_id: int, service: LoanService = Depends(get_loan_service)):
    return service.approve_loan(loan_id)

@router.put("/{loan_id}/reject", response_model=LoanStatusResponse)
def reject_loan(loan_id: int, service: LoanService = Depends(get_loan_service)):
    return service.reject_loan(loan_id)
