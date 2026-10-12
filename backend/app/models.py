from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    language = Column(String(50), default="Hindi")
    created_at = Column(DateTime, default=datetime.utcnow)

    profile = relationship("WorkerProfile", back_populates="user", uselist=False)
    assessments = relationship("Assessment", back_populates="assessor")


class WorkerProfile(Base):
    __tablename__ = "worker_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    worker_id = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    state = Column(String(200))
    district = Column(String(200))
    preferred_language = Column(String(50), default="Hindi")
    primary_trade = Column(String(200))
    years_experience = Column(Float, default=0)
    employment_type = Column(String(100))
    tasks_performed = Column(Text)
    tools_used = Column(Text)
    previous_training = Column(Text)
    certifications = Column(Text)
    industries = Column(Text)
    evidence_summary = Column(Text)
    status = Column(String(50), default="Draft")
    submitted_at = Column(DateTime, nullable=True)
    ai_summary = Column(Text)
    ai_suggestions = Column(JSON, default=list)

    user = relationship("User", back_populates="profile")


class QualificationPack(Base):
    __tablename__ = "qualification_packs"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(100), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    nsqf_level = Column(String(50), default="Level 3")
    description = Column(Text)
    verification_status = Column(String(100), default="Demonstration data")
    source_notice = Column(Text, default="Synthetic demonstration records. Requires official verification.")
    criteria = Column(JSON, default=list)


class EvidenceItem(Base):
    __tablename__ = "evidence_items"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("worker_profiles.id"))
    title = Column(String(200))
    file_type = Column(String(50))
    file_size_kb = Column(Integer)
    status = Column(String(50), default="Uploaded")
    notes = Column(Text)


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("worker_profiles.id"))
    assessor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    selected_trade = Column(String(200))
    status = Column(String(50), default="Under review")
    score = Column(Float, default=0)
    recommendation = Column(String(200), default="Pending")
    rubric = Column(JSON, default=list)
    audit_history = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    assessor = relationship("User", back_populates="assessments")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    actor = Column(String(200), nullable=False)
    action = Column(String(200), nullable=False)
    details = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
