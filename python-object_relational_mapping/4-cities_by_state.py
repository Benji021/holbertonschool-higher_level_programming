#!/usr/bin/python3
"List all cities from database hbtn_0e_4_usa"

import sys
import MySQLdb

def main():
    # Checking arguments
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Retrieving arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Database connexion
        db = MySQLdb.connect(host="localhost", user=mysql_username, passwd=mysql_password, db=database_name, port=3306)

        # Cursor creation
        cursor = db.cursor()

        # Execute SQL query to retrieve reports sorted by id
        cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)

        # Retrieving and displaying results
        results = cursor.fetchall()
        for city in results:
            print(f"{city[0]}: {city[1]} ({city[2]})")

    except MySQLdb.Error as e:
        print(f"Error: Unable to connect to the database or execute query. Details: {e}")

    finally:
        # Close to connexion
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    main()
