from pydantic import BaseModel
from datetime import datetime

##Class to create user object
class Message(BaseModel):
    content:str
    roomId:str
    timestamp:datetime
