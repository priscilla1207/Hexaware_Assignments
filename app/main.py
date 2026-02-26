from fastapi import FastAPI
from app.core.db import init_db
from app.middleware.cors import setup_cors
from app.controllers import student_controller, course_controller, enrollment_controller

app = FastAPI(
    title="Learning Management System",
    description="Course Enrollment Platform API",
    version="1.0.0"
)

setup_cors(app)

app.include_router(student_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def root():
    return {"message": "LMS API is running. Visit /docs for API documentation"}
