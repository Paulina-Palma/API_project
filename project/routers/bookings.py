from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/booking",
    tags=["booking"],
    )

class BookingSchema(BaseModel):
    booking_id = int
    date_start = int
    date_end = int
    customer_id = int
    ship_id = int


bookings = []

def get_booking(booking_id: int):
    try: 
        return bookings[booking_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Booking not found")


@router.post("/", status_code=201)
async def add(booking: BookingSchema):
    booking.append(booking)
    return bookings


@router.get("/")
async def index(page: int = 0):
    return bookings


@router.get("/{booking_id}")
async def get(booking_id: int):
    return get_booking(booking_id)


@router.delete("/{booking_id}")
async def delete(booking_id: int):
    get_booking(booking_id)
    del bookings[booking_id]
    return bookings


@router.put("/{booking_id}")
async def update(booking_id: int, booking: BookingSchema):
    get_booking(booking_id)
    bookings[booking_id] = booking
    return bookings