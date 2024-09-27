from fastapi import APIRouter, HTTPException
from project.schemas.bookings import BookingSchema

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)


bookings = []


@router.post("/", status_code=201)
async def add(booking: BookingSchema):
    bookings.append(booking)
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


def get_booking(booking_id: int):
    try:
        return bookings[booking_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Booking not found")
