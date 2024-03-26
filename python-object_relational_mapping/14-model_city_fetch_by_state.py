#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    """ Perform inner join """
    innerj_result = session.query(State.name, City.id, City.name).join(
                    City, State.id == City.state_id).all()

    for state_name, city_id, city_name in innerj_result:
        print(f"{state_name}: ({city_id}) {city_name}")
