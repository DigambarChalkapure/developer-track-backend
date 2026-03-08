from fastapi import APIRouter, Depends, HTTPException
from routes.auth import get_current_user
from db import get_db
from services.learning_service import get_user_stats, get_quests, complete_quest
from models.quest_model import UserStats

router = APIRouter(prefix="/quests", tags=["quests"])

@router.get("/stats")
def fetch_user_stats(current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    return get_user_stats(db, current_user['username'])

@router.get("/")
def fetch_available_quests(current_user: dict = Depends(get_current_user)):
    return get_quests(current_user['username'])

@router.post("/complete/{topic_id}")
def submit_quest(topic_id: int, current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    stats = complete_quest(db, current_user['username'], topic_id)
    return {"message": "Quest completed!", "stats": stats}
