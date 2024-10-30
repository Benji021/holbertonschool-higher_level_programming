#!/usr/bin/python3
""" lists all cities of that state"""

import sys
import MySQLdb

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                            db=sys.argv[3], port=3306)

        cur = db.cursor()

        query = """
            SELECT cities.id, cities.name, states.name
            FROM cities JOIN states ON cities.state_id = states.id
            WHERE states.name = %s;
        """
        cur.execute(query, (sys.argv[4],))

        states = cur.fetchall()

        if states:
            print(", ".join([state[1] for state in states]))
        else:
            print("No cities found for the specified state.")

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cur.close()
        db.close()
