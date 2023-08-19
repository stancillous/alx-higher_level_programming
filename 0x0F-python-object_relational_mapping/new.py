# """script that lists all cities from a database"""

# if __name__ == "__main__":
#     import MySQLdb

#     dbUser = 'root'
#     pswd = 'kavulani@88'
#     dbName = 'mydb'

#     """make a connection w our db"""
#     db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

#     """cursor object"""
#     cur = db.cursor()
#     query = "SELECT * FROM orders ORDER BY orders.id ASC"
#     cur.execute(query)
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     cur.close()
#     db.close()



#!/usr/bin/python3
"""file that contains the class definition of a
State and an instance Base = declarative_base()"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
dbUser = sys.argv[1]
pswd = sys.argv[2]
dbName = sys.argv[3]

"""class State that inherits from Base"""


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ :name of the MySQL table to store States.
    id: state's id.
    name: state's name.
    """
    __tablename__ = "states"
    id = Column("id", Integer, autoincrement=True,
                primary_key=True, unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)
