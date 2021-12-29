from flask import Flask
import sqlite3
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("todos.db")
    except sqlite3.error:
        logging.warning("Database connection error.")
    return conn