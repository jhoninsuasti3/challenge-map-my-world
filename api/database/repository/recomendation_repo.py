from sqlalchemy.orm import Session
from sqlalchemy import func
from api.database.models import Location, Category, LocationCategoryReviewed
from typing import List, Dict

def get_unreviewed_combinations(db: Session) -> List[Dict[str, int]]:
    thirty_days_ago = func.now() - func.interval('30 day')

    # Subquery to get recent reviews
    recent_reviews_subquery = (
        db.query(LocationCategoryReviewed.location_id, LocationCategoryReviewed.category_id)
        .filter(LocationCategoryReviewed.reviewed_at > thirty_days_ago)
        .subquery()
    )

    # Query to get unreviewed combinations
    unreviewed_combinations = (
        db.query(Location.id, Category.id)
        .select_from(Location)
        .outerjoin(Category, Category.location_id == Location.id)
        .outerjoin(recent_reviews_subquery,
                   (Location.id == recent_reviews_subquery.c.location_id) &
                   (Category.id == recent_reviews_subquery.c.category_id))
        .filter(recent_reviews_subquery.c.location_id.is_(None))
        .filter(recent_reviews_subquery.c.category_id.is_(None))
        .limit(10)  # Limitar a 10 combinaciones
        .all()
    )

    # Convert result to list of dictionaries
    recommendations = [{"location_id": loc_id, "category_id": cat_id} for loc_id, cat_id in unreviewed_combinations]

    return recommendations
