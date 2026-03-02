from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate

class DepartmentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, department: DepartmentCreate) -> Department:
        db_dept = Department(**department.dict())
        self.db.add(db_dept)
        self.db.commit()
        self.db.refresh(db_dept)
        return db_dept
    
    def get_all(self):
        return self.db.query(Department).all()
    
    def get_by_id(self, dept_id: int) -> Department:
        return self.db.query(Department).filter(Department.id == dept_id).first()
