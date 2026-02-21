def check_malicious(query: str) -> bool:
    blocked_phrases = [
        "ignore previous instructions",
        "reveal system prompt",
        "override rules",
        "jailbreak",
        "act as"
    ]

    query = query.lower()

    return any(phrase in query for phrase in blocked_phrases)


