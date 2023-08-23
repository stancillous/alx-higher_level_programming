from sqlalchemy import Column, String, Integer
from model_state import Base

class City(Base):
    __tablename__ = "city"
    id = Column(Integer, unique=True, primary_key=True)
    Name = Column(String)
    CountryCode = Column(String)
    District = Column(String)
    Population = Column(Integer)
   
