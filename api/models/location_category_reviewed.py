# api/models/location.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from api.database.database import Base
from sqlalchemy.orm import relationship
from api.models.category import Category
from api.models.location import Location

class LocationCategoryReviewed(Base):
    __tablename__ = 'location_category_reviewed'
    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    last_reviewed = Column(DateTime, nullable=False)
    location = relationship(Location)
    category = relationship(Category)