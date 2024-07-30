# routers/location.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, List
from api.database.db import get_db
from api.schemas.location import LocationCreate, LocationResponse, LocationsBulkCreate
from api.database.repository.location_repo import (
    create_location,
    get_location,
    get_all_locations,
    bulk_create_locations,
    update_location,
    delete_location
)

router = APIRouter()

@router.post("/locations/", response_model=LocationResponse)
def create_new_location(
    location: LocationCreate,
    db: Session = Depends(get_db)
) -> LocationResponse:
    """
    Create a new location.

    Args:
        location (LocationCreate): The location data to be created.
        db (Session): The database session.

    Returns:
        LocationResponse: The created location data.

    Raises:
        HTTPException: If there is an error during the creation process.
    """
    try:
        db_location = create_location(db, location)
        return db_location
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating location: {str(e)}")

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
    try:
        db_location = get_location(db, location_id)
        if db_location is None:
            raise HTTPException(status_code=404, detail="Location not found")
        return db_location
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving location: {str(e)}")

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

    Raises:
        HTTPException: If there is an error during the retrieval process.
    """
    try:
        locations = get_all_locations(db)
        return locations
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving locations: {str(e)}")

@router.post("/locations/bulk", response_model=List[LocationResponse])
def create_bulk_locations(
    locations_bulk: LocationsBulkCreate,
    db: Session = Depends(get_db)
) -> List[LocationResponse]:
    """
    Create multiple locations in bulk.

    Args:
        locations_bulk (LocationsBulkCreate): A list of locations to be created.
        db (Session): The database session.

    Returns:
        List[LocationResponse]: A list of created location data.

    Raises:
        HTTPException: If there is an error during the creation process.
    """
    try:
        created_locations = bulk_create_locations(db, locations_bulk.locations)
        return created_locations
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating bulk locations: {str(e)}")

@router.put("/locations/{location_id}", response_model=LocationResponse)
def update_existing_location(
    location_id: int,
    location: LocationCreate,
    db: Session = Depends(get_db)
) -> LocationResponse:
    """
    Update an existing location by its ID.

    Args:
        location_id (int): The ID of the location to update.
        location (LocationCreate): The updated location data.
        db (Session): The database session.

    Returns:
        LocationResponse: The updated location data.

    Raises:
        HTTPException: If the location is not found or if there is an error during the update process.
    """
    try:
        db_location = update_location(db, location_id, location)
        if db_location is None:
            raise HTTPException(status_code=404, detail="Location not found")
        return db_location
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating location: {str(e)}")

@router.delete("/locations/{location_id}", response_model=LocationResponse)
def delete_existing_location(
    location_id: int,
    db: Session = Depends(get_db)
) -> LocationResponse:
    """
    Delete a location by its ID.

    Args:
        location_id (int): The ID of the location to delete.
        db (Session): The database session.

    Returns:
        LocationResponse: The deleted location data.

    Raises:
        HTTPException: If the location is not found or if there is an error during the deletion process.
    """
    try:
        db_location = delete_location(db, location_id)
        if db_location is None:
            raise HTTPException(status_code=404, detail="Location not found")
        return db_location
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting location: {str(e)}")
