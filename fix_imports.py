import os
import glob

files = glob.glob('c:/Users/ADMIN/.gemini/antigravity/scratch/developer_tracker/backend/**/*.py', recursive=True)

for file in files:
    if 'venv' in file:
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    new_content = content.replace('from routes', 'from routes')
    new_content = new_content.replace('from models', 'from models')
    new_content = new_content.replace('from services', 'from services')
    new_content = new_content.replace('from routes.auth', 'from routes.auth')
    new_content = new_content.replace('from services.topic_service', 'from services.topic_service')

    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
