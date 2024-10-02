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
    user_id = Column(Integer, ForeignKey("users.id"))
    ship_id = Column(Integer, ForeignKey("ships.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    total_cost = Column(Float)

    user = relationship("User", back_populates="bookings")
    ship = relationship("Ship", back_populates="bookings")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    document_number = Column(String, unique=True, index=True)
