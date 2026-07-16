from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

pwdContext = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
oauth2_scheme= OAuth2PasswordBearer(tokenUrl = "Login")

##JWT
SECRET_KEY = "MY-SUPPER-SUPPER-SUPPER-LONG-KEY"
ALGORITHM = "HS256"
EXPIRATION_MINUTE = 30

##Function to hash any password
def hashPassword(password:str):
    return pwdContext.hash(password)

##Function to verify password
def verifyPassword(password:str, hashedPassword):
    return pwdContext.verify(password, hashedPassword)

##Function to create jwt token
def generateJwtToken(data:dict):
    dayta = data.copy()
    time = datetime.utcnow()
    time+= timedelta(minutes = EXPIRATION_MINUTE)
    dayta.update({"exp":time})
    token = jwt.encode(dayta, SECRET_KEY, algorithm = ALGORITHM)
    return token

##Function to get current user email 
def getCurrentUserEmail(token = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
    email = payload.get("sub")
    return email




