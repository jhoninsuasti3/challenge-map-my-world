# api/utils/recommendation_system.py

from datetime import datetime, timedelta
from typing import List
from sqlalchemy.orm import Session
from api.models import Location, Category, ExplorationRecord
from sqlalchemy import func


def recommend_locations_categories(session: Session, threshold_date: datetime) -> List[str]:
    # Consulta para obtener las combinaciones no revisadas en los últimos 30 días
    unrevised_combinations = session.query(Location.name, Category.name) \
        .outerjoin(ExplorationRecord, (Location.id == ExplorationRecord.location_id) &
                   (Category.id == ExplorationRecord.category_id) &
                   (ExplorationRecord.last_reviewed < threshold_date)) \
        .filter(ExplorationRecord.id == None) \
        .group_by(Location.name, Category.name) \
        .order_by(func.random()) \
        .limit(10) \
        .all()

    recommended_combinations = [f"{location}-{category}" for location, category in unrevised_combinations]

    return recommended_combinations
