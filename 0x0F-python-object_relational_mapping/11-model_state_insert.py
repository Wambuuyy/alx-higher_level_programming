#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
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

    # Create the State object for Louisiana
    louisiana = State(name="Louisiana")

    # Add the State object to the session
    session.add(louisiana)

    # Commit the session to the database
    session.commit()

    # Print the new state's ID
    print(louisiana.id)

    # Close the session
    session.close()
