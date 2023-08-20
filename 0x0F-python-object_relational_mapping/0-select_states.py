#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            password=argv[2],
            db=argv[3],
            port=3306
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states_list = cur.fetchall()
    for state in states_list:
        print(state)
    cur.close()
    conn.close()
