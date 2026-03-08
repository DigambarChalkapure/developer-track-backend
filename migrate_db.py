import json
import os
from db import engine, SessionLocal
from models.schema import Base
from services.topic_service import seed_master_roadmap

ROADMAP_FILE = os.path.join(os.path.dirname(__file__), 'data', 'roadmap.json')

def init_db():
    # 1. Create all SQL tables defined in schema.py
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    # 2. Seed initial roadmap data if available
    if os.path.exists(ROADMAP_FILE):
        print(f"Found {ROADMAP_FILE}, seeding initial data...")
        with open(ROADMAP_FILE, 'r', encoding='utf-8') as f:
            topics_data = json.load(f)
            
        db = SessionLocal()
        try:
            seed_master_roadmap(db, topics_data)
            print(f"Successfully migrated {len(topics_data)} topics to the database.")
        finally:
            db.close()
    else:
        print("No roadmap.json found to seed.")

if __name__ == "__main__":
    init_db()
