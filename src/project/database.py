import os
from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# Load environment variables
# load_dotenv()
# Load environment variables from the correct path
load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))


# DATABASE_URL = os.getenv('DATABASE_URL') or "postgresql://project:password@localhost:5432/project"

# POSTGRES_USER = os.getenv('POSTGRES_USER')
# POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
# POSTGRES_HOST = os.getenv('POSTGRES_HOST')
# POSTGRES_PORT = os.getenv('POSTGRES_PORT')
# POSTGRES_DB = os.getenv('POSTGRES_DB')

# DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

DB_USER = os.getenv("POSTGRES_USER", "project")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")  # Use localhost for local development
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "project")


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Print connection details for debugging
print(f"Attempting to connect to database with URL: {DATABASE_URL}")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# def get_db(request: Request):
#     return request.state.db

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
