"""
One-time migration script: reads roadmap.json and seeds MongoDB Atlas.
Run this ONCE with: python migrate_mongo.py
"""
import json
import os
from db import db  # Uses MONGO_URI env var, falls back to default with embedded credentials

ROADMAP_FILE = os.path.join(os.path.dirname(__file__), 'data', 'roadmap.json')

def migrate():
    # Check if already seeded
    count = db.topics.count_documents({})
    if count > 0:
        print(f"Database already has {count} topics. Skipping seed.")
        return

    if not os.path.exists(ROADMAP_FILE):
        print(f"No roadmap.json found at {ROADMAP_FILE}. Cannot seed.")
        return

    with open(ROADMAP_FILE, 'r', encoding='utf-8') as f:
        topics_data = json.load(f)

    # Remove MongoDB _id issues by ensuring clean docs
    docs = []
    for t in topics_data:
        doc = {
            "id": t.get('id'),
            "category": t.get('category', ''),
            "topic": t.get('topic', ''),
            "subtopic": t.get('subtopic', ''),
            "completed": t.get('completed', False),
            "difficulty": t.get('difficulty', 'medium'),
            "estimated_hours": t.get('estimated_hours', 2),
            "notes": t.get('notes', ''),
            "feynman_reflection": t.get('feynman_reflection', ''),
            "subpoints": t.get('subpoints', []),
            "interview_explanation": t.get('interview_explanation', ''),
            "interview_questions": t.get('interview_questions', []),
            "last_updated": t.get('last_updated', '')
        }
        docs.append(doc)

    db.topics.insert_many(docs)
    
    # Create indexes for efficient queries
    db.topics.create_index("id", unique=True)
    db.topics.create_index("category")
    db.studylogs.create_index("date")
    db.flashcards.create_index("id", unique=True)
    db.user_stats.create_index("username", unique=True)
    
    print(f"SUCCESS: Migrated {len(docs)} topics to MongoDB Atlas!")
    print("SUCCESS: Created indexes on topics, studylogs, flashcards, and user_stats collections.")

if __name__ == "__main__":
    migrate()
