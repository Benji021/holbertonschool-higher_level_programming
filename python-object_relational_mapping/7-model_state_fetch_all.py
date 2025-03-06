#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def list_states(mysql_user, mysql_password, db_name):
    # Create the engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost:3306/{db_name}')
    
    # Create all tables if they don't already exist (using Base metadata)
    Base.metadata.create_all(engine)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all State objects and order by id in ascending order
    states = session.query(State).order_by(State.id).all()
    
    # Loop through the results and print each State object
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()

if __name__ == '__main__':
    # Check if the script is being executed directly
    if len(sys.argv) == 4:
        mysql_user = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        
        list_states(mysql_user, mysql_password, db_name)
    else:
        print("Usage: ./list_states.py <mysql_username> <mysql_password> <database_name>")
