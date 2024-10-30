from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from sqlalchemy.orm import Session

from project.database import get_db
from project.models import User
from project.repositories.users import create, get_user_by_username
from project.schemas.users import UserResponseSchema, UserCreateSchema
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix='/users',
    tags=['users']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @router.get('/get-password')
# def get_password():
#     return pwd_context.hash('Admin123!')
# tylko do testu

SECRET_KEY = '4fe8e9ab1e8732ff788a89b58b52cbd1046ab1691c2777accd372fb4f596dfd8'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    'ppalma': {
        'username': 'ppalma',
        'full_name': 'Paulina Palma',
        'email': 'paulina.anna.palma@gqmail.com',
        'hashed_password': '$2b$12$TVbdyqcTMTlnoDwsuJIkPePjva1rSVjykYW2YpZkUxgzc70gtFtS2',
        'disabled': False
    }
}


class UserInDB(UserResponseSchema):
    hashed_password: str
#     dziedziczy po ... dlatego w schema nie dodaliśmy password
# później wymienimy na SQL Alchemy


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
# funkcja szukająca user'a w naszej bazie - przeniesiona pozniej do repozytorium


def authenticate_user(fake_db, username: str, password: str):
    user = get_user_by_username(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
#     liczymy hash hasła


def get_password_hash(password):
    return pwd_context.hash(password)
# weryfikujemy hash


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# @router.post('/token')
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail='Incorrect username or password',
#             headers={'WWW-Authenticate': 'Bearer'}
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={'sub': user.username}, expires_delta=access_token_expires
#     )
#     return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/token')
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}
# spr czy użytkownik jest zalogowany


# @router.post("/", response_model=UserResponseSchema, status_code=201)
# async def add(user: UserCreateSchema, db: Session = Depends(get_db)):
#     """Create a new user"""
#     hashed_password = get_password_hash(user.password)
#     try:
#         new_user = create(
#             db=db,
#             username=user.username,
#             hashed_password=hashed_password,
#             email=user.email,
#             full_name=user.full_name,
#             disabled=user.disabled
#         )
#     except IntegrityError:
#         db.rollback()  # Rollback if there’s an integrity error
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User with this username or email already exists."
#         )
#     return new_user # This will automatically exclude the password in the response


@router.post("/", status_code=201)
async def add(user: UserCreateSchema, db: Session = Depends(get_db)):
    """Create a new user"""
    hashed_password = get_password_hash(user.password)
    try:
        new_user = create(
            db=db,
            username=user.username,
            hashed_password=hashed_password,
            email=user.email,
            full_name=user.full_name,
            disabled=user.disabled
        )
    except IntegrityError:
        db.rollback() # Rollback if there’s an integrity error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username or email already exists."
        )
    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "full_name": new_user.full_name,
        "disabled": new_user.disabled
    }


@router.get("/all-users")
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()
