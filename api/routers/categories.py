from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from ..schemas.category import CategoryCreate, CategoryResponse
from api.database.repository.category_repo import(
    create_category,
    get_category,
    get_categories
)
from ..database.db import get_db

router = APIRouter()

@router.post("/categories/", response_model=CategoryResponse)
def create_new_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
) -> CategoryResponse:
    """
    Create a new category.

    Args:
        category (CategoryCreate): The category data to create.
        db (Session): The database session.

    Returns:
        CategoryResponse: The created category data.
    """
    db_category = create_category(db, category)
    return db_category

@router.get("/categories/{category_id}", response_model=CategoryResponse)
def get_single_category(
    category_id: int,
    db: Session = Depends(get_db)
) -> Any:
    """
    Retrieve a single category by its ID.

    Args:
        category_id (int): The ID of the category to retrieve.
        db (Session): The database session.

    Returns:
        CategoryResponse: The category data if found.

    Raises:
        HTTPException: If the category is not found.
    """
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.get("/categories/", response_model=List[CategoryResponse])
def list_categories(
    db: Session = Depends(get_db)
) -> List[CategoryResponse]:
    """
    Retrieve a list of all categories.

    Args:
        db (Session): The database session.

    Returns:
        List[CategoryResponse]: The list of all categories.
    """
    categories = get_categories(db)
    return categories