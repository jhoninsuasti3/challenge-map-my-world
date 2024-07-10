from sqlalchemy.orm import Session
from ..models.category import Category
from ..schemas.category import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

