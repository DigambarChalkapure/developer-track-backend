from fastapi import APIRouter, Depends
from db import get_db
from services.analytics_service import get_user_analytics
from routes.auth import get_current_user

router = APIRouter(prefix="/progress", tags=["progress"])

@router.get("/")
def get_progress(current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    data = get_user_analytics(db, current_user['username'])
    return data['progress']
