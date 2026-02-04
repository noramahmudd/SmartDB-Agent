def build_conversation_context(history):
    context = ""
    for role, content in history[-5:]:
        if role == "user":
            context += f"User asked: {content}\n"
        elif role == "assistant":
            context += f"SQL used: {content}\n"
    return context
