#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()

        for state in states:
            print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
