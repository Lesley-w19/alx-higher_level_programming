#!/usr/bin/python3
"""
11-model_state_insert.py
a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    user = argv[1]
    passwrd = argv[2]
    db_n = argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwrd, db_n),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = State(name="Louisiana")

    session.add(state)
    session.commit()

    print(state.id)

    session.close()


if __name__ == "__main__":
    main()
