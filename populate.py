import json
import os

ROADMAP_FILE = r"C:\Users\ADMIN\.gemini\antigravity\scratch\developer_tracker\backend\data\roadmap.json"

def populate_roadmap():
    if not os.path.exists(ROADMAP_FILE):
        print("Roadmap file not found.")
        return

    with open(ROADMAP_FILE, 'r', encoding='utf-8') as f:
        topics = json.load(f)

    for topic in topics:
        subtopic = topic.get('subtopic', 'this topic')
        category = topic.get('category', 'this field')
        
        # Add basic subpoints if not present
        if 'subpoints' not in topic or not topic['subpoints']:
            topic['subpoints'] = [
                f"Core concepts and fundamentals of {subtopic}",
                f"Practical application and common use cases",
                f"Best practices and common pitfalls to avoid"
            ]
        
        # Add interview explanation if not present
        if 'interview_explanation' not in topic or not topic['interview_explanation']:
            topic['interview_explanation'] = f"In technical interviews, {subtopic} is a key indicator of your practical knowledge in {category}. Interviewers look for your ability to explain what it is, when to use it, and its underlying mechanics rather than just memorized definitions."
            
        # Add interview questions if not present
        if 'interview_questions' not in topic or not topic['interview_questions']:
            topic['interview_questions'] = [
                f"How would you explain {subtopic} to a junior developer?",
                f"Describe a scenario where you successfully implemented {subtopic} in a project.",
                f"What are the trade-offs or alternatives to using {subtopic}?"
            ]

    with open(ROADMAP_FILE, 'w', encoding='utf-8') as f:
        json.dump(topics, f, indent=4)
        
    print(f"Successfully populated {len(topics)} topics with interview details.")

if __name__ == "__main__":
    populate_roadmap()
