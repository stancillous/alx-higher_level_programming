#!/usr/bin/python3
"""script that lists all State objects
from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker


    engine = create_engine("mysql://ray:raypassword@localhost/hbtn_0e_0_usa",pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects from the database and sort by states.id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for item in states:
        print(f"{item.id}: {item.name}")

    # Close the session
    session.close()


