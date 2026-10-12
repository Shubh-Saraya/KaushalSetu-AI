from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import WorkerProfile, Assessment
from app.schemas import AssessmentScoreRequest

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/assessor/assignments")
def assessor_assignments(db: Session = Depends(get_db)):
    worker = db.query(WorkerProfile).first()
    return {
        "assigned_workers": [{
            "worker_id": worker.worker_id if worker else "KS-2026001",
            "name": "Asha Worker",
            "trade": worker.primary_trade if worker else "Electrician",
            "status": worker.status if worker else "Submitted",
            "score": 72,
            "progress": 82,
        }]
    }


@router.post("/assessments/score")
def score_assessment(payload: AssessmentScoreRequest, db: Session = Depends(get_db)):
    assessment = Assessment(
        worker_id=payload.worker_id,
        assessor_id=payload.assessor_id,
        selected_trade=payload.selected_trade,
        status="Completed",
        score=sum(item.get("score", 0) for item in payload.rubric) / max(len(payload.rubric), 1),
        recommendation=payload.recommendation,
        rubric=payload.rubric,
        audit_history=[{"actor": "Assessor", "action": "Score recorded"}],
    )
    db.add(assessment)
    db.commit()
    return {"status": "saved", "assessment_id": assessment.id}
