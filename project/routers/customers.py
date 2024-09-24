from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix='/customers'
    tags=['customers']
)

class Customer(BaseModel):
    customer_id: int
    name: str
    adress: str
    document_number: int
