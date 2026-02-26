from fastapi import FastAPI
from app.core.config import init_db
from app.middleware.cors import setup_cors
from app.controllers import loan_controller

app = FastAPI(
    title="Loan Application & Approval Management System",
    description="Fintech Loan Processing API",
    version="1.0.0"
)

setup_cors(app)

app.include_router(loan_controller.router)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def root():
    return {"message": "Loan Management API is running. Visit /docs for API documentation"}
