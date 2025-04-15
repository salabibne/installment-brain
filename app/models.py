from sqlalchemy import Column, Integer, String,BOOLEAN
from app.database import Base

class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    isVerified= Column(BOOLEAN,default=False)
