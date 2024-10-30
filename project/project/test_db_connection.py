from sqlalchemy import create_engine, text

# Update with the correct URL
DATABASE_URL = "postgresql://project:password@localhost:6543/project"

try:
    engine = create_engine(DATABASE_URL, echo=True)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful. Result:", result.fetchone())
except Exception as e:
    print("Database connection failed:", e)
