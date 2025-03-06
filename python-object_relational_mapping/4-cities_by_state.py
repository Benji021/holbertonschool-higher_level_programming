#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa,
along with their corresponding states, sorted by cities.id.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Main entry point of the script. This section will run only
    if the script is executed directly (not imported as a module).
    """
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """
    Connect to the MySQL server running on localhost at port 3306
    using the provided username, password, and database name.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    """
    Create a cursor object to execute SQL queries.
    Using a single execute() call to retrieve all cities and their
    corresponding states sorted by cities.id.
    """
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    """
    Fetch all results from the executed query and display each
    city's id, name, and the name of its state.
    """
    results = cursor.fetchall()
    for row in results:
        print(row)

    """
    Close the cursor and the database connection to free up resources.
    """
    cursor.close()
    db.close()