from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from project.database import Base, engine

Base.metadata.create_all(bind=engine)


class Ship(Base):
    __tablename__ = "ships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    max_speed = Column(Float)
    distance = Column(Float)
    cost_per_day = Column(Float)

    # Add this relationship to bookings
    bookings = relationship("Booking", back_populates="ship")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    bookings = relationship("Booking", back_populates="user")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    spaceship_id = Column(Integer, ForeignKey("ships.id"))
    date_start = Column(Date)
    date_end = Column(Date)
    total_cost = Column(Float)

    user = relationship("User", back_populates="bookings")
    ship = relationship("Ship", back_populates="bookings")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    phone = Column(String, index=True)
    email = Column(String, index=True)
    document_number = Column(String, unique=True, index=True)

    # Add this relationship to bookings
    bookings = relationship("Booking", back_populates="customer")
