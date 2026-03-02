from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.schemas.asset_schema import AssetCreate
from typing import Optional

class AssetRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, asset: AssetCreate) -> Asset:
        db_asset = Asset(**asset.dict())
        self.db.add(db_asset)
        self.db.commit()
        self.db.refresh(db_asset)
        return db_asset
    
    def get_by_id(self, asset_id: int) -> Asset:
        return self.db.query(Asset).filter(Asset.id == asset_id).first()
    
    def get_by_tag(self, asset_tag: str) -> Asset:
        return self.db.query(Asset).filter(Asset.asset_tag == asset_tag).first()
    
    def get_all(self, status: Optional[str] = None, department_id: Optional[int] = None):
        query = self.db.query(Asset)
        if status:
            query = query.filter(Asset.status == status)
        if department_id:
            query = query.filter(Asset.department_id == department_id)
        return query
    
    def update_status(self, asset_id: int, status: str):
        asset = self.get_by_id(asset_id)
        if asset:
            asset.status = status
            self.db.commit()
            self.db.refresh(asset)
        return asset
