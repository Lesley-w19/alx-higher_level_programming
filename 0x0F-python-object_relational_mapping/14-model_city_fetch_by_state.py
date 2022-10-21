#!/usr/bin/python3
"""
 a script 14-model_city_fetch_by_state.py
 that prints all City objects from the
 database hbtn_0e_14_usa:
"""

from sys import argv
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


def main():
    user = argv[1]
    passwrd = argv[2]
    db_name = argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwrd, db_name),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    sql_query = session.query(State, City)
    join_query = sql_query.filter(State.id == City.state_id)
    order_query = join_query.order_by(City.id).all()

    for state, city in order_query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
