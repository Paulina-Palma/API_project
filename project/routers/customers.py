from fastapi import APIRouter, HTTPException
from project.schemas.customers import CustomerSchema

router = APIRouter(
    prefix='/customers',
    tags=['customers']
    )


customers = []


@router.post("/", status_code=201)
async def add(customer: CustomerSchema):
    customers.append(customer)
    return customers


@router.get("/")
async def index(page: int = 0):
    return customers


@router.get("/{customer_id}")
async def get(customer_id: int):
    return get_customer(customer_id)


@router.delete("/{customer_id}")
async def delete(customer_id: int):
    get_customer(customer_id)
    del customers[customer_id]
    return customers


@router.put("/{customer_id}")
async def update(customer_id: int, customer: CustomerSchema):
    get_customer(customer_id)
    customers[customer_id] = customer
    return customers


def get_customer(customer_id: int):
    try:
        return customers[customer_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="customer not found")
