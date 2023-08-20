#!/usr/bin/python3

from sqlalchemy import create_engine #engine to create
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    db = argv[3]

    dbUrl = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user_name, password, db)

    engine = create_engine(dbUrl)
    Session = sessionmaker(bind = engine)
    session = Session() #return fn

    for instance in session.query(State).order_by(State.id):
        print("{}:{}".format(instance.id, instance.name))
