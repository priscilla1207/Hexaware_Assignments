from fastapi import APIRouter, Depends, status
from app.schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse, StudentEnrollmentResponse
from app.services.enrollment_service import EnrollmentService
from app.dependencies.dependencies import get_enrollment_service

router = APIRouter(tags=["Enrollments"])

@router.post("/enrollments", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll_student(enrollment: EnrollmentCreate, service: EnrollmentService = Depends(get_enrollment_service)):
    return service.enroll_student(enrollment)

@router.get("/enrollments", response_model=list[EnrollmentResponse])
def get_all_enrollments(service: EnrollmentService = Depends(get_enrollment_service)):
    return service.get_all_enrollments()

@router.get("/students/{student_id}/enrollments", response_model=list[StudentEnrollmentResponse])
def get_student_enrollments(student_id: int, service: EnrollmentService = Depends(get_enrollment_service)):
    return service.get_student_enrollments(student_id)
