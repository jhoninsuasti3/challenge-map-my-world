from sqlalchemy.orm import Session
from ..models.location import Location
from ..schemas.location import LocationCreate

def create_location(db: Session, location: LocationCreate):
    db_location = Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def get_location(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()

# Otros métodos para actualizar, eliminar, listar ubicaciones, etc.
