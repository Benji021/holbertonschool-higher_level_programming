#!/usr/bin/python3
""" List all states with a name starting with N from the hbtn_0e_0_usa """


import sys
import MySQLdb


if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = None
    cursor = None

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
            user=mysql_username, passwd=mysql_password,
            db=database_name)

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
