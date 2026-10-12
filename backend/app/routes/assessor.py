from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import WorkerProfile
from app.services.qualification import build_candidate_matches
from app.schemas import WorkerProfileCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/worker/summary")
def worker_summary(db: Session = Depends(get_db)):
    profile = db.query(WorkerProfile).first()
    return {
        "worker_id": profile.worker_id,
        "status": profile.status,
        "trade": profile.primary_trade,
        "years_experience": profile.years_experience,
        "ai_summary": profile.ai_summary,
        "ai_suggestions": profile.ai_suggestions,
    }


@router.post("/worker/profile")
def save_profile(payload: WorkerProfileCreate, db: Session = Depends(get_db)):
    profile = db.query(WorkerProfile).first()
    if not profile:
        profile = WorkerProfile(
            user_id=1,
            worker_id="KS-2026001",
            status="Draft",
            ai_summary="AI summary pending.",
            ai_suggestions=["Complete missing evidence"],
        )
        db.add(profile)
        db.commit()

    for key, value in payload.model_dump(exclude_none=True).items():
        setattr(profile, key, value)
    profile.status = "Submitted"
    profile.ai_summary = "Strong skill alignment with electrician trade. Requires verification for safety and fault diagnosis steps."
    profile.ai_suggestions = ["Add evidence for fault-finding", "Confirm PPE and safety checklist"]
    db.commit()
    return {"status": "saved", "worker_id": profile.worker_id}


@router.get("/worker/qualifications")
def worker_qualifications(db: Session = Depends(get_db)):
    profile = db.query(WorkerProfile).first()
    text = " ".join(filter(None, [
        profile.primary_trade,
        profile.tasks_performed,
        profile.tools_used,
        profile.previous_training,
        profile.evidence_summary,
    ]))
    return {"matches": build_candidate_matches(text)}
