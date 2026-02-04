FORBIDDEN_KEYWORDS = ["drop", "delete", "alter", "truncate"]

def is_safe_query(query: str) -> bool:
    return not any(word in query.lower() for word in FORBIDDEN_KEYWORDS)
