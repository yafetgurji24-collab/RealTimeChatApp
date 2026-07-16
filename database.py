from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///./chat.db")
sessionMaker= sessionmaker(autocommit=False, autoflush=False, bind=engine)

