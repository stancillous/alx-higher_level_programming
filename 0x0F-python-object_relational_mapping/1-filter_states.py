#!/usr/bin/python3
import sys
import MySQLdb

def listFilteredStates(user, pswd, dbName):
    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = user,
        passwd = pswd,
        db = dbName
    )
    #cursor
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%'"
    #execute our query
    cur.execute(query)
    #get the result of the previous execution
    rows = cur.fetchall()

    for row in rows:
        print(row)

if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    listFilteredStates(user, pswd, dbName)    