#!/usr/bin/python3

import MySQLdb

from sys import argv

if __name__ == '__main__':

    """
    argv[0] shebang
    argv[1] mysql username,
    argv[2] mysql password
    argv[3] database name
    """

    my_db = MySQLdb.connect(host='localhost',user=argv[1],password=argv[2],db=argv[3],port=3306)

    my_cursor = my_db.cursor()

    my_cursor.execute("SELECT * FROM states")

    my_data = my_cursor.fetchall()

    for data in my_data:
        print(data)
