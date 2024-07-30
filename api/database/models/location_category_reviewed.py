# api/database/models/location_category_reviewed.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from api.database import Base

class LocationCategoryReviewed(Base):
    __tablename__ = 'location_category_reviewed'

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    reviewed_at = Column(DateTime, default=func.now(), nullable=False)

    # Relationships
    location = relationship("Location", back_populates="location_category_reviews")
    category = relationship("Category", back_populates="location_category_reviews")
