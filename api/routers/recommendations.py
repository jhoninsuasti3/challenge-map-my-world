from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta
from ..schemas.location_category_reviewed import LocationCategoryReviewedResponse
from ..repository.location_category_reviewed_repo import get_location_category_reviewed
from ..database.db import get_db

router = APIRouter()

@router.get("/recommendations/", response_model=List[LocationCategoryReviewedResponse])
def get_recommendations(db: Session = Depends(get_db)):
    thirty_days_ago = datetime.now() - timedelta(days=30)
    # Obtener las 10 combinaciones de ubicación-categoría que no han sido revisadas en los últimos 30 días
    unrevised_combinations = db.query(LocationCategoryReviewed).filter(
        LocationCategoryReviewed.last_reviewed <= thirty_days_ago
    ).limit(10).all()
    return unrevised_combinations
