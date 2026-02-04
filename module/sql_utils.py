# module/sql_utils.py
import sqlite3
import mysql.connector
import psycopg2

def execute_query(db_type, query, **kwargs):
    """
    Execute a SQL query on different database types.
    db_type: "SQLite", "MySQL", "PostgreSQL"
    kwargs: connection parameters (db_path for SQLite, host/user/password/db_name for others)
    """
    try:
        if db_type == "SQLite":
            with sqlite3.connect(kwargs["db_path"]) as conn:
                cursor = conn.cursor()
        # Split multiple statements by ';'
                statements = [s.strip() for s in query.split(";") if s.strip()]
                for stmt in statements:
                  cursor.execute(stmt)
                if query.strip().lower().startswith("select"):
                    rows = cursor.fetchall()
                    cols = [desc[0] for desc in cursor.description]
                    return rows, cols
                else:
                    conn.commit()
                    return [], []

        elif db_type == "MySQL":
            conn = mysql.connector.connect(
                host=kwargs["host"],
                user=kwargs["user"],
                password=kwargs["password"],
                database=kwargs["db_name"]
            )
            cursor = conn.cursor()
            cursor.execute(query)
            if query.strip().lower().startswith("select"):
                rows = cursor.fetchall()
                cols = [desc[0] for desc in cursor.description]
                conn.close()
                return rows, cols
            else:
                conn.commit()
                conn.close()
                return [], []

        elif db_type == "PostgreSQL":
            conn = psycopg2.connect(
                host=kwargs["host"],
                user=kwargs["user"],
                password=kwargs["password"],
                dbname=kwargs["db_name"]
            )
            cursor = conn.cursor()
            cursor.execute(query)
            if query.strip().lower().startswith("select"):
                rows = cursor.fetchall()
                cols = [desc[0] for desc in cursor.description]
                conn.close()
                return rows, cols
            else:
                conn.commit()
                conn.close()
                return [], []

    except Exception as e:
        return f"SQL Error: {str(e)}", []


def get_current_schema(db_type, **kwargs):
    """
    Fetch current database schema dynamically.
    """
    schema = ""
    try:
        if db_type == "SQLite":
            with sqlite3.connect(kwargs["db_path"]) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = cursor.fetchall()
                for table in tables:
                    table_name = table[0]
                    cursor.execute(f"PRAGMA table_info({table_name})")
                    cols = cursor.fetchall()
                    schema += f"- {table_name}({', '.join([col[1] for col in cols])})\n"

        elif db_type == "MySQL":
            conn = mysql.connector.connect(
                host=kwargs["host"],
                user=kwargs["user"],
                password=kwargs["password"],
                database=kwargs["db_name"]
            )
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = [t[0] for t in cursor.fetchall()]
            for table_name in tables:
                cursor.execute(f"DESCRIBE {table_name}")
                cols = cursor.fetchall()
                schema += f"- {table_name}({', '.join([col[0] for col in cols])})\n"
            conn.close()

        elif db_type == "PostgreSQL":
            conn = psycopg2.connect(
                host=kwargs["host"],
                user=kwargs["user"],
                password=kwargs["password"],
                dbname=kwargs["db_name"]
            )
            cursor = conn.cursor()
            cursor.execute("""
                SELECT table_name FROM information_schema.tables
                WHERE table_schema='public'
            """)
            tables = [t[0] for t in cursor.fetchall()]
            for table_name in tables:
                cursor.execute(f"""
                    SELECT column_name FROM information_schema.columns
                    WHERE table_name='{table_name}'
                """)
                cols = [c[0] for c in cursor.fetchall()]
                schema += f"- {table_name}({', '.join(cols)})\n"
            conn.close()

    except Exception as e:
        schema = f"Error fetching schema: {str(e)}"

    return schema.strip()

