from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from services.topic_service import get_user_roadmap, update_topic_progress
from models.topic_model import TopicUpdate
from routes.auth import get_current_user

router = APIRouter(prefix="/topics", tags=["topics"])

@router.get("/")
def get_topics(current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    return get_user_roadmap(db)

@router.get("/category/{name}")
def get_topics_by_category(name: str, current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    roadmap = get_user_roadmap(db)
    return [t for t in roadmap if t['category'].lower() == name.lower()]

@router.put("/{topic_id}")
def update_topic(topic_id: int, updates: TopicUpdate, current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    update_dict = updates.dict(exclude_unset=True)
    update_topic_progress(db, topic_id, update_dict)
    return {"message": f"Topic {topic_id} updated"}

@router.put("/{topic_id}/complete")
def complete_topic(topic_id: int, current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    update_topic_progress(db, topic_id, {"completed": True})
    return {"message": f"Topic {topic_id} marked as completed"}

@router.put("/{topic_id}/notes")
def update_topic_notes(topic_id: int, note: dict, current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    update_topic_progress(db, topic_id, {"notes": note.get("notes", "")})
    return {"message": f"Topic {topic_id} notes updated"}
