#!/usr/bin/python3

""""""
if __name__ == "__main__":
    import sys
    import MySQLdb

    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]

    """make the connection"""
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)
    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"

    cur = db.cursor()
    """execute query"""
    cur.execute(query, (stateName,))
    """get results"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()