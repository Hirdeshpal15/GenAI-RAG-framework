import sqlite3
from datetime import datetime


def log_interaction(query,answer,evidence):

    conn = sqlite3.connect("database/logs.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            answer TEXT,
            evidence TEXT,
            timestamp TEXT
        )
    """)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    evidence_text = "\n\n".join(evidence)

    cursor.execute(
        "INSERT INTO interactions (query, answer, evidence, timestamp) VALUES (?, ?, ?, ?)",
        (query, answer, evidence_text, timestamp)
    )

    conn.commit()

    conn.close()
