#!/usr/bin/python3
"""SQL Injection..."""


import sys
import MySQLdb

if __name__ == '__main__':

    # Check the number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

        cursor = db.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM states WHERE name =%s;", (sys.argv[4],))

        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
