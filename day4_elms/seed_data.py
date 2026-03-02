from sqlalchemy.orm import Session
from app.database.base import SessionLocal, engine, Base
from app.core.security import get_password_hash

# Import all models
from app.models.user import User
from app.models.department import Department
from app.models.leave_request import LeaveRequest

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).first():
            print("Database already seeded")
            return
        
        # Create departments
        it_dept = Department(id=1, name="IT Department")
        hr_dept = Department(id=2, name="HR Department")
        finance_dept = Department(id=3, name="Finance Department")
        
        db.add_all([it_dept, hr_dept, finance_dept])
        db.commit()
        
        # Create users
        users = [
            User(name="Admin User", email="admin@company.com", 
                 password=get_password_hash("admin123"), role="ADMIN", department_id=1),
            User(name="Manager IT", email="manager@company.com", 
                 password=get_password_hash("manager123"), role="MANAGER", department_id=1),
            User(name="Employee One", email="employee@company.com", 
                 password=get_password_hash("employee123"), role="EMPLOYEE", department_id=1),
            User(name="Employee Two", email="employee2@company.com", 
                 password=get_password_hash("employee123"), role="EMPLOYEE", department_id=2),
        ]
        
        db.add_all(users)
        db.commit()
        
        # Update department manager
        it_dept.manager_id = 2  # Manager IT
        db.commit()
        
        print("Database seeded successfully!")
        
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
