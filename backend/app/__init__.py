from app.db import SessionLocal
from app.models import User, WorkerProfile, QualificationPack, Assessment
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(value: str):
    return pwd_context.hash(value)


def seed_data():
    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            db.add_all([
                User(name="Asha Worker", email="worker@demo.local", password=hash_password("demo123"), role="worker", language="Hindi"),
                User(name="Rahul Assessor", email="assessor@demo.local", password=hash_password("demo123"), role="assessor", language="English"),
                User(name="Meera Admin", email="admin@demo.local", password=hash_password("demo123"), role="admin", language="Hindi"),
            ])
            db.commit()

        if db.query(WorkerProfile).count() == 0:
            worker = db.query(User).filter(User.role == "worker").first()
            db.add(WorkerProfile(
                user_id=worker.id,
                worker_id="KS-2026001",
                age=29,
                state="Maharashtra",
                district="Nagpur",
                preferred_language="Hindi",
                primary_trade="Electrician",
                years_experience=6,
                employment_type="Daily wage",
                tasks_performed="Installed switchboards, changed MCBs, repaired wiring, tested continuity.",
                tools_used="Multimeter, screwdrivers, pliers, electrical test lamp.",
                previous_training="Industrial safety and wiring training",
                certifications="None",
                industries="Construction and electrical maintenance",
                evidence_summary="Safety checklist and installation photos submitted.",
                status="Submitted",
                ai_summary="Strong fit for electrician trade but missing fault diagnosis evidence.",
                ai_suggestions=["Add evidence for fault-finding", "Confirm PPE compliance"],
            ))
            db.commit()

        if db.query(QualificationPack).count() == 0:
            db.add_all([
                QualificationPack(
                    code="QP-ELC-01",
                    title="Electrician General (Demonstration)",
                    nsqf_level="Level 4",
                    description="Demonstration electrician pack for evaluation and testing.",
                    verification_status="Demonstration record; requires official verification.",
                    source_notice="Synthetic demonstration data. Official verification required.",
                    criteria=["Tool identification", "Electrical safety", "Wiring installation", "Fault diagnosis", "Testing equipment use"],
                ),
                QualificationPack(
                    code="QP-WIRE-02",
                    title="Domestic Wiring Technician",
                    nsqf_level="Level 3",
                    description="Residential installation and maintenance support.",
                    verification_status="Demonstration record; requires official verification.",
                    source_notice="Synthetic demonstration data. Official verification required.",
                    criteria=["Basic wiring layout", "Switchboard installation", "Safety compliance", "Testing and troubleshooting"],
                ),
            ])
            db.commit()

        if db.query(Assessment).count() == 0:
            worker = db.query(WorkerProfile).first()
            assessor = db.query(User).filter(User.role == "assessor").first()
            db.add(Assessment(
                worker_id=worker.id,
                assessor_id=assessor.id,
                selected_trade="Electrician",
                status="Completed",
                score=72,
                recommendation="Recommended for review",
                rubric=[
                    {"criterion": "Tool identification", "score": 3, "status": "satisfactory"},
                    {"criterion": "Electrical safety", "score": 2, "status": "satisfactory"},
                    {"criterion": "Wiring task", "score": 2, "status": "satisfactory"},
                    {"criterion": "Risk identification", "score": 1, "status": "insufficient evidence"},
                ],
                audit_history=[{"actor": "Rahul Assessor", "action": "Score updated", "timestamp": datetime.utcnow().isoformat()}],
            ))
            db.commit()
    finally:
        db.close()
