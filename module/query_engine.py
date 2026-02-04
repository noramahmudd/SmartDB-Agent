from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from module.config import GROQ_API_KEY, MODEL_NAME

def get_sql_query(user_query: str, schema: str, memory_context: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
You are an AI Database Agent.

Conversation History:
{memory}

Database Schema:
{schema}

Rules:
- Generate safe SQL only
- No destructive queries
- Return only SQL

User Question: {question}
SQL:
""")

    llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=MODEL_NAME)
    chain = prompt | llm | StrOutputParser()

    return chain.invoke({
        "question": user_query,
        "schema": schema,
        "memory": memory_context
    }).strip()
