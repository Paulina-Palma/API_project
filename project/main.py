from fastapi import FastAPI
from project.routers import bookings, customers, ships

app = FastAPI()
app.include_router(ships.router)
app.include_router(bookings.router)
app.include_router(customers.router)

