from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import WorkerProfile, Assessment

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/admin/dashboard")
def admin_dashboard(db: Session = Depends(get_db)):
    workers = db.query(WorkerProfile).count()
    assessments = db.query(Assessment).count()
    return {
        "registered_workers": workers,
        "assessments_completed": assessments,
        "pending_assessments": 4,
        "average_completion_time_days": 3.4,
        "trade_distribution": [
            {"name": "Electrician", "value": 8},
            {"name": "Welder", "value": 2},
            {"name": "Plumber", "value": 1},
        ],
        "summary": "Synthetic demonstration analytics under human review.",
    }
