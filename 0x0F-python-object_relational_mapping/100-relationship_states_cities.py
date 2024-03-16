#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connection to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Create a new State object
    california = State(name='California')
    # Create a new City object
    san_francisco = City(name='San Francisco')
    # Assign the city to the state
    california.cities.append(san_francisco)
    # Add the state and city to the session
    session.add(california)
    # Commit the transaction
    session.commit()
    # Close the session
    session.close()
