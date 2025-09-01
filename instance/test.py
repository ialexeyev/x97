import sqlite3

conn = sqlite3.connect('instance/prismdb.db')
prism_cursor = conn.cursor()

prism_cursor.execute('SELECT * FROM tempusers')
#prism_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#prism_cursor.execute("""CREATE TABLE tempusers (
#   id INTEGER PRIMARY KEY,
#   tuid TEXT,
#   tufname TEXT,
#   tulname TEXT,
#   tumail TEXT,
#   tudepartment TEXT,
#   tusupervisor TEXT,
#   tuposition TEXT,
#   tupassword TEXT,
#   tuphoto TEXT,
#   tustatus TEXT
#)""")
#prism_cursor.execute("INSERT INTO services (spagename, sname, sdata) VALUES (?, ?, ?)", ('home', 'positionFieldPlaceholder', 'Position'))
#prism_cursor.execute("INSERT INTO tempusers (uid, ufname, ulname, umail, udepartment, usupervisor,  uposition, uaccess, upassword) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", ('i.alexeyev', 'Igor', 'Alexeyev', 'i.alexeyev@hyundai.kz', 'Manufacturing development department', 'Yerbol Kassymkanov', 'Head of department', 'PRIVAC', 'alexgt40'))

data = prism_cursor.fetchall()
#conn.commit()
conn.close()

print(data)
