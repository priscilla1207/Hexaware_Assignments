from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # SUPERADMIN, IT_ADMIN, MANAGER, EMPLOYEE
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    
    department = relationship("Department", back_populates="users", foreign_keys=[department_id])
    assignments = relationship("AssetAssignment", back_populates="user")
    requests = relationship("AssetRequest", foreign_keys="AssetRequest.employee_id", back_populates="employee")
