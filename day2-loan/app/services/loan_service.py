from fastapi import HTTPException
from app.repositories.loan_repository import LoanRepository
from app.schemas.loan_schema import LoanCreate, LoanResponse, LoanStatusResponse

class LoanService:
    ELIGIBILITY_MULTIPLIER = 10
    
    def __init__(self, repository: LoanRepository):
        self.repository = repository
    
    def _calculate_eligibility(self, income: float) -> float:
        return income * self.ELIGIBILITY_MULTIPLIER
    
    def submit_application(self, loan: LoanCreate) -> LoanResponse:
        eligibility = self._calculate_eligibility(loan.income)
        
        if loan.loan_amount > eligibility:
            db_loan = self.repository.create(loan, status="REJECTED")
        else:
            db_loan = self.repository.create(loan, status="PENDING")
        
        return LoanResponse.model_validate(db_loan)
    
    def get_loan(self, loan_id: int) -> LoanResponse:
        loan = self.repository.get_by_id(loan_id)
        if not loan:
            raise HTTPException(status_code=404, detail="Loan application not found")
        return LoanResponse.model_validate(loan)
    
    def get_all_loans(self) -> list[LoanResponse]:
        loans = self.repository.get_all()
        return [LoanResponse.model_validate(loan) for loan in loans]
    
    def approve_loan(self, loan_id: int) -> LoanStatusResponse:
        loan = self.repository.get_by_id(loan_id)
        
        if not loan:
            raise HTTPException(status_code=404, detail="Loan application not found")
        
        if loan.status != "PENDING":
            raise HTTPException(status_code=400, detail="Only pending loans can be approved")
        
        eligibility = self._calculate_eligibility(loan.income)
        if loan.loan_amount > eligibility:
            raise HTTPException(status_code=400, detail="Loan amount exceeds eligibility limit")
        
        self.repository.update_status(loan_id, "APPROVED")
        return LoanStatusResponse(message="Loan approved successfully", status="APPROVED")
    
    def reject_loan(self, loan_id: int) -> LoanStatusResponse:
        loan = self.repository.get_by_id(loan_id)
        
        if not loan:
            raise HTTPException(status_code=404, detail="Loan application not found")
        
        if loan.status != "PENDING":
            raise HTTPException(status_code=400, detail="Only pending loans can be rejected")
        
        self.repository.update_status(loan_id, "REJECTED")
        return LoanStatusResponse(message="Loan rejected", status="REJECTED")
