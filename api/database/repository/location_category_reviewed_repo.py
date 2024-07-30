from sqlalchemy.orm import Session
from api.database.models.location_category_reviewed import LocationCategoryReviewed
from datetime import datetime


def create_review(db: Session, location_id: int, category_id: int, reviewed_at: datetime) -> LocationCategoryReviewed:
    db_review = LocationCategoryReviewed(
        location_id=location_id,
        category_id=category_id,
        reviewed_at=reviewed_at
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_review(db: Session, review_id: int) -> LocationCategoryReviewed:
    return db.query(LocationCategoryReviewed).filter(LocationCategoryReviewed.id == review_id).first()

# Otros métodos para actualizar, eliminar, listar revisiones de ubicación-categoría, etc.
