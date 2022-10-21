#!/usr/bin/python3
"""
9-model_state_filter_a.py
a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    sql_query = session.query(State).filter(State.name.like('%a%'))
    order_query = sql_query.order_by(State.id)

    for states in order_query:
        print("{:d}: {}".format(states.id, states.name))

    session.close()


if __name__ == '__main__':
    main()
