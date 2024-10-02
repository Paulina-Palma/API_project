from sqlalchemy.orm import Session
from project.models import Booking


def create(db: Session, customer_id: int, spaceship_id: int, date_start: date, date_end: date, total_cost: float):
    """Create a new booking."""
    db_booking = Booking(customer_id=customer_id, spaceship_id=spaceship_id, date_start=date_start, date_end=date_end, total_cost=total_cost)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def fetch_one(db: Session, booking_id: int):
    """Fetch a single booking by its ID."""
    return db.query(Booking).filter(Booking.id == booking_id).first()


def fetch_all(db: Session):
    """Fetch all bookings."""
    return db.query(Booking).all()


def update_by_id(db: Session, booking_id: int, **kwargs):
    """Update a booking by its ID."""
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        return None
    for key, value in kwargs.items():
        setattr(booking, key, value)
    db.commit()
    db.refresh(booking)
    return booking


def delete_by_id(db: Session, booking_id: int):
    """Delete a booking by its ID."""
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        return None
    db.delete(booking)
    db.commit()
    return booking
