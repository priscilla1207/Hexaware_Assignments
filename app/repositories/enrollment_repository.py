from sqlalchemy.orm import Session
from app.models.enrollment_model import Enrollment
from app.schemas.enrollment_schema import EnrollmentCreate

class EnrollmentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, enrollment: EnrollmentCreate) -> Enrollment:
        db_enrollment = Enrollment(**enrollment.model_dump())
        self.db.add(db_enrollment)
        self.db.commit()
        self.db.refresh(db_enrollment)
        return db_enrollment
    
    def exists(self, student_id: int, course_id: int) -> bool:
        return self.db.query(Enrollment).filter(
            Enrollment.student_id == student_id,
            Enrollment.course_id == course_id
        ).first() is not None
    
    def get_all(self) -> list[Enrollment]:
        return self.db.query(Enrollment).all()
    
    def get_by_student(self, student_id: int) -> list[Enrollment]:
        return self.db.query(Enrollment).filter(Enrollment.student_id == student_id).all()
