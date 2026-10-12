from pydantic import BaseModel
from typing import Optional, List


class UserLoginRequest(BaseModel):
    email: str
    password: str


class WorkerProfileCreate(BaseModel):
    name: Optional[str] = None
    preferred_language: Optional[str] = "Hindi"
    state: Optional[str] = None
    district: Optional[str] = None
    primary_trade: Optional[str] = None
    years_experience: Optional[float] = 0
    employment_type: Optional[str] = None
    tasks_performed: Optional[str] = None
    tools_used: Optional[str] = None
    previous_training: Optional[str] = None
    certifications: Optional[str] = None
    industries: Optional[str] = None
    evidence_summary: Optional[str] = None


class AssessmentScoreRequest(BaseModel):
    worker_id: int
    assessor_id: int
    selected_trade: str
    rubric: List[dict]
    recommendation: Optional[str] = "Pending"
