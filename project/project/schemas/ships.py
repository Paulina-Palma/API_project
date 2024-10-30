from pydantic import BaseModel, PositiveFloat, Field, PositiveInt
from typing import Optional


class ShipCreateSchema(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    max_speed: float
    distance: float
    cost_per_day: float

    class Config:
        from_attributes = True


class ShipResponseSchema(BaseModel):
    id: PositiveInt
    name: str = Field(min_length=3, max_length=255)
    max_speed: PositiveFloat
    distance: PositiveFloat
    cost_per_day: PositiveFloat

    class Config:
        # orm_mode = True -> renamed to from_attributes
        from_attributes = True
