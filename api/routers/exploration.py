# api/routers/exploration.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.utils.database import get_db
from api.utils.utils import recommend_locations_categories
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/recommendations/")
async def get_recommendations(db: Session = Depends(get_db)):
    thirty_days_ago = datetime.now() - timedelta(days=30)
    recommended_combinations = recommend_locations_categories(db, thirty_days_ago)
    return {"recommendations": recommended_combinations}
