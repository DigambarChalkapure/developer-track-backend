import uuid
from datetime import datetime, timedelta
from pymongo.database import Database

# --- Flashcards ---
def create_flashcard(db: Database, username: str, topic_id: int, question: str, answer: str):
    card_id = str(uuid.uuid4())
    new_card = {
        "id": card_id,
        "username": username,
        "topic_id": topic_id,
        "question": question,
        "answer": answer,
        "next_review": datetime.utcnow().isoformat(),
        "interval": 0,
        "ease_factor": 2.5
    }
    db.flashcards.insert_one(new_card)
    return {
        "id": new_card["id"],
        "topic_id": new_card["topic_id"],
        "question": new_card["question"],
        "answer": new_card["answer"],
        "next_review_date": new_card["next_review"]
    }

def get_due_flashcards(db: Database, username: str):
    cards = list(db.flashcards.find({}, {"_id": 0}))
    now = datetime.utcnow()
    due_cards = []
    
    for c in cards:
        try:
            due_date = datetime.fromisoformat(c["next_review"])
        except ValueError:
            due_date = now # default to due if parse fails
        
        if due_date <= now:
            due_cards.append({
                "id": c["id"],
                "topic_id": c["topic_id"],
                "question": c["question"],
                "answer": c["answer"],
                "next_review_date": c["next_review"]
            })
    return due_cards

def process_flashcard_review(db: Database, username: str, flashcard_id: str, quality: int):
    # Ensure flashcard_id is treated as string since we use UUIDs now
    c = db.flashcards.find_one({"id": str(flashcard_id)})
    if not c: return None
    
    repetitions = c["interval"] if c["interval"] > 0 else 0
    interval_days = c["interval"]
    
    if quality < 3:
        repetitions = 0
        interval_days = 1
    else:
        if repetitions == 0:
            interval_days = 1
        elif repetitions == 1:
            interval_days = 6
        else:
            interval_days = round(interval_days * c["ease_factor"])
        
        repetitions += 1
        
    new_ease = c["ease_factor"] + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    if new_ease < 1.3:
        new_ease = 1.3
        
    next_date = datetime.utcnow() + timedelta(days=interval_days)
    
    db.flashcards.update_one(
        {"id": str(flashcard_id)},
        {"$set": {
            "interval": interval_days,
            "ease_factor": new_ease,
            "next_review": next_date.isoformat()
        }}
    )
    
    return {"id": str(flashcard_id), "next_review_date": next_date.isoformat()}

# --- Quests & Stats ---
def get_user_stats(db: Database, username: str):
    stat = db.user_stats.find_one({"username": username})
    if not stat:
        stat = {
            "username": username,
            "xp": 0,
            "completed_quests": [],
            "unlocked_badges": []
        }
        db.user_stats.insert_one(stat)
        
    return {
        "username": username,
        "total_xp": stat["xp"],
        "completed_quests": stat["completed_quests"],
        "badges": stat["unlocked_badges"]
    }

def get_quests(username: str):
    return [
       {"topic_id": 1, "title": "Internet Architect", "description": "Explain how DNS works in your own words in the reflection journal.", "xp_reward": 50},
       {"topic_id": 2, "title": "HTML Hero", "description": "Build a personal portfolio skeleton using only semantic HTML5 tags.", "xp_reward": 100},
       {"topic_id": 3, "title": "CSS Maestro", "description": "Style a cute button using pure CSS flexbox and hover effects.", "xp_reward": 100},
       {"topic_id": 4, "title": "JS Ninja", "description": "Write a function that reverses a string and share it in your notes.", "xp_reward": 150},
       {"topic_id": 10, "title": "React Rookie", "description": "Build a simple increment/decrement counter using useState.", "xp_reward": 200},
       {"topic_id": 16, "title": "Backend Boss", "description": "Create a simple Express or FastAPI hello-world endpoint.", "xp_reward": 250},
    ]

def complete_quest(db: Database, username: str, topic_id: int):
    stat = db.user_stats.find_one({"username": username})
    if not stat:
        stat = {
            "username": username,
            "xp": 0,
            "completed_quests": [],
            "unlocked_badges": []
        }
        db.user_stats.insert_one(stat)
        
    completed_quests = stat["completed_quests"]
    badges = stat["unlocked_badges"]
    
    if topic_id in completed_quests:
        return {"username": username, "total_xp": stat["xp"], "completed_quests": completed_quests, "badges": badges}
        
    quests = get_quests(username)
    quest = next((q for q in quests if q['topic_id'] == topic_id), None)
    xp = quest['xp_reward'] if quest else 50
    
    completed_quests.append(topic_id)
    new_xp = stat["xp"] + xp
    
    if len(completed_quests) == 1 and "First Quest" not in badges:
        badges.append("First Quest")
    if new_xp >= 500 and "XP Bronze" not in badges:
        badges.append("XP Bronze")
    if new_xp >= 1000 and "XP Silver" not in badges:
        badges.append("XP Silver")
        
    db.user_stats.update_one(
        {"username": username},
        {"$set": {
            "xp": new_xp,
            "completed_quests": completed_quests,
            "unlocked_badges": badges
        }}
    )
    
    return {"username": username, "total_xp": new_xp, "completed_quests": completed_quests, "badges": badges}
