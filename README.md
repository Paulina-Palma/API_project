# 🚀FastAPI Ship Booking API

This project is a RESTful API built using  **FastAPI**  for managing ships, customers, and bookings. It allows users to create and manage bookings for different ships and customers. The project uses  **PostgreSQL**  for data persistence and  **SQLAlchemy ORM**  for database interactions. The project is likely containerized using  **Docker**  for easier deployment and scalability.

## 📋 Features

-   **CRUD operations**  for  **Customers**,  **Ships**, and  **Bookings**
-   **Pydantic models**  for data validation
-   **SQLAlchemy ORM**  for database interaction
-   **PostgreSQL**  as the database
-   **Alembic**  for database migrations (if applicable)
-   **Docker**  support for containerized deployment

## 📂 Project Structure

`project/`   
├── `app/`   
 │     ├── `__init__.py`   
 │     ├── `main.py`                # Entry point for FastAPI app   
 │     ├── `models.py`              # SQLAlchemy models for Customers, Ships, and Bookings   
 │     ├── `database.py`            # Database connection setup   
 │     ├── `schemas/`   
 │      │     ├── `customers.py`       # Pydantic schemas for Customers   
 │      │     ├── `ships.py`           # Pydantic schemas for Ships   
 │      │     └── `bookings.py`        # Pydantic schemas for Bookings   
 │     ├── `repositories/`   
 │      │     ├── `customers.py`       # Repository functions for interacting with Customers in DB   
 │      │     ├── `ships.py`           # Repository functions for interacting with Ships in DB   
 │      │     └── `bookings.py`        # Repository functions for interacting with Bookings in DB    
 │     └── `routers/`   
 │          ├── `customers.py`       # API routes for Customers   
 │          ├── `ships.py`           # API routes for Ships   
 │          └── `bookings.py`        # API routes for Bookings    
├── `tests/`                     # Test cases for the API   
├── `alembic/`                   # Alembic for migrations (if applicable)  
├── `Dockerfile`                 # Docker setup for containerizing the app   
└── `README.md`                  # Project documentation   



## 🛠️ Setup and Installation

### Prerequisites

-   Python 3.10+
-   PostgreSQL
-   Docker (optional, if you are using Docker for deployment)
&nbsp;
### 1. Clone the Repository

`git clone https://github.com/yourusername/ship-booking-api.git
cd ship-booking-api`  

&nbsp;
### 2. Create a Virtual Environment

source venv/bin/activate  # For Linux/Mac
#On Windows:
#venv\Scripts\activate
  
&nbsp;
### 3. Install Dependencies


`pip install -r requirements.txt` 

&nbsp;
### 4. Configure the Database

Update your  **`database.py`**  file with the PostgreSQL connection details:

`SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost/<database>"` 

&nbsp;
### 5. Run Database Migrations (if using Alembic)


`alembic upgrade head` 

&nbsp;
### 6. Run the Application


`uvicorn app.main:app --reload` 

The API will be running at  **`http://127.0.0.1:8000`**.\

&nbsp;
### 7. (Optional) Run with Docker

If you're using Docker, build and run the container:


`docker build -t ship-booking-api .
docker run -p 8000:8000 ship-booking-api`

&nbsp;
## 📄 API Endpoints

### Customers

-   **POST**  `/customers/`  - Create a new customer
-   **GET**  `/customers/`  - Get all customers
-   **GET**  `/customers/{customer_id}`  - Get a specific customer by ID
-   **PUT**  `/customers/{customer_id}`  - Update a customer by ID
-   **DELETE**  `/customers/{customer_id}`  - Delete a customer by ID

### Ships

-   **POST**  `/ships/`  - Create a new ship
-   **GET**  `/ships/`  - Get all ships
-   **GET**  `/ships/{ship_id}`  - Get a specific ship by ID
-   **PUT**  `/ships/{ship_id}`  - Update a ship by ID
-   **DELETE**  `/ships/{ship_id}`  - Delete a ship by ID

### Bookings

-   **POST**  `/bookings/`  - Create a new booking
-   **GET**  `/bookings/`  - Get all bookings
-   **GET**  `/bookings/{booking_id}`  - Get a specific booking by ID
-   **PUT**  `/bookings/{booking_id}`  - Update a booking by ID
-   **DELETE**  `/bookings/{booking_id}`  - Delete a booking by ID


## 🧪 Running Tests

To run the tests, use the following command:
`pytest` 

Make sure you have set up an SQLite database (or any other testing database) for running tests to avoid modifying the production database.


## 🚀 Deployment

You can deploy the FastAPI application using  **Docker**  or any cloud service that supports FastAPI. If using Docker, make sure to:

1.  Build the Docker image.
2.  Push the Docker image to a container registry.
3.  Deploy it using a cloud provider such as AWS, Azure, or Google Cloud.

## 📚 Further Documentation

FastAPI provides built-in interactive API documentation:

-   Swagger UI:  **`http://127.0.0.1:8000/docs`**
-   ReDoc:  **`http://127.0.0.1:8000/redoc`**
