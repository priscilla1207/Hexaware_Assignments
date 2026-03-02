from sqlalchemy.orm import Session
from app.database.base import SessionLocal, engine, Base
from app.core.security import get_password_hash

# Import all models to ensure they're registered with SQLAlchemy
from app.models.user import User
from app.models.department import Department
from app.models.asset import Asset
from app.models.asset_assignment import AssetAssignment
from app.models.asset_request import AssetRequest

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
            User(name="Super Admin", email="superadmin@company.com", 
                 password=get_password_hash("admin123"), role="SUPERADMIN", department_id=1),
            User(name="IT Admin", email="itadmin@company.com", 
                 password=get_password_hash("admin123"), role="IT_ADMIN", department_id=1),
            User(name="Manager", email="manager@company.com", 
                 password=get_password_hash("manager123"), role="MANAGER", department_id=2),
            User(name="Employee", email="employee@company.com", 
                 password=get_password_hash("employee123"), role="EMPLOYEE", department_id=2),
        ]
        
        db.add_all(users)
        db.commit()
        
        print("Database seeded successfully!")
        
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
