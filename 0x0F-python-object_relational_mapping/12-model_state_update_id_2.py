#!/usr/bin/python3
"""
12-model_state_update_id_2.py
a script that changes the name of a State object
from the database hbtn_0e_6_usa
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

    sql_query = session.query(State).filter(State.id == 2)

    if sql_query.count() == 0:
        print("Not found")
    else:
        state = sql_query.first()
        state.name = "New Mexico"
        session.add(state)
        session.commit()

    session.close()


if __name__ == '__main__':
    main()
