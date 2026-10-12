from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Assessment

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/reports/assessment/{assessment_id}")
def assessment_report(assessment_id: int, db: Session = Depends(get_db)):
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return {
        "worker_reference_id": "KS-2026001",
        "trade": assessment.selected_trade,
        "qualification": "QP-ELC-01",
        "verification_status": "Demonstration record; requires official verification.",
        "assessment_date": assessment.created_at.isoformat(),
        "final_recommendation": assessment.recommendation,
        "report_disclaimer": "This report supports Recognition of Prior Learning assessment. It is not a certificate. Final assessment and certification decisions must be made by the appropriate authorised human assessor and certification authority.",
        "rubric": assessment.rubric,
    }
