from sqlalchemy.orm import Session
from sqlalchemy import update
from project.models import Ship


def create(db: Session, name: str, max_speed: float, distance: float, cost_per_day: float):
    db_ship = Ship(name=name, max_speed=max_speed, distance=distance, cost_per_day=cost_per_day)
    print(db)
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship
#   nowy statek


def fetch_one(db: Session, ship_id: int):
    return db.get(Ship, ship_id)
    # return db.query(Ship).filter(Ship.id == ship_id).first()
# pobieranie statku


def update_by_id(db: Session, ship_id: int, **kwargs):
    del kwargs['id']
    db_ship = db.execute(update(Ship).where(Ship.id ==ship_id).values(**kwargs))
    db.commit()
    return db_ship


def delete_one(db: Session, ship_id: int):
    db.query(Ship).filter(Ship.id == ship_id).delete()
    db.commit()
    return db.query(Ship).all()
