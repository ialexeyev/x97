import sqlite3
import socket


#1. Load function (default)
def load(table, col):
    conn = sqlite3.connect('instance/prismdb.db')
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
    conn = sqlite3.connect('instance/prismdb.db')
    prism_cursor = conn.cursor()
    request = "SELECT " + expression + " FROM " + args[0]
    prism_cursor.execute(request)
    data = prism_cursor.fetchall()
    conn.close()
    return data


#3. Load function (without same values):
def loadunique(table, col):
    conn = sqlite3.connect('instance/prismdb.db')
    prism_cursor = conn.cursor()
    request = "SELECT DISTINCT " + col + " FROM " + table
    prism_cursor.execute(request)
    data = prism_cursor.fetchall()
    conn.close()
    return data


#4. Insert function: insert new candidate to temporary users
def newuser(nufname, nulname, numail, nudep, nupos, nusupervisor):
    conn = sqlite3.connect('instance/prismdb.db')
    prism_cursor = conn.cursor()
    prism_cursor.execute(
        "INSERT INTO tempusers (tufname, tulname, tumail, tudepartment, tusupervisor, tuposition, tustatus ) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (nufname, nulname, numail, nudep, nusupervisor, nupos, 'new'))
    conn.commit()
    conn.close()
    return "OK"

#5. Add user to attendance (PRIVAC);
def attendanceadd(aid):
    conn = sqlite3.connect('instance/prismdb.db')
    prism_cursor = conn.cursor()
    # 1. Select first name and last name from users according to id
    prism_cursor.execute("SELECT ufname, ulname FROM users WHERE uid = ?", (aid,))
    dataName = prism_cursor.fetchall()
    afname = dataName[0][0];
    alname = dataName[0][1];
    conn.close()
    #print(aid)
    #print(afname)
    #print(alname)
    # 2. Define user ip adress
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    output = 'HOST: ' + hostname + ';  IP: ' + ip_address;
    return output;
    #prism_cursor.execute(
   #     "INSERT INTO attendance (aid) VALUES (?)",
   #     (aid))
   # conn.commit()
   # conn.close()
    return "OK"