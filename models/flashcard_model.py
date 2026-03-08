from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Flashcard(BaseModel):
    id: str  # e.g., UUID string
    topic_id: int
    question: str
    answer: str
    username: str

class FlashcardReview(BaseModel):
    flashcard_id: str
    quality: int  # 0-5 scale of how well they knew it

class FlashcardCreate(BaseModel):
    topic_id: int
    question: str
    answer: str
