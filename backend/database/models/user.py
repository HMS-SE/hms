from database import Base
from schemas.user import UserSex, UserType
from sqlalchemy import BigInteger, Column, Date, Enum, Integer, String


class User(Base): 
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False) 
    email = Column(String, unique=True, index=True) 
    password = Column(String, nullable=False) 
    date_of_birth = Column(Date)
    sex = Column(Enum(UserSex)) 
    phone_no = Column(BigInteger) 
    address = Column(String)
    user_type = Column(Enum(UserType), nullable=False) 
