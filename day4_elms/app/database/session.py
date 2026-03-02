from app.database.base import SessionLocal

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
