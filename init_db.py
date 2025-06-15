import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    is_done INTEGER DEFAULT 0
)
''')

conn.commit()
conn.close()