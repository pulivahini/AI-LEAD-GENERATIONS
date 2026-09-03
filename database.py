import sqlite3
from pathlib import Path
DB=Path(__file__).resolve().parent/"leads.db"
def init_db():
    c=sqlite3.connect(DB)
    c.execute('''CREATE TABLE IF NOT EXISTS leads(
    id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,company TEXT,
    industry TEXT,budget REAL,requirement TEXT,engagement INTEGER,
    score INTEGER,category TEXT,ai_message TEXT)''')
    c.commit(); c.close()
def insert_lead(d):
    c=sqlite3.connect(DB)
    cur=c.execute('''INSERT INTO leads
    (name,email,company,industry,budget,requirement,engagement,score,category,ai_message)
    VALUES (?,?,?,?,?,?,?,?,?,?)''',
    (d["name"],d["email"],d["company"],d["industry"],d["budget"],d["requirement"],
     d["engagement"],d["score"],d["category"],d["ai_message"]))
    c.commit(); i=cur.lastrowid; c.close(); return i
def all_leads():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    rows=[dict(x) for x in c.execute("SELECT * FROM leads ORDER BY id DESC")]
    c.close(); return rows
