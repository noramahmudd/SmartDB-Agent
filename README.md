
![Uploading ChatGPT Image Feb 4, 2026, 08_08_56 AM.png…]()  

🧠 QueryMind AI — Intelligent Multi-Database SQL Agent

QueryMind AI is an AI-powered data assistant that allows users to talk to their database in plain English and get real SQL queries, results, explanations, and charts — instantly.

It combines LLMs + Databases + Visualization into one intelligent system.

🚀 What This Project Does

You can:

✔ Ask questions about your database in plain English
✔ Automatically generate SQL queries using an LLM
✔ Execute queries in real time
✔ Get results as tables
✔ See automatic charts based on the data
✔ Get AI explanations of the SQL query
✔ Create tables or insert data manually
✔ Download the entire conversation
✔ Work with multiple database types

🧩 Supported Data Sources
Type	Status
SQLite	✅
MySQL	✅
PostgreSQL	✅
CSV Files	✅
🏗️ System Architecture

User → Streamlit UI → LLM (Groq) → SQL Generator
→ Safety Check → Database Engine → Results
→ Auto Charts → SQL Explanation → Chat Memory

This makes the system behave like an AI Data Agent, not just a chatbot.

🧠 AI Capabilities

Natural Language → SQL conversion

Context-aware conversations (memory)

SQL safety filtering (prevents dangerous queries)

Query explanation in plain English

Automatic chart generation from results

📊 Auto Visualization

QueryMind automatically chooses the best chart:

Data Type	Chart
Category + Number	Bar Chart
Date + Number	Line Chart
2 Numbers	Scatter Plot
Single Number Column	Histogram
🛠 Tech Stack
Layer	Technology
UI	Streamlit
LLM	Groq (LLaMA 3.1 8B)
AI Framework	LangChain
Databases	SQLite, MySQL, PostgreSQL
Data Handling	Pandas
Charts	Matplotlib
Agent Logic	Custom modules
📁 Project Structure
project/
│
├── nl2sql.py              # Main Streamlit app
├── module/
│   ├── config.py          # API keys & settings
│   ├── query_engine.py    # LLM → SQL generation
│   ├── sql_utils.py       # Multi-DB execution
│   ├── safety.py          # SQL protection
│   ├── memory.py          # Conversation memory
│   ├── explain.py         # SQL explanation
│   ├── download_utils.py  # Chat export
│
└── requirements.txt

⚙️ Installation
git clone https://github.com/YOUR_USERNAME/querymind-ai.git
cd querymind-ai

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file:

GROQ_API_KEY=your_key_here

▶ Run the App
streamlit run nl2sql.py

💬 Example Questions You Can Ask

"Show total sales by product"

"Who are the top 5 students by score?"

"Average revenue per month"

"How many users signed up this year?"

🔒 Safety Features

The system blocks dangerous queries like:

DROP TABLE

DELETE without WHERE

System-level operations

🧠 Is This a RAG System?

No.
This is an AI Agent that works on structured databases, not document retrieval.

It uses:

Schema awareness

SQL reasoning

Memory

Tool usage

Which makes it closer to a Database AI Agent than RAG.

🌟 Future Improvements

Dashboard mode

Role-based access control

Query optimization hints

Voice-to-SQL

Cloud deployment

👩‍💻 Author

Nourhan Mahmoud
AI Engineer | LLMs | Computer Vision | ML Systems

🏁 Why This Project Matters

Most AI apps stop at chat.
QueryMind AI takes action, understands data, and becomes an intelligent database assistant.
