from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import WorkerProfile
from app.schemas import WorkerProfileCreate
from app.services.qualification import build_candidate_matches, build_ai_assessment_summary

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
    if not profile:
        return {"worker_id": None, "status": "Draft", "trade": None, "years_experience": 0}
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
            ai_summary="AI suggestions pending.",
            ai_suggestions=["Update missing information"],
        )
        db.add(profile)

    for field, value in payload.model_dump(exclude_none=True).items():
        setattr(profile, field, value)

    profile.status = "Submitted"
    profile.ai_summary = "Strong alignment with electrician trade. Human review is required for safety and fault diagnosis evidence."
    profile.ai_suggestions = ["Add evidence for live testing", "Verify safety compliance"]
    db.commit()
    return {"status": "saved", "worker_id": profile.worker_id}


@router.get("/worker/qualifications")
def worker_qualifications(db: Session = Depends(get_db)):
    profile = db.query(WorkerProfile).first()
    if not profile:
        return {"matches": []}

    text = " ".join(filter(None, [
        profile.primary_trade,
        profile.tasks_performed,
        profile.tools_used,
        profile.previous_training,
        profile.evidence_summary,
    ]))
    return {
        "matches": build_candidate_matches(text),
        "ai_summary": build_ai_assessment_summary(text),
    }
