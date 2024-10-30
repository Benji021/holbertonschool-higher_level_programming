#!/usr/bin/python3
""" List all states with a name starting with N from the hbtn_0e_0_usa """


import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(f"Error {e}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
