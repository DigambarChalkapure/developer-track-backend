from fastapi import APIRouter, Depends
from db import get_db
from services.analytics_service import get_user_analytics
from routes.auth import get_current_user

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/")
def get_analytics(current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    return get_user_analytics(db, current_user['username'])
