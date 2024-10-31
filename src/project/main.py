from fastapi import FastAPI, Request, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from project.routers import ships, bookings, customers, attachments, users
from project.database import engine, SessionLocal
from sqlalchemy.orm import sessionmaker, Session
from project.database import get_db
from datetime import datetime
import pytz
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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

@app.get("/health", tags=["health"])
async def health_check():
    logger.debug("Health check endpoint called")
    try:
        response = {
            "status": "healthy",
            "version": "1.0.0",
            "timestamp": str(datetime.now())
        }
        logger.debug(f"Returning response: {response}")
        return response
    except Exception as e:
        logger.error(f"Error in health check: {e}")
        raise

# @app.get("/health", tags=["health"])
# async def health_check():
#     logger.debug("Health check endpoint called")
    
#     response = {
#         "status": "healthy",
#         "version": "1.0.0",
#         "timestamp": str(datetime.now())
#     }
    
#     logger.debug(f"Returning response: {response}")
#     return response

# @app.get("/health", tags=["health"])
# async def health_check():
#     # Simple response without database check
#     return {
#         "status": "healthy",
#         "version": "1.0.0",
#         "timestamp": datetime.now().isoformat()
#     }

# @app.get("/health", tags=["health"])
# async def health_check(db: Session = Depends(get_db)):
#     try:
#         # Test database connection
#         result = db.execute("SELECT 1").scalar()
#         db_status = "healthy" if result == 1 else "unhealthy"
#     except Exception as e:
#         db_status = f"unhealthy: {str(e)}"

#     # Get current timestamp in UTC
#     current_time = datetime.now(pytz.UTC).isoformat()

#     response = {
#         "status": "healthy",
#         "version": "1.0.0",
#         "database": db_status,
#         "environment": "development",
#         "timestamp": current_time,
#         "details": {
#             "database_connected": db_status == "healthy",
#             "api_version": "1.0.0",
#             "uptime": "available"
#         }
#     }
    
#     return response

# one option - here we can add prefix 
# app.include_router(ships.router, prefix="/ships", tags=["ships"])
# app.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
# app.include_router(customers.router, prefix="/customers", tags=["customers"])
# app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(attachments.router, prefix="/attachments", tags=["attachments"])

app.include_router(ships.router)
app.include_router(bookings.router)
app.include_router(customers.router)
app.include_router(users.router)
app.include_router(attachments.router)
