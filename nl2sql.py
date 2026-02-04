# nl2sql_multi_db.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from module.query_engine import get_sql_query
from module.sql_utils import execute_query, get_current_schema
from module.download_utils import download_button
from module.memory import build_conversation_context
from module.safety import is_safe_query
from module.explain import explain_query

load_dotenv()
st.set_page_config(page_title="QueryMind AI - MultiDB", layout="wide")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛠️ Database Connection & Schema")

db_type = st.sidebar.selectbox("Select Database Type", ["SQLite", "MySQL", "PostgreSQL"])
conn_params = {}

if db_type == "SQLite":
    conn_params["db_path"] = st.sidebar.text_input("SQLite DB Path:", "nour.db")
else:
    conn_params["host"] = st.sidebar.text_input("Host:", "localhost")
    conn_params["user"] = st.sidebar.text_input("User:", "root")
    conn_params["password"] = st.sidebar.text_input("Password:", "", type="password")
    conn_params["db_name"] = st.sidebar.text_input("Database Name:", "testdb")

st.sidebar.subheader("📊 Current Schema")
st.sidebar.code(get_current_schema(db_type, **conn_params))

st.sidebar.subheader("🛠️ Manual SQL Executor")
sql_input = st.sidebar.text_area("Run SQL manually:", height=200)
if st.sidebar.button("Execute SQL"):
    result, _ = execute_query(db_type, sql_input, **conn_params)
    if isinstance(result, str) and result.startswith("SQL Error"):
        st.sidebar.error(result)
    else:
        st.sidebar.success("SQL executed successfully!")

# ---------------- MAIN UI ----------------
st.title("🧠 QueryMind AI — Multi-DB Agent")
st.markdown("Ask in plain English. I generate SQL, run it, explain it, and auto-plot results.")

user_input = st.chat_input("Ask about your data")
if user_input:
    st.session_state.chat_history.append(("user", user_input))

    schema = get_current_schema(db_type, **conn_params)
    memory_context = build_conversation_context(st.session_state.chat_history)

    # Generate SQL
    with st.spinner("🧠 Generating SQL..."):
        sql_query = get_sql_query(user_input, schema, memory_context)

    # Safety check
    if not is_safe_query(sql_query):
        st.session_state.chat_history.append(("error", "⚠ Unsafe query blocked!"))
    else:
        st.session_state.chat_history.append(("assistant", sql_query))

        # Execute SQL
        with st.spinner("📊 Running query..."):
            result, columns = execute_query(db_type, sql_query, **conn_params)

        if isinstance(result, str) and result.startswith("SQL Error"):
            st.session_state.chat_history.append(("error", result))
        else:
            st.session_state.chat_history.append(("result", (result, columns)))

            # Explain SQL
            explanation = explain_query(sql_query)
            st.session_state.chat_history.append(("assistant", f"🧠 Explanation:\n{explanation}"))

            # Auto Chart
            df = pd.DataFrame(result, columns=columns)
            if not df.empty:
                st.subheader("📈 Auto Chart")
                try:
                    numeric_cols = df.select_dtypes(include="number").columns.tolist()
                    if numeric_cols:
                        df[numeric_cols].plot(kind="bar", figsize=(8,4))
                        st.pyplot(plt)
                        plt.clf()
                except:
                    st.info("Chart could not be generated automatically.")

# ---------------- RENDER CHAT HISTORY ----------------
for role, content in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(content)
    elif role == "assistant":
        with st.chat_message("assistant"):
            if content.strip().lower().startswith("select"):
                st.code(content, language="sql")
            else:
                st.markdown(content)
    elif role == "error":
        with st.chat_message("assistant"):
            st.error(content)
    elif role == "result":
        df = pd.DataFrame(content[0], columns=content[1])
        with st.chat_message("assistant"):
            st.dataframe(df, use_container_width=True)

# ---------------- DOWNLOAD ----------------
download_button(st.session_state.chat_history)
