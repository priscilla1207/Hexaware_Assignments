from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.assignment_repo import AssignmentRepository
from app.repositories.asset_repo import AssetRepository
from app.schemas.assignment_schema import AssignmentCreate

class AssignmentService:
    def __init__(self, db: Session):
        self.assignment_repo = AssignmentRepository(db)
        self.asset_repo = AssetRepository(db)
    
    def assign_asset(self, assignment: AssignmentCreate):
        asset = self.asset_repo.get_by_id(assignment.asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")
        
        if asset.status != "AVAILABLE":
            raise HTTPException(status_code=400, detail="Asset is not available")
        
        active_assignment = self.assignment_repo.get_active_by_asset(assignment.asset_id)
        if active_assignment:
            raise HTTPException(status_code=400, detail="Asset already assigned")
        
        new_assignment = self.assignment_repo.create(assignment.asset_id, assignment.user_id)
        self.asset_repo.update_status(assignment.asset_id, "ASSIGNED")
        return new_assignment
    
    def return_asset(self, assignment_id: int, condition: str = None):
        assignment = self.assignment_repo.return_asset(assignment_id, condition)
        if assignment:
            self.asset_repo.update_status(assignment.asset_id, "AVAILABLE")
        return assignment
    
    def get_user_assets(self, user_id: int):
        return self.assignment_repo.get_by_user(user_id)
