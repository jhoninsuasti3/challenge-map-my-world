# routers/location.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, List
from api.schemas.location import LocationCreate, LocationResponse
from api.database.repository.location_repo import(
    create_location,
    get_location,
    get_all_locations
)
from api.database.db import get_db

router = APIRouter()

@router.post("/locations/", response_model=LocationResponse)
def create_new_location(
    location: LocationCreate,
    db: Session = Depends(get_db)
):
    db_location = create_location(db, location)
    return db_location

@router.get("/locations/{location_id}", response_model=LocationResponse, response_model_exclude_none=True)
def get_single_location(
    location_id: int,
    db: Session = Depends(get_db)
) -> Any:
    """
    Retrieve a single location by its ID.

    Args:
        location_id (int): The ID of the location to retrieve.
        db (Session): The database session.

    Returns:
        LocationResponse: The location data if found.

    Raises:
        HTTPException: If the location is not found.
    """
    db_location = get_location(db, location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.get("/locations/", response_model=List[LocationResponse])
def list_all_locations(
    db: Session = Depends(get_db)
) -> List[LocationResponse]:
    """
    List all locations.

    Args:
        db (Session): The database session.

    Returns:
        List[LocationResponse]: A list of all locations.
    """
    locations = get_all_locations(db)
    return locations