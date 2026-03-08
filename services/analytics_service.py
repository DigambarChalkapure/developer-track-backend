from services.topic_service import get_user_roadmap, get_studylogs

def get_user_analytics(db, username: str):
    roadmap = get_user_roadmap(db)
    studylogs = get_studylogs(db)

    total_topics = len(roadmap)
    completed_topics = sum(1 for t in roadmap if t.get('completed', False))
    remaining = total_topics - completed_topics
    percentage = round((completed_topics / total_topics * 100) if total_topics > 0 else 0, 1)

    categories = set(t['category'] for t in roadmap)
    
    category_progress = []
    for cat in categories:
        cat_topics = [t for t in roadmap if t['category'] == cat]
        cat_completed = sum(1 for t in cat_topics if t.get('completed', False))
        category_progress.append({
            "category": cat,
            "total": len(cat_topics),
            "completed": cat_completed,
            "percentage": round((cat_completed / len(cat_topics) * 100) if len(cat_topics) > 0 else 0, 1)
        })
        
    category_progress.sort(key=lambda x: x['total'], reverse=True)

    # Study Hours
    study_hours_by_cat = {cat: 0 for cat in categories}
    total_hours = 0
    topic_map = {t['id']: t['category'] for t in roadmap}
    
    for log in studylogs:
        hrs = log.get('hours', 0)
        total_hours += hrs
        tid = log.get('topic_id')
        cat = topic_map.get(tid)
        if cat:
            study_hours_by_cat[cat] += hrs

    study_chart_data = [{"category": k, "hours": round(v, 2)} for k, v in study_hours_by_cat.items()]

    return {
        "progress": {
            "total": total_topics,
            "completed": completed_topics,
            "remaining": remaining,
            "percentage": percentage
        },
        "category_progress": category_progress,
        "study_hours_chart": study_chart_data,
        "total_study_hours": round(total_hours, 2)
    }
