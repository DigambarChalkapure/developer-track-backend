from pydantic import BaseModel
from typing import Optional, List

class QuestSubmission(BaseModel):
    topic_id: int
    project_url: str

class Quest(BaseModel):
    topic_id: int
    title: str
    description: str
    xp_reward: int

class UserStats(BaseModel):
    username: str
    total_xp: int = 0
    completed_quests: List[int] = [] # list of topic_ids
    badges: List[str] = []
