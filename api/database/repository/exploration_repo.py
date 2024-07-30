# api/database/repository/exploration_repo.py

from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from api.database.models.location_category_reviewed import LocationCategoryReviewed

def get_exploration_recommendations(db: Session, limit: int = 10):
    # Fecha actual y fecha de corte (30 días atrás)
    now = datetime.utcnow()
    thirty_days_ago = now - timedelta(days=30)

    # Consulta para obtener combinaciones de ubicación-categoría no revisadas en los últimos 30 días
    # Prioriza combinaciones que nunca se han revisado
    subquery = (
        db.query(LocationCategoryReviewed.location_id, LocationCategoryReviewed.category_id)
        .filter(LocationCategoryReviewed.reviewed_at >= thirty_days_ago)
        .subquery()
    )

    recommendations = (
        db.query(LocationCategoryReviewed.location_id, LocationCategoryReviewed.category_id)
        .outerjoin(subquery,
                   (LocationCategoryReviewed.location_id == subquery.c.location_id) &
                   (LocationCategoryReviewed.category_id == subquery.c.category_id))
        .filter(subquery.c.location_id == None, subquery.c.category_id == None)
        .limit(limit)
        .all()
    )

    return recommendations
