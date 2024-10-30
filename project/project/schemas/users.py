from typing import Optional
from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    password: str #hasło miało być w innym miejscu, ale router widzi brak relacji
    email: str | None = None
    full_name: Optional[str] | None = None
    disabled: Optional[bool] | None = None #włączony lub wyłączony

    class Config:
        # orm_mode = True  # Enables compatibility with ORM models but renamed to from_attributes
        from_attributes = True


class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str | None = None
    full_name: Optional[str] | None = None
    disabled: Optional[bool] | None = None

    class Config:
        # orm_mode = True  #renamed to from_attributes
        from_attributes = True
