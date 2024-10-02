from pydantic import BaseModel, PositiveFloat, Field, PositiveInt
from typing import Optional


class ShipSchema(BaseModel):
    id: Optional[PositiveInt]
    name: str = Field(min_length=3, max_length=255)
    max_speed: PositiveFloat
    distance: PositiveFloat
    cost_per_day: PositiveFloat

    class Config:
        # orm_mode = True
        from_attributes = True
