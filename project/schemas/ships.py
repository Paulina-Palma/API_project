from pydantic import BaseModel, PositiveFloat, Field


class ShipSchema(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=255)
    max_speed: PositiveFloat
    distance: PositiveFloat
    cost_per_day: PositiveFloat

