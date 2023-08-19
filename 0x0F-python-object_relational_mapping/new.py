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
"""Class State"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, UniqueConstraint, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# MY_USER = 'bot'
# MY_PASSWD = 'TwoGreen1.'
# MY_DB = 'hbtn_0e_4_usa'
# MY_HOST = 'localhost'
# MY_PORT = '3306'

# connection_url = f"mysql://{MY_USER}:{MY_PASSWD}@{MY_HOST}:{MY_PORT}/{MY_DB}"

# print()
# print(connection_url)
# print()

# """Engine to connect to DB"""
# engine = create_engine(connection_url)

# """Actual connection to DB"""
# connection = engine.connect()

# result = connection.execute("SHOW DATABASES;")

# for row in result:
#     print(row)

# connection.close()


class State(Base):
    """Class State"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(length=128), nullable=False)
