# api/models/location.py
from sqlalchemy import Column, Integer, Float
from api.database.database import Base

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
