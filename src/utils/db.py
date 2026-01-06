import sqlite3

def get_connection(db_path="output/asana_simulation.sqlite"):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
