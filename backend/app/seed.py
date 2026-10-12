from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import QualificationPack

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/qualifications")
def qualifications(db: Session = Depends(get_db)):
    packs = db.query(QualificationPack).all()
    return {"packs": [{
        "code": p.code,
        "title": p.title,
        "nsqf_level": p.nsqf_level,
        "verification_status": p.verification_status,
        "criteria": p.criteria,
    } for p in packs]}
