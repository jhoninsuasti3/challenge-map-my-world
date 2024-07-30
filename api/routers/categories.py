# routers/category.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Any
from ..schemas.category import CategoryCreate, CategoryResponse, CategoriesBulkCreate
from api.database.repository.category_repo import (
    create_category,
    create_categories,
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

    Raises:
        HTTPException: If there is an error during the creation process.
    """
    try:
        db_category = create_category(db, category)
        return db_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating category: {str(e)}")

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
        HTTPException: If the category is not found or if there is an error during retrieval.
    """
    try:
        db_category = get_category(db, category_id)
        if db_category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        return db_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving category: {str(e)}")

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

    Raises:
        HTTPException: If there is an error during the retrieval process.
    """
    try:
        categories = get_categories(db)
        return categories
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving categories: {str(e)}")

@router.post("/categories/bulk", response_model=List[CategoryResponse])
def create_bulk_categories(
    categories_bulk: CategoriesBulkCreate,
    db: Session = Depends(get_db)
) -> List[CategoryResponse]:
    """
    Create multiple categories in bulk.

    Args:
        categories_bulk (CategoriesBulkCreate): A list of categories to create.
        db (Session): The database session.

    Returns:
        List[CategoryResponse]: A list of created category data.

    Raises:
        HTTPException: If there is an error during the creation process.
    """
    try:
        created_categories = create_categories(db, categories_bulk.categories)
        return created_categories
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating categories: {str(e)}")
