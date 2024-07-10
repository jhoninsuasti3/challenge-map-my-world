# api/models/location.py
from sqlalchemy import Column, Integer, String
from api.database.database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
