from fastapi import FastAPI, Request, Response
from project.routers import ships, bookings, customers, attachments
from project.database import engine
from sqlalchemy.orm import sessionmaker


app = FastAPI()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# engine - połączenie z bazą danych


@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)

    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response


app.include_router(ships.router)
app.include_router(bookings.router)
app.include_router(customers.router)
app.include_router(attachments.router)
