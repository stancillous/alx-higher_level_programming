#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker


    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{dbUser}:{pswd}@localhost:3306/{dbName}")
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


