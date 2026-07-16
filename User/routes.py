from fastapi import APIRouter, status, HTTPException, Depends
from User.schemas import User, UserResponse
from database import sessionMaker
from User.models import UserDB
from User.auth import hashPassword, verifyPassword, generateJwtToken
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

##Sign up route for user
@router.post("/signup",response_model = UserResponse, status_code = status.HTTP_201_CREATED)
def signup(user:User):
    db = sessionMaker()
    newUser = UserDB(email = user.email, hashedPassword = hashPassword(user.password))
    db.add(newUser)
    db.commit()
    db.close()
    return user

##Log in route for user
@router.post("/login")
def login(formData:OAuth2PasswordRequestForm = Depends()):
    db = sessionMaker()
    foundUser = db.query(UserDB).filter(UserDB.email == formData.username).first()
    if foundUser != None:
        if verifyPassword(formData.password,foundUser.hashedPassword):
            token = generateJwtToken({"sub":formData.username})
            return {"access_token":token , "token_type": "bearer"}
        else:
            raise HTTPException(status_code = 401, detail = "Unauthorized")
    else:
        raise HTTPException(status_code = 404, detail = "User Not Found")
