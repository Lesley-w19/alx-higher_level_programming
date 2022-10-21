#!/usr/bin/python3
"""
8-model_state_fetch_first.py
a script that prints the first State object from the
database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    username = argv[1]
    passwrd = argv[2]
    db_n = argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, passwrd, db_n),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    sql_query = session.query(State).order_by(State.id)

    states_length = sql_query.count()
    first_state = sql_query.first()

    if states_length == 0:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()


if __name__ == "__main__":
    main()
