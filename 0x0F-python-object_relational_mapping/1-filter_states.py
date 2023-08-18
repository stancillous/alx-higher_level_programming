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






#!/usr/bin/python3
def listStates(user, pswd, dbName):
    db = MySQLdb.connect(
        host = "localhost",
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
    import sys
    import MySQLdb
    user = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    listStates(user, pswd, dbName)






    
#!/usr/bin/python3
"""List all states in database"""

if __name__ == "__main__":
    
    import MySQLdb
    import sys

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    """Establish connection to DB"""
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    """Create cursor object"""
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    """Capture all rows returned by query"""
    rows = cur.fetchall()

    for state in rows:
        print(state)