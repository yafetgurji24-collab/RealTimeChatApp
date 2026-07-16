from database import Base, engine
from sqlalchemy import Column, String, Integer

##Class to create database model for user
class UserDB(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
    email = Column(String)
    hashedPassword = Column(String)

##Initiliaze database
Base.metadata.create_all(bind=engine)