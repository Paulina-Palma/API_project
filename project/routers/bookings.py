from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from project.database import get_db
from project.schemas.bookings import BookingSchema
from project.repositories.bookings import create, fetch_one, fetch_all, update_by_id, delete_by_id

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)


@router.post("/", status_code=201)
async def add(booking: BookingSchema, db: Session = Depends(get_db)):
    """Create a new booking."""
    new_booking = create(
        db=db,
        customer_id=booking.customer_id,
        spaceship_id=booking.spaceship_id,
        date_start=booking.date_start,
        date_end=booking.date_end,
        total_cost=booking.total_cost
    )
    return new_booking


@router.get("/")
async def index(db: Session = Depends(get_db)):
    """Fetch all bookings."""
    bookings = fetch_all(db=db)
    return bookings


@router.get("/{booking_id}", response_model=BookingSchema)
async def get(booking_id: int, db: Session = Depends(get_db)):
    """Fetch a single booking by its ID."""
    booking = fetch_one(db=db, booking_id=booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


@router.delete("/{booking_id}", status_code=204)
async def delete(booking_id: int, db: Session = Depends(get_db)):
    """Delete a booking by its ID."""
    booking = delete_by_id(db=db, booking_id=booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted successfully"}


@router.put("/{booking_id}", response_model=BookingSchema)
async def update(booking_id: int, booking: BookingSchema, db: Session = Depends(get_db)):
    """Update a booking by its ID."""
    updated_booking = update_by_id(db=db, booking_id=booking_id, **booking.dict())
    if not updated_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return updated_booking
