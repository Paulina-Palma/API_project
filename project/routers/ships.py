from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/ships',
    tags=['ships']
    )


class ShipSchema(BaseModel):
    name: str
#     mozna tez inne nazwy zmiennych podawac dalej + typy



@router.post('/')
async def add(ship: ShipSchema):
    print(ship)
    return {'message': f'Add new ship {ship.name}'}


@router.get('/')
async def index(page: int = 0):
    return {'message': f'List of ships, page number {page}'}


@router.get('/{ship_id}')
async def get(ship_id: int):
    return {'message': f'Details of ship with id {ship_id}'}


@router.delete('/{ship_id}')
async def delete(ship_id: int):
    return {'message': f'Deleting ship with id {ship_id}'}


@router.put('/{ship_id}')
async def update(ship_id: int):
    return {'message': f'Updating ship with id {ship_id}'}