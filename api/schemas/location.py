# schemas/location.py
from pydantic import BaseModel, Field
from typing import Optional

class LocationBase(BaseModel):
    name: str = Field(..., description="Name of the location")
    latitude: float = Field(..., description="Latitude of the location")
    longitude: float = Field(..., description="Longitude of the location")

class LocationCreate(LocationBase):
    pass

class LocationResponse(LocationBase):
    id: int = Field(..., description="ID of the location")

    class Config:
        orm_mode = True
