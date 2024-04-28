#!/usr/bin/python3`
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
DB_URL = 'mysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db'

# Create a database engine
engine = create_engine(DB_URL)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Define the base class for ORM models
Base = declarative_base()

# Define the State model
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

# Function to add all USA states to the database
def add_usa_states():
    # List of USA states
    usa_states = [
        "Alabama", "Alaska", "Arizona", "Arkansas",
        "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
        "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
        "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
        "New Hampshire", "New Jersey", "New Mexico", "New York",
        "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
        "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
        "West Virginia", "Wisconsin", "Wyoming"
    ]

    # Create a session
    session = Session()

