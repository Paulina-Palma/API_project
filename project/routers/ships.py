from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from project.database import get_db
from project.schemas.ships import ShipSchema
from project.repositories.ships import create, update_by_id, update_all, fetch_one, fetch_all, delete_by_id

router = APIRouter(
    prefix='/ships',
    tags=['ships']
)

@router.post('/', status_code=201)
async def add(ship: ShipSchema, db: Session = Depends(get_db)):
    """Create a new ship."""
    new_ship = create(
        db=db,
        name=ship.name,
        max_speed=ship.max_speed,
        distance=ship.distance,
        cost_per_day=ship.cost_per_day
    )
    return new_ship  # Return the created ship


@router.get('/')
async def index(db: Session = Depends(get_db)):
    """Fetch all ships."""
    ships = fetch_all(db=db)
    return ships  # Return all ships from the database


@router.get('/{ship_id}', response_model=ShipSchema)
async def get(ship_id: int, db: Session = Depends(get_db)):
    """Fetch a single ship by its ID."""
    ship = fetch_one(db=db, ship_id=ship_id)
    if not ship:
        raise HTTPException(status_code=404, detail='Ship not found')
    return ship  # Return the ship if found


@router.delete('/{ship_id}', status_code=204)
async def delete(ship_id: int, db: Session = Depends(get_db)):
    """Delete a ship by its ID."""
    deleted_ship = delete_by_id(db=db, ship_id=ship_id)
    if not deleted_ship:
        raise HTTPException(status_code=404, detail='Ship not found')
    return {"message": "Ship deleted successfully"}  # Success message (status 204 implies no content)


@router.put('/{ship_id}', response_model=ShipSchema)
async def edit(ship_id: int, ship: ShipSchema, db: Session = Depends(get_db)):
    """Update a ship by its ID."""
    updated_ship = update_by_id(db=db, ship_id=ship_id, **ship.dict())
    if not updated_ship:
        raise HTTPException(status_code=404, detail='Ship not found')
    return updated_ship  # Return the updated ship data


@router.put('/update_all', status_code=200)
async def update_all_ships(ship: ShipSchema, db: Session = Depends(get_db)):
    """Update all ships with the same values."""
    updated_ships = update_all(db=db, **ship.dict())
    if not updated_ships:
        raise HTTPException(status_code=404, detail="No ships found to update")
    return updated_ships  # Return the updated list of ships
