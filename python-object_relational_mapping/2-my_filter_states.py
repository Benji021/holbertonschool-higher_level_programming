#!/usr/bin/python3
""" List all states with a name starting with N from the hbtn_0e_0_usa """

import pymysql
import sys


if __name__ == "__main__":

    # Get arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = pymysql.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    cursor = db.cursor()

    # Create the SQL query using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
