from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.asset_repo import AssetRepository
from app.schemas.asset_schema import AssetCreate

class AssetService:
    def __init__(self, db: Session):
        self.asset_repo = AssetRepository(db)
    
    def create_asset(self, asset: AssetCreate):
        existing = self.asset_repo.get_by_tag(asset.asset_tag)
        if existing:
            raise HTTPException(status_code=400, detail="Asset tag already exists")
        return self.asset_repo.create(asset)
    
    def get_assets(self, status: str = None, department_id: int = None, page: int = 1, size: int = 20):
        query = self.asset_repo.get_all(status=status, department_id=department_id)
        total = query.count()
        items = query.offset((page - 1) * size).limit(size).all()
        pages = (total + size - 1) // size
        return {
            "items": items,
            "total": total,
            "page": page,
            "size": size,
            "pages": pages
        }
    
    def get_asset_by_id(self, asset_id: int):
        asset = self.asset_repo.get_by_id(asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")
        return asset
