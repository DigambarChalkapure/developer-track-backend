from datetime import datetime
from pymongo.database import Database

def seed_master_roadmap(db: Database, topics_data: list):
    # Only seed if db is empty to avoid overwriting user progress during redeploys
    if db.topics.count_documents({}) > 0:
        return
        
    for t_data in topics_data:
        topic_doc = {
            "id": t_data.get('id'),
            "category": t_data.get('category'),
            "topic": t_data.get('topic'),
            "subtopic": t_data.get('subtopic'),
            "completed": t_data.get('completed', False),
            "difficulty": t_data.get('difficulty', 'medium'),
            "estimated_hours": t_data.get('estimated_hours', 2),
            "notes": t_data.get('notes', ''),
            "feynman_reflection": t_data.get('feynman_reflection', ''),
            "subpoints": t_data.get('subpoints', []),
            "interview_explanation": t_data.get('interview_explanation', ''),
            "interview_questions": t_data.get('interview_questions', []),
            "last_updated": t_data.get('last_updated', '')
        }
        db.topics.insert_one(topic_doc)

def get_user_roadmap(db: Database):
    # Returns all topics. In a multi-user app we'd filter by user_id or username
    # Exclude _id to avoid serialization issues
    topics = list(db.topics.find({}, {"_id": 0}).sort("id", 1))
    return topics

def update_topic_progress(db: Database, topic_id: int, updates: dict):
    # Remove any None values from updates
    updates = {k: v for k, v in updates.items() if v is not None}
    
    updates['last_updated'] = datetime.utcnow().isoformat()
    
    db.topics.update_one(
        {"id": topic_id},
        {"$set": updates}
    )
    return get_user_roadmap(db)

def get_studylogs(db: Database):
    logs = list(db.studylogs.find({}, {"_id": 0}).sort("date", -1))
    return logs

def add_studylog(db: Database, username: str, topic_id: int, hours: float, date: str):
    log_doc = {
        "username": username,
        "topic_id": topic_id,
        "hours": hours,
        "date": date
    }
    db.studylogs.insert_one(log_doc)
    return get_studylogs(db)
