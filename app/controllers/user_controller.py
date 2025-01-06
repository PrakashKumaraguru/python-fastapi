from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.user_service import create_user, UserCreate
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
