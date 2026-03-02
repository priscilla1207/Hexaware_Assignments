from sqlalchemy.orm import Session
from app.repositories.department_repo import DepartmentRepository
from app.schemas.department_schema import DepartmentCreate

class DepartmentService:
    def __init__(self, db: Session):
        self.dept_repo = DepartmentRepository(db)
    
    def create_department(self, department: DepartmentCreate):
        return self.dept_repo.create(department)
    
    def get_all_departments(self):
        return self.dept_repo.get_all()
