from pydantic import BaseModel
from typing import Optional

class RequestBase(BaseModel):
    asset_type: str
    reason: str

class RequestCreate(RequestBase):
    pass

class RequestApprove(BaseModel):
    asset_id: int

class RequestResponse(RequestBase):
    id: int
    employee_id: int
    status: str
    approved_by: Optional[int] = None
    
    class Config:
        from_attributes = True
