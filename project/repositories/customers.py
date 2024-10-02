from sqlalchemy.orm import Session
from project.models import Customer


def create(db: Session, name: str, address: str, email: str, phone: str, document_number: str):
    """Create a new customer."""
    db_customer = Customer(name=name, address=address, email=email, phone=phone, document_number=document_number)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def fetch_one(db: Session, customer_id: int):
    """Fetch a single customer by its ID."""
    return db.query(Customer).filter(Customer.id == customer_id).first()


def fetch_all(db: Session):
    """Fetch all customers."""
    return db.query(Customer).all()


def update_by_id(db: Session, customer_id: int, **kwargs):
    """Update a customer by its ID."""
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        return None
    for key, value in kwargs.items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer)
    return customer


def delete_by_id(db: Session, customer_id: int):
    """Delete a customer by its ID."""
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        return None
    db.delete(customer)
    db.commit()
    return customer
