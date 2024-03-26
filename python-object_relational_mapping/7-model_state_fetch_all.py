#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()

states = session.query(State).all()
for state in states:
    print(f"{state.id}: {state.name}")
