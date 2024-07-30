# api/schemas/category.py
from pydantic import BaseModel
from typing import List
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    location_id: int

class CategoriesBulkCreate(BaseModel):
    categories: List[CategoryCreate]

class CategoryResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    location_id: int

    class Config:
        orm_mode = True
