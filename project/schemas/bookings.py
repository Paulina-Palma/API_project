from pydantic import BaseModel, PositiveFloat, PositiveInt, Field
from typing import Optional


class BookingSchema(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=20)
    spaceship_id: int
    customer_id: int
    date_start: str = Field
    date_end: str = Field
