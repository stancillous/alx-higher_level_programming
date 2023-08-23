#!/usr/bin/python3
"""List all State objects with letter a"""

if __name__ == '__main__':

    import sqlalchemy
    from sqlalchemy import create_engine, \
        Column, Integer, UniqueConstraint, String
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    import sys
    from sqlalchemy.orm import sessionmaker

    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    """Engine to connect to DB"""
    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}")

    """Session class for session objects"""
    Session = sessionmaker(bind=engine)

    """Session with database started"""
    session = Session()

    """Sample query"""
    results = session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id.asc())

    """Iterateing through results of query"""
    for state in results:
        print(f"{state.id}: {state.name}")
