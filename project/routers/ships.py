from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix='/ships',
    tags=['ships']
    )


class ShipSchema(BaseModel):
    name: str
#     mozna tez inne nazwy zmiennych podawac dalej + typy


ships = []

@router.post('/', status_code=201)
async def add(ship: ShipSchema):
    ships.append(ship)
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
