from pydantic import BaseModel
from typing import Optional
from datetime import date

class AssetBase(BaseModel):
    asset_tag: str
    asset_type: str
    brand: Optional[str] = None
    model: Optional[str] = None
    purchase_date: Optional[date] = None
    department_id: Optional[int] = None

class AssetCreate(AssetBase):
    pass

class AssetResponse(AssetBase):
    id: int
    status: str
    
    class Config:
        from_attributes = True
