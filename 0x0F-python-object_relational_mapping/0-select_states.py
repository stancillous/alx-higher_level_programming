#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb

    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=dbUser, passwd=pswd, db=dbName)
    query = "SELECT * FROM states ORDER BY states.id ASC"

    cur = db.cursor()
    #execute our query
    cur.execute(query)
    #get result of previous execution
    rows = cur.fetchall()
    #rows will be a list of tuples
    for row in rows:
        print(row)