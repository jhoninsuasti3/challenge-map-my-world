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

def bulk_create_locations(db: Session, locations_data):
    locations = [
        Location(
            name=loc.name,
            latitude=loc.latitude,
            longitude=loc.longitude
        )
        for loc in locations_data
    ]
    db.add_all(locations)
    db.commit()
    return locations

def get_location(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()

def get_all_locations(db: Session) -> List[Location]:
    return db.query(Location).all()


def update_location(db: Session, location_id: int, location_data: LocationCreate):
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location:
        db_location.name = location_data.name
        db_location.latitude = location_data.latitude
        db_location.longitude = location_data.longitude
        db.commit()
        db.refresh(db_location)
    return db_location

def delete_location(db: Session, location_id: int):
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location:
        db.delete(db_location)
        db.commit()
    return db_location