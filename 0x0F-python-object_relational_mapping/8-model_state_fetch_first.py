#!/usr/bin/python3
"""List the first state object"""

if __name__ == '__main__':

    import sqlalchemy
    from sqlalchemy import create_engine,\
        Column, Integer, UniqueConstraint, String
    from sqlalchemy.ext.declarative import declarative_base
    from model_city import City, Base
    import sys
    from sqlalchemy.orm import sessionmaker


    engine = create_engine("mysql://ray:raypassword@localhost/world")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_city = City(Name="Nairobi", CountryCode="254", District="Idek", Population=323390)
    session.add(new_city)
    session.commit()
    print(new_city.id)
    session.close()