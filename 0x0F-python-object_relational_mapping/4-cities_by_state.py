#!/usr/bin/python3
"""import my sql module"""
import MySQLdb
# import argv(list to store sommand line args) from sys module
from sys import argv
# checks if this is the script being run as main program
if __name__ == "__main__":
    # est connection to mysql db using variables in the command line args
    conmysql = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
        )
    # create a cursor obj used to execute SQL queries & fetch frm db
    curobj = conmysql.cursor()
    # execute method() executes the query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY id ASC
    """
    curobj.execute(query)
    # fetched all rows returned by query & store in states_list
    cities_list = curobj.fetchall()
    for city in cities_list:
        print(city)
    # closes cursor and db connection & release resources
    curobj.close()
    conmysql.close()
