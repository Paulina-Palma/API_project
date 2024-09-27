from fastapi import FastAPI
from project.routers import ships
from project.routers import bookings
from project.routers import customers

app = FastAPI()
app.include_router(ships.router)
app.include_router(bookings.router)
app.include_router(customers.router)

