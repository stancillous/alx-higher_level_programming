#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sql://username:password@host:port/database')
# engine.connect()

Base = declarative_base()
dbUser = sys.argv[1]
pswd = sys.argv[2]
dbName = sys.argv[3]


class State(Base):
    __tablename__ = "states"
    id = Column("id", Integer, autoincrement=True,
                primary_key=True, unique=True, nullable=False)
    name = Column("name", String, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


engine = create_engine(f"mysql+mysqldb://{dbUser}:{pswd}@localhost/{dbName}")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
