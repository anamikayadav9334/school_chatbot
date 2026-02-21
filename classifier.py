def classify_query(query: str) -> str:
    query = query.lower()

    if any(word in query for word in ["marks", "grade", "score", "result"]):
        return "marks"

    elif any(word in query for word in ["course", "subject", "offer", "program"]):
        return "courses"

    elif any(word in query for word in ["admission", "apply", "enroll"]):
        return "admission"

    elif any(word in query for word in ["ignore previous", "system prompt", "override"]):
        return "malicious"

    else:
        return "general"
