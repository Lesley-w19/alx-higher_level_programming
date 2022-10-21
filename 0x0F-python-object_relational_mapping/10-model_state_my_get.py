#!/usr/bin/python3
"""
10-model_state_my_get.py
 a script that prints the State object with the name
 passed as argument from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    user = argv[1]
    passwrd = argv[2]
    db_name = argv[3]
    s_input = argv[4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwrd, db_name),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    sql_query = session.query(State).filter(State.name.like(s_input,))
    order_query = sql_query.order_by(State.id)

    if order_query.count() == 0:
        print("Not found")
    else:
        for states in order_query:
            print("{:d}".format(states.id))

    session.close()


if __name__ == '__main__':
    main()
