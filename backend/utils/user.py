from database.models import user as user_model
from fastapi import HTTPException, status
from passlib.context import CryptContext
from schemas import user as user_schema
from sqlalchemy.orm import Session

from utils.auth import verify_jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def authenticate_user(db: Session, email: str, password: str) -> bool | user_model.User :
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_current_user(db: Session, token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    jwt_payload = verify_jwt(token)
    if jwt_payload is False: 
        raise credentials_exception 
    
    user = get_user_by_email(db, jwt_payload["email"])

    if user is None:
        raise credentials_exception

    return user

def get_user(db: Session, user_id: int) -> user_model.User | None: 
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> user_model.User | None: 
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def create_user(db: Session, user: user_schema.UserCreate) -> user_model.User:
    pwd_hash = get_password_hash(user.password)
    user.password = pwd_hash 

    new_user = user_model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
