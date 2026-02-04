from langchain_groq import ChatGroq
from module.config import GROQ_API_KEY, MODEL_NAME

def explain_query(sql_query: str) -> str:
    llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=MODEL_NAME)
    return llm.invoke(f"Explain this SQL query in simple English:\n{sql_query}").content
