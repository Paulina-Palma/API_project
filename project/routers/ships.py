from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from project.database import get_db
from project.schemas.ships import ShipSchema
from project.repositories.ships import create

router = APIRouter(
    prefix='/ships',
    tags=['ships']
)


ships = []


@router.post('/', status_code=201)
async def add(ship: ShipSchema, db: Session = Depends(get_db)):
    create(
        db=db,
        name=ship.name,
        max_speed=ship.max_speed,
        distance=ship.distance,
        cost_per_day=ship.cost_per_day
    )
    return ships


@router.get('/')
async def index(page: int = 0):
    return ships


@router.get('/{ship_id}')
async def get(ship_id: int) -> ShipSchema:
    return get_ship(ship_id)


@router.delete('/{ship_id}')
async def delete(ship_id: int):
    get_ship(ship_id)
    del ships[ship_id]
    return ships


@router.put('/{ship_id}')
async def update(ship_id: int, ship: ShipSchema):
    get_ship(ship_id)
    ships[ship_id] = ship
    return ships


def get_ship(ship_id: int) -> ShipSchema:
    try:
        return ships[ship_id]
    except IndexError:
        raise HTTPException(status_code=404, detail='Ship not found')
