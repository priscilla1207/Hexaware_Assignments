from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.base import Base, engine
from app.middleware.logging import log_requests
from app.middleware.exception_handler import validation_exception_handler, general_exception_handler
from fastapi.exceptions import RequestValidationError
from app.routers import auth_router, superadmin_router, itadmin_router, manager_router, employee_router

# Import all models to ensure they're registered with SQLAlchemy
from app.models.user import User
from app.models.department import Department
from app.models.asset import Asset
from app.models.asset_assignment import AssetAssignment
from app.models.asset_request import AssetRequest

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Enterprise Asset Management System", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware
app.middleware("http")(log_requests)

# Exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Routers
app.include_router(auth_router.router)
app.include_router(superadmin_router.router)
app.include_router(itadmin_router.router)
app.include_router(manager_router.router)
app.include_router(employee_router.router)

@app.get("/")
def root():
    return {"message": "Enterprise Asset Management System API"}
