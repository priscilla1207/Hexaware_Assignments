from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService

def get_student_service(db: Session = Depends(get_db)) -> StudentService:
    return StudentService(StudentRepository(db))

def get_course_service(db: Session = Depends(get_db)) -> CourseService:
    return CourseService(CourseRepository(db))

def get_enrollment_service(db: Session = Depends(get_db)) -> EnrollmentService:
    return EnrollmentService(
        EnrollmentRepository(db),
        StudentRepository(db),
        CourseRepository(db)
    )
