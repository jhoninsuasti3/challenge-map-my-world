from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas.category import CategoryCreate, CategoryResponse
from ..repository.category_repo import create_category, get_category
from ..database.db import get_db

router = APIRouter()

@router.post("/categories/", response_model=CategoryResponse)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = create_category(db, category)
    return db_category

@router.get("/categories/{category_id}", response_model=CategoryResponse)
def get_single_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

