from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Cities

if __name__ == "__main__":
    import sys
    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost/{dbName}", pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    #instance of the Session
    session = Session()

    #our query
    citiesQuery = session.query(Cities).order_by(Cities.id).all()