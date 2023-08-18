#!/usr/bin/python3
import sys
import MySQLdb


def listStates(user, pswd, dbName):
    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = user,
        passwd = pswd,
        db = dbName
    )
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    print(user, pswd, dbName)
    listStates(user, pswd, dbName)