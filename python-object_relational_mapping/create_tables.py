#!/usr/bin/python3
"""
Script to create the states table in hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a table in database
    Base.metadata.create_all(engine)
