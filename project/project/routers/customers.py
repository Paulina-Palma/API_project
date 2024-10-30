from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from project.database import get_db
from project.schemas.customers import CustomerResponseSchema, CustomerCreateSchema
from project.repositories.customers import create, fetch_one, fetch_all, update_by_id, delete_by_id

router = APIRouter(
    prefix='/customers',
    tags=['customers']
)


@router.post("/", status_code=201)
async def add(customer: CustomerCreateSchema, db: Session = Depends(get_db)):
    """Create a new customer."""
    new_customer = create(
        db=db,
        name=customer.name,
        address=customer.address,
        email=customer.email,
        phone=customer.phone,
        document_number=customer.document_number
    )
    return new_customer


@router.get("/")
async def index(db: Session = Depends(get_db)):
    """Fetch all customers."""
    customers = fetch_all(db=db)
    return customers


@router.get("/{customer_id}", response_model=CustomerResponseSchema)
async def get(customer_id: int, db: Session = Depends(get_db)):
    """Fetch a single customer by ID."""
    customer = fetch_one(db=db, customer_id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.delete("/{customer_id}", status_code=204)
async def delete(customer_id: int, db: Session = Depends(get_db)):
    """Delete a customer by ID."""
    customer = delete_by_id(db=db, customer_id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}


@router.put("/{customer_id}", response_model=CustomerResponseSchema)
async def update(customer_id: int, customer: CustomerCreateSchema, db: Session = Depends(get_db)):
    """Update a customer by ID."""
    updated_customer = update_by_id(
        db=db,
        customer_id=customer_id,
        name=customer.name,
        address=customer.address,
        document_number=customer.document_number
    )
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

# @router.put("/{customer_id}", response_model=CustomerSchema)
# async def update(customer_id: int, customer: CustomerCreateSchema, db: Session = Depends(get_db)):
#     """Update a customer by ID."""
#     updated_customer = update_by_id(db=db, customer_id=customer_id, **customer.dict())
#     if not updated_customer:
#         raise HTTPException(status_code=404, detail="Customer not found")
#     return updated_customer