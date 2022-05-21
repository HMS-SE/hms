from dependencies import get_db, oauth2_scheme
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas import auth as auth_schema
from schemas import user as user_schema
from sqlalchemy.orm import Session
from utils import auth as auth_utils
from utils import user as user_utils

router = APIRouter(prefix="/users")

@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_utils.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_utils.create_user(db=db, user=user)

@router.post("/login", response_model=auth_schema.Token)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()): 
    user = user_utils.authenticate_user(db, form_data.username, form_data.password) 

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    access_token = auth_utils.create_access_token({"sub": form_data.username})

    return {
        "access_token": access_token, 
        "token_type": "Bearer"
    }

@router.get("/me", response_model=user_schema.User)
def read_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = user_utils.get_current_user(db, token)

    return current_user
