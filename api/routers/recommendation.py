from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from api.database.db import get_db
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from api.database.querys.query_recommendations import query as QY

router = APIRouter()

@router.get("/recommendations/", response_model=List[Dict[str, int]])
def get_recommendations(db: Session = Depends(get_db)) -> List[Dict[str, int]]:
    """
    Retrieve recommendations for location-category combinations that haven't been reviewed in the last 30 days.

    Returns:
        List[Dict[str, int]]: A list of recommended location-category combinations.

    Raises:
        HTTPException: If there is an error during the retrieval process.
    """
    query = QY

    try:
        result = db.execute(query).fetchall()
        recommendations = [{"location_id": row[0], "category_id": row[1]} for row in result]
        return recommendations
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving recommendations: {str(e)}")
