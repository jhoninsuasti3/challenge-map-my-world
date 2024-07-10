from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas.location import LocationCreate, LocationResponse
from ..repository.location_repo import create_location, get_location
from ..database.db import get_db

router = APIRouter()

@router.post("/locations/", response_model=LocationResponse)
def create_new_location(location: LocationCreate, db: Session = Depends(get_db)):
    db_location = create_location(db, location)
    return db_location

@router.get("/locations/{location_id}", response_model=LocationResponse)
def get_single_location(location_id: int, db: Session = Depends(get_db)):
    db_location = get_location(db, location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location
