from pydantic import BaseModel
from typing import Optional
from datetime import date

class AssignmentBase(BaseModel):
    asset_id: int
    user_id: int

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentReturn(BaseModel):
    condition_on_return: Optional[str] = None

class AssignmentResponse(AssignmentBase):
    id: int
    assigned_date: date
    returned_date: Optional[date] = None
    condition_on_return: Optional[str] = None
    
    class Config:
        from_attributes = True
