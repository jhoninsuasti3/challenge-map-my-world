from sqlalchemy.orm import Session
from api.database.models.category import Category
from api.schemas.category import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name, location_id=category.location_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_categories(db: Session) -> list[Category]:
    return db.query(Category).all()