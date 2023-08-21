#!/usr/bin/python3
"""import my sql module"""
import MySQLdb
# import argv(list to store sommand line args) from sys module
from sys import argv
# checks if this is the script being run as main program
if __name__ == "__main__":
    # est connection to mysql db using variables in the command line args
    state_name = argv[4]
    conmysql = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
        )
    # create a cursor obj used to execute SQL queries & fetch frm db
    curobj = conmysql.cursor()
    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """
    # execute method() executes the query
    curobj.execute(query, (state_name,))
    # fetched all rows returned by query & store in states_list
    cities_tuple = curobj.fetchall()
    cities_list = []
    for city in cities_tuple:
        cities_list.append(city[0])
    print(", ".join(cities_list))
    # closes cursor and db connection & release resources
    curobj.close()
    conmysql.close()
