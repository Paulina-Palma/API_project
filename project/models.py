from sqlalchemy import Column, Date, Integer, String, Float, ForeignKey
from project.database import Base, engine
from sqlalchemy.orm import relationship

Base.metadata.create_all(bind=engine)


class Ship(Base):
    __tablename__ = 'ships'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    max_speed = Column(Float)
    distance = Column(Float)
    cost_per_day = Column(Float)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    # customer_id = Column(Integer, ForeignKey("customer.id"))
    # spaceship_id = Column(Integer, ForeignKey("ships.id"))
    customer_id = Column(Integer)
    spaceship_id = Column(Integer)
    date_start = Column(Date)
    date_end = Column(Date)
    total_cost = Column(Float)

    # customer = relationship("Customer", back_populates="customers")
    # ship = relationship("Ship", back_populates="ships")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    phone = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    document_number = Column(String, unique=True, index=True)
