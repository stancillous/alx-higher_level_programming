"""script that lists all cities from a database"""

if __name__ == "__main__":
    import MySQLdb

    dbUser = 'root'
    pswd = 'kavulani@88'
    dbName = 'mydb'

    """make a connection w our db"""
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    """cursor object"""
    cur = db.cursor()
    query = "SELECT * FROM orders ORDER BY orders.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
