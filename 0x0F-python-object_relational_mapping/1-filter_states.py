#!/usr/bin/python3


# import my sql module
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

query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"

# exucte method() executes the queru
curobj.execute(query)

# fetched all tows returned by query & store in states_list

states_list = curobj.fetchall()

for state in states_list:
    print(state)

# closes curdoe and db connection & release resources
curobj.close()
conmysql.close()
