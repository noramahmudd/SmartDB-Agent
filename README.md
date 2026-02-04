<img width="1536" height="1024" alt="ChatGPT Image Feb 4, 2026, 08_08_56 AM" src="https://github.com/user-attachments/assets/f27519c0-ea9a-4e8e-9da2-06922cd0afe2" />
# 🧠 QueryMind AI — Intelligent Multi-Database SQL Agent

**QueryMind AI** 
is an AI-powered data assistant that lets users **talk to their databases in plain English** and receive **real SQL queries, live results, explanations, and automatic visualizations**.

It combines **LLMs + Databases + Data Visualization** into one intelligent system.

---

## 🚀 What This Project Does

You can:

✔ Ask questions about your database in natural language  
✔ Automatically generate SQL queries using an LLM  
✔ Execute queries in real time  
✔ View results as structured tables  
✔ Get automatic charts from query results  
✔ Receive AI explanations of the generated SQL  
✔ Create tables or insert data manually  
✔ Download the full conversation history  
✔ Connect to multiple database types  

---

## 🧩 Supported Data Sources

| Data Source | Supported |
|------------|-----------|
| SQLite | ✅ |
| MySQL | ✅ |
| PostgreSQL | ✅ |
| CSV Files | ✅ |

---
## 🏗️ System Architecture

**User → Streamlit UI → LLM (Groq) → SQL Generator → Safety Check → Database Engine → Results → Auto Charts → SQL Explanation → Memory**

This allows the system to behave like an **AI Data Agent**, not just a chatbot.

---

## 🧠 AI Capabilities

- Natural Language → SQL conversion  
- Context-aware conversation memory  
- SQL safety filtering (blocks dangerous queries)  
- Plain-English SQL explanations  
- Automatic chart selection from results  

---

## 📊 Auto Visualization

QueryMind selects charts automatically:

| Data Pattern | Chart Type |
|-------------|------------|
| Category + Numeric | Bar Chart |
| Date + Numeric | Line Chart |
| Two Numeric Columns | Scatter Plot |
| One Numeric Column | Histogram |

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| UI | Streamlit |
| LLM | Groq (LLaMA 3.1 8B) |
| Framework | LangChain |
| Databases | SQLite, MySQL, PostgreSQL |
| Data Processing | Pandas |
| Charts | Matplotlib |
| Agent Logic | Custom Python Modules |

---
## 📁 Project Structure

project/
│
├── nl2sql.py # Main Streamlit application
├── module/
│ ├── config.py # API keys & settings
│ ├── query_engine.py # LLM → SQL generation
│ ├── sql_utils.py # Multi-database execution
│ ├── safety.py # Query protection layer
│ ├── memory.py # Conversation memory
│ ├── explain.py # SQL explanation engine
│ ├── download_utils.py # Chat export functionality
│
└── requirements.txt
---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/querymind-ai.git
cd querymind-ai

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```
🔑 Environment Variables

Create a .env file:
GROQ_API_KEY=your_key_here
---
▶ Run the App
streamlit run nl2sql.py
---
💬 Example Questions

“Show total sales by product”

“Who are the top 5 students by score?”

“Average revenue per month”

“How many users signed up this year?”
---
🔒 Safety Features

The system blocks harmful SQL such as:

DROP TABLE

DELETE FROM

ALTER DATABASE

TRUNCATE

This protects your database from destructive operations.
---
🎯 Why This Project Is Powerful

This is not just text-to-SQL.
It behaves like a real AI Data Agent that can:

✔ Understand context
✔ Generate accurate queries
✔ Explain its logic
✔ Visualize results
✔ Work with multiple databases
---
👩‍💻 Author

Nourhan Mahmoud
AI Engineer | LLMs • Agents • Computer Vision




