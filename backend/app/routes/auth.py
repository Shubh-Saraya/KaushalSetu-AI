from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas import UserLoginRequest, WorkerProfileCreate, AssessmentScoreRequest
from app.models import User, WorkerProfile, Assessment, QualificationPack, AuditLog
from app.services.qualification import build_candidate_matches, assessment_suggestion
from app.db import SessionLocal
from app.seed import seed_data

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
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if payload.password != "demo123":
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
    user = db.query(User).filter(User.role == "worker").first()
    existing = db.query(WorkerProfile).filter(WorkerProfile.user_id == user.id).first()
    if existing:
        for field, value in payload.model_dump(exclude_none=True).items():
            setattr(existing, field, value)
        db.commit()
        return {"status": "updated", "worker_id": existing.worker_id}

    profile = WorkerProfile(
        user_id=user.id,
        worker_id="KS-2026002",
        preferred_language=payload.preferred_language,
        state=payload.state,
        district=payload.district,
        primary_trade=payload.primary_trade,
        years_experience=payload.years_experience,
        employment_type=payload.employment_type,
        tasks_performed=payload.tasks_performed,
        tools_used=payload.tools_used,
        previous_training=payload.previous_training,
        certifications=payload.certifications,
        industries=payload.industries,
        evidence_summary=payload.evidence_summary,
        status="Draft",
        ai_summary="AI suggestions pending review.",
        ai_suggestions=["Complete evidence confirmation", "Add missing safety observations"],
    )
    db.add(profile)
    db.commit()
    return {"status": "created", "worker_id": profile.worker_id}


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


@router.post("/assessments/score")
def score_assessment(payload: AssessmentScoreRequest, db: Session = Depends(get_db)):
    assessment = Assessment(
        worker_id=payload.worker_id,
        assessor_id=payload.assessor_id,
        selected_trade=payload.selected_trade,
        status="Assessment completed",
        score=sum(item["score"] for item in payload.rubric) / max(len(payload.rubric), 1),
        recommendation=payload.recommendation,
        rubric=payload.rubric,
        audit_history=[{"actor": "Assessor", "action": "Score recorded", "details": "Updated rubric values"}],
    )
    db.add(assessment)
    db.commit()
    return {"status": "saved", "assessment_id": assessment.id}


@router.get("/assessor/assignments")
def assessor_assignments(db: Session = Depends(get_db)):
    worker = db.query(WorkerProfile).first()
    return {
        "assigned_workers": [
            {
                "worker_id": worker.worker_id,
                "name": "Asha Worker",
                "trade": worker.primary_trade,
                "status": worker.status,
                "score": 72,
                "progress": 82,
            }
        ]
    }


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
