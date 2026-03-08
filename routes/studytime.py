from fastapi import APIRouter, Depends, Body
from db import get_db
from services.topic_service import get_studylogs, add_studylog
from models.topic_model import StudyLogCreate
from routes.auth import get_current_user

router = APIRouter(prefix="/studylog", tags=["studylog"])

@router.get("/")
def get_logs(current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    return get_studylogs(db)

@router.post("/")
def create_log(log: StudyLogCreate, current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    add_studylog(db, current_user['username'], log.topic_id, log.hours, log.date)
    return {"message": "Study log created"}
