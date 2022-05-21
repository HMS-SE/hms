from datetime import date
from enum import Enum, auto

from pydantic import BaseModel


class UserType(Enum): 
    doctor = "doctor"
    patient = "patient"
    administrator = "administrator"

class UserSex(Enum): 
    male = "male"
    female = "female"
    other = "other"

class UserBase(BaseModel):
    name: str 
    email: str 
    user_type: UserType 

    date_of_birth: date | None
    sex: UserSex | None
    phone_no: int | None 
    address: str | None

class UserCreate(UserBase): 
    password: str

class User(UserBase):
    id: int

    class Config: 
        orm_mode = True 
     
    

