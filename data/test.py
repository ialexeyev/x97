import sqlite3

conn = sqlite3.connect('prismdb.db')
prism_cursor = conn.cursor()

prism_cursor.execute('SELECT * FROM base')
#prism_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#prism_cursor.execute("""CREATE TABLE base (
#  id INTEGER PRIMARY KEY,
#  bname TEXT,
#  bdata TEXT
# )""")


data = prism_cursor.fetchall()
#conn.commit()
conn.close()

print(data)
