#!/usr/bin/python3
"""This script script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa
"""

''' Module that connects python script to a database'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_ = argv[4]
    queriedState = session.query(State).filter(State.name == state_).first()
    if queriedState:
        print(queriedState.id)
    else:
        print("Not found")

    session.close()
