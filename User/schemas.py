from pydantic import BaseModel

##Class to create user object 
class User(BaseModel):
    email:str
    password:str

##Class to create user object but with only information that can be sent back to the client
class UserResponse(BaseModel):
    email:str
