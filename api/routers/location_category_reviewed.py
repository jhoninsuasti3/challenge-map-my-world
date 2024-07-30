from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any
from ..schemas.location_category_reviewed import LocationCategoryReviewedCreate, LocationCategoryReviewedResponse
from api.database.repository.location_category_reviewed_repo import create_review, get_review
from ..database.db import get_db
from datetime import datetime

router = APIRouter()

@router.post("/reviews/", response_model=LocationCategoryReviewedResponse)
def create_new_review(
    review: LocationCategoryReviewedCreate,
    db: Session = Depends(get_db)
) -> LocationCategoryReviewedResponse:
    """
    Create a new review for a location-category combination.

    Args:
        review (LocationCategoryReviewedCreate): The review data to create.
        db (Session): The database session.

    Returns:
        LocationCategoryReviewedResponse: The created review data.
    """
    created_review = create_review(
        db,
        review.location_id,
        review.category_id,
        review.reviewed_at
    )
    return created_review

@router.get("/reviews/{review_id}", response_model=LocationCategoryReviewedResponse)
def get_single_review(
    review_id: int,
    db: Session = Depends(get_db)
) -> Any:
    """
    Retrieve a single review by its ID.

    Args:
        review_id (int): The ID of the review to retrieve.
        db (Session): The database session.

    Returns:
        LocationCategoryReviewedResponse: The review data if found.

    Raises:
        HTTPException: If the review is not found.
    """
    db_review = get_review(db, review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review