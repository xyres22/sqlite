import sqlite3

conn = sqlite3.connect("todos.db")

cursor = conn.cursor()
sql_query = """CREATE TABLE todos (
        id integer PRIMARY KEY,
        title text NOT NULL,
        description text NOT NULL,
        done text NOT NULL
        )"""
cursor.execute(sql_query)