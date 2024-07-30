# api/database/repository/location_repo.py
from sqlalchemy.orm import Session
from api.database.models.location import Location
from api.schemas.location import LocationCreate
from typing import List

def create_location(db: Session, location: LocationCreate):
    db_location = Location(
        name=location.name,
        latitude=location.latitude,
        longitude=location.longitude
    )
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def get_location(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()

def get_all_locations(db: Session) -> List[Location]:
    return db.query(Location).all()
