from sqlalchemy import Column, Integer, String, Float
from project.database import Base, engine

Base.metadata.create_all(bind=engine)


class Ship(Base):
    __tablename__ = 'ships'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    max_speed = Column(Float)
    distance = Column(Float)
    cost_per_day = Column(Float)
