from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import User, WorkerProfile
from app.schemas import UserLoginRequest, WorkerProfileCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/auth/login")
def login(payload: UserLoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or payload.password != "demo123":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "token": f"demo-token-{user.id}",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "language": user.language,
        },
    }
