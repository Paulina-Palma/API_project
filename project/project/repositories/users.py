from sqlalchemy.orm import Session
from project.models import User
from typing import Optional


def create(db: Session, username: str, hashed_password: str, email: str, full_name: str, disabled: bool = False):
    """Creates a new user record in the database."""
    db_user = User(
        username=username,
        hashed_password=hashed_password,
        email=email,
        full_name=full_name,
        disabled=disabled
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()
