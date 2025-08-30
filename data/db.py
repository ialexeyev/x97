import sqlite3

#1. Load function (default)
def load(table, col):
    conn = sqlite3.connect('data/prismdb.db')
    prism_cursor = conn.cursor()
    request = "SELECT " + col + " FROM " + table
    prism_cursor.execute(request)
    data = prism_cursor.fetchall()
    conn.close()
    return data

#2. Load function (specific for few parameters)
def loadspec(*args):
    # Getting expression:
    preparation = ""
    for i in range(1, len(args)):
        preparation += args[i] + ", "
    expression = preparation[:-2]
    #connecting to database:
    conn = sqlite3.connect('data/prismdb.db')
    prism_cursor = conn.cursor()
    request = "SELECT " + expression + " FROM " + args[0]
    prism_cursor.execute(request)
    data = prism_cursor.fetchall()
    conn.close()
    return data

#3. Load function (without same values):
def loadunique(table, col):
    conn = sqlite3.connect('data/prismdb.db')
    prism_cursor = conn.cursor()
    request = "SELECT DISTINCT " + col + " FROM " + table
    prism_cursor.execute(request)
    data = prism_cursor.fetchall()
    conn.close()
    return data

#4. Insert function: insert new candidate to temporary users
def newuser(nufname, 
            nulname, 
            numail, 
            nudep, 
            nupos, 
            nusupervisor):
    conn = sqlite3.connect('data/prismdb.db')
    prism_cursor = conn.cursor()
    prism_cursor.execute("INSERT INTO tempusers (tufname, tulname, tumail, tudepartment, tusupervisor, tuposition, tustatus ) VALUES (?, ?, ?, ?, ?, ?, ?)", (nufname, nulname, numail, nudep, nusupervisor, nupos, 'new'))
    conn.commit()
    conn.close()
    return "OK"
