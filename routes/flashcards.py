from fastapi import APIRouter, Depends, HTTPException
from routes.auth import get_current_user
from db import get_db
from models.flashcard_model import FlashcardCreate, FlashcardReview
from services.learning_service import create_flashcard, get_due_flashcards, process_flashcard_review

router = APIRouter(prefix="/flashcards", tags=["flashcards"])

@router.get("/due")
def get_due_cards(current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    return get_due_flashcards(db, current_user['username'])

@router.post("/")
def add_flashcard(item: FlashcardCreate, current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    card = create_flashcard(db, current_user['username'], item.topic_id, item.question, item.answer)
    return {"message": "Flashcard created", "card": card}

@router.post("/review")
def review_flashcard(review: FlashcardReview, current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    card = process_flashcard_review(db, current_user['username'], review.flashcard_id, review.quality)
    if not card:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return {"message": "Review recorded", "next_review_date": card['next_review_date']}
