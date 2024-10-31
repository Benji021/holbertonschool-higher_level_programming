#!/usr/bin/python3
"""SQL Injection..."""


import sys
import MySQLdb

if __name__ == '__main__':

        # Connect to the MySQL database
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

        cursor = db.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM states WHERE name =%s;", (sys.argv[4],))

        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close to connexion
        cursor.close()
        db.close()