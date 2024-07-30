# api/routers/exploration.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.schemas.location_category_reviewed import LocationCategoryReviewedResponse
from api.database.repository.exploration_repo import get_exploration_recommendations
from ..database.db import get_db

router = APIRouter()

@router.get("/exploration/recommendations/", response_model=List[LocationCategoryReviewedResponse])
def get_recommendations(
    db: Session = Depends(get_db),
    limit: int = 10
) -> List[LocationCategoryReviewedResponse]:
    """
    Retrieve exploration recommendations.

    Args:
        db (Session): The database session.
        limit (int): The maximum number of recommendations to return.

    Returns:
        List[LocationCategoryReviewedResponse]: The list of recommended location-category combinations.
    """
    recommendations = get_exploration_recommendations(db, limit)
    return recommendations
