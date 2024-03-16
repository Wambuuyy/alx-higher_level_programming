#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
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

    # Query all State objects with a name containing the letter 'a'
    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%')).all()

    # Delete the selected State objects
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()
