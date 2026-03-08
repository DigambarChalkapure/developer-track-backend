from pydantic import BaseModel, Field
from typing import Optional, List

class Topic(BaseModel):
    id: int
    category: str
    topic: str
    subtopic: str
    completed: bool = False
    difficulty: str = "medium"
    estimated_hours: int = 2
    notes: str = ""
    feynman_reflection: str = ""
    subpoints: List[str] = Field(default_factory=list)
    interview_explanation: str = ""
    interview_questions: List[str] = Field(default_factory=list)
    last_updated: str = ""

class TopicUpdate(BaseModel):
    completed: Optional[bool] = None
    notes: Optional[str] = None
    difficulty: Optional[str] = None
    feynman_reflection: Optional[str] = None
    subpoints: Optional[List[str]] = None
    interview_explanation: Optional[str] = None
    interview_questions: Optional[List[str]] = None

class StudyLogCreate(BaseModel):
    topic_id: int
    hours: float
    date: str  # YYYY-MM-DD
