#!/usr/bin/python3

"""
This script takes in a state name as an argument and lists all cities
of that state from the hbtn_0e_4_usa database, using a parameterized query
to prevent SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Retrieve command-line arguments: username, password, database name, 
    and state name.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    """
    Connect to the MySQL database on localhost at port 3306.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    """
    Create a cursor object to execute SQL queries.
    """
    cursor = db.cursor()

    """
    Execute a parameterized SQL query to retrieve cities from a specific state.
    Using a single execute() call to fetch cities associated with the state.
    The state_id is determined by joining the states and cities tables.
    """
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    """
    Fetch all rows in the result set from the executed query.
    """
    rows = cursor.fetchall()

    """
    Print the names of the cities, joining them with a comma if there are multiple.
    If there are no cities, it will just output an empty line.
    """
    if rows:
        print(", ".join(city[0] for city in rows))
    else:
        print("")  # Print empty line if no cities found

    """
    Close the cursor and the database connection to free up resources.
    """
    cursor.close()
    db.close()