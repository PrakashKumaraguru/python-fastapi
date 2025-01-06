from sqlalchemy.orm import Session
from app.models.user_model import User
from pydantic import BaseModel
from fastapi import HTTPException

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str

def create_user(db: Session, user: UserCreate):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
