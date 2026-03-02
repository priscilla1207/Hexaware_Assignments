from sqlalchemy.orm import Session
from app.models.asset_assignment import AssetAssignment
from datetime import date

class AssignmentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, asset_id: int, user_id: int) -> AssetAssignment:
        assignment = AssetAssignment(
            asset_id=asset_id,
            user_id=user_id,
            assigned_date=date.today()
        )
        self.db.add(assignment)
        self.db.commit()
        self.db.refresh(assignment)
        return assignment
    
    def get_active_by_asset(self, asset_id: int) -> AssetAssignment:
        return self.db.query(AssetAssignment).filter(
            AssetAssignment.asset_id == asset_id,
            AssetAssignment.returned_date == None
        ).first()
    
    def get_by_user(self, user_id: int):
        return self.db.query(AssetAssignment).filter(
            AssetAssignment.user_id == user_id,
            AssetAssignment.returned_date == None
        ).all()
    
    def return_asset(self, assignment_id: int, condition: str = None):
        assignment = self.db.query(AssetAssignment).filter(AssetAssignment.id == assignment_id).first()
        if assignment:
            assignment.returned_date = date.today()
            assignment.condition_on_return = condition
            self.db.commit()
            self.db.refresh(assignment)
        return assignment
