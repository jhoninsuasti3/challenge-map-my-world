from sqlalchemy.orm import Session
from ..models.location_category_reviewed import LocationCategoryReviewed
from ..schemas.location_category_reviewed import LocationCategoryReviewedCreate

def create_location_category_reviewed(db: Session, lc_reviewed: LocationCategoryReviewedCreate):
    db_lc_reviewed = LocationCategoryReviewed(**lc_reviewed.dict())
    db.add(db_lc_reviewed)
    db.commit()
    db.refresh(db_lc_reviewed)
    return db_lc_reviewed

def get_location_category_reviewed(db: Session, location_id: int, category_id: int):
    return db.query(LocationCategoryReviewed).filter(
        LocationCategoryReviewed.location_id == location_id,
        LocationCategoryReviewed.category_id == category_id
    ).first()

# Otros métodos para actualizar, eliminar, listar revisiones de ubicación-categoría, etc.
