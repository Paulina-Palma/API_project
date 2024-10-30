from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from project.routers import ships, bookings, customers, attachments, users
from project.database import engine, SessionLocal
from sqlalchemy.orm import sessionmaker


app = FastAPI(debug=True)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


app.include_router(ships.router, prefix="/ships", tags=["ships"])
app.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(attachments.router, prefix="/attachments", tags=["attachments"])
