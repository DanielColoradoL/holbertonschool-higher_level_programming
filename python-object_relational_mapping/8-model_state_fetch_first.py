#!/usr/bin/python3
"""Start link class to table in database
and print the first state object
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")
