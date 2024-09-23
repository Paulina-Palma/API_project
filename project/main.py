from fastapi import FastAPI
from project.routers import ships

app = FastAPI()
app.include_router(ships.router)

