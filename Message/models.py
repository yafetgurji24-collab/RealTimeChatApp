from database import Base, engine
from sqlalchemy import Column, Integer, String, DateTime


##Function to create message database
class MessageDB(Base):
    __tablename__ = "Messages"
    id = Column(Integer, primary_key = True)
    user = Column(String)
    roomId = Column(String)
    content = Column(String)
    timestamp = Column(DateTime)

Base.metadata.create_all(bind=engine)