from fastapi import HTTPException
from app.repositories.student_repository import StudentRepository
from app.schemas.student_schema import StudentCreate, StudentResponse

class StudentService:
    def __init__(self, repository: StudentRepository):
        self.repository = repository
    
    def create_student(self, student: StudentCreate) -> StudentResponse:
        db_student = self.repository.create(student)
        return StudentResponse.model_validate(db_student)
    
    def get_student(self, student_id: int) -> StudentResponse:
        student = self.repository.get_by_id(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return StudentResponse.model_validate(student)
