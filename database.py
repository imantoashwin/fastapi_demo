from sqlalchemy import create_engine # create_engine is used to establish a connection to the database
from sqlalchemy.orm import sessionmaker, declarative_base # sessionmaker is used to create a new session for interacting with the database, declarative_base is used to create a base class for our ORM models
from dotenv import load_dotenv # load_dotenv is used to load environment variables from a .env file
import os # os is used to access environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL") # Get the database URL from environment variables
engine = create_engine(DATABASE_URL) # Establish a connection to the database
sessionlocal = sessionmaker(bind=engine, autoflush=False) # Create a new session for interacting with the database
Base = declarative_base() # Create a base class for our ORM models