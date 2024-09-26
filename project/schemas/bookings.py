from pydantic import BaseModel


class BookingSchema(BaseModel):
    name: str