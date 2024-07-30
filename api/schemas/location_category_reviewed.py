from pydantic import BaseModel
from datetime import datetime

class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: int
    reviewed_at: datetime

class LocationCategoryReviewedCreate(LocationCategoryReviewedBase):
    pass


class LocationCategoryReviewedResponse(LocationCategoryReviewedBase):
    id: int

    class Config:
        orm_mode = True
