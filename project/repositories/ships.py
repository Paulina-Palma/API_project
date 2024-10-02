from sqlalchemy.orm import Session
from project.models import Ship


def create(db: Session, name: str, max_speed: float, distance: float, cost_per_day: float):
    """Creates a new ship record in the database."""
    db_ship = Ship(name=name, max_speed=max_speed, distance=distance, cost_per_day=cost_per_day)
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship) # Refresh to get the updated state after insert
    return db_ship


def fetch_one(db: Session, ship_id: int):
    """Fetches a single ship by its ID, returns None if not found."""
    return db.get(Ship, ship_id)
    # return db.query(Ship).filter(Ship.id == ship_id).first()


def fetch_all(db: Session, ship_id: int):
    """Fetches all ships from the database."""
    return db.query(Ship).all()


def update_by_id(db: Session, ship_id: int, **kwargs):
    ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if not ship:
        return None  # Ship not found

    # Update the attributes dynamically
    for key, value in kwargs.items():
        setattr(ship, key, value)

    db.commit()  # Commit the transaction
    db.refresh(ship)  # Refresh the instance to get the latest data from the DB
    return ship


def update_all(db: Session, **kwargs):
    """Update all ships with the provided values."""
    ships = db.query(Ship).all()
    if not ships:
        return None  # If there are no ships to update, return None

    for ship in ships:
        for key, value in kwargs.items():
            setattr(ship, key, value)  # Update each ship's attributes

    db.commit()  # Commit the transaction
    return ships  # Return the updated list of ships


def delete_by_id(db: Session, ship_id: int):
    """Deletes a ship by its ID, returns the deleted ship or None if not found."""
    ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if not ship:
        return None
    db.delete(ship)
    db.commit()
    return ship
