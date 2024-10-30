#!/usr/bin/python3


import MySQLdb
import sys

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        return

    # Assign the arguments to variables
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object
        cursor = db.cursor()

        # Define the query using a parameterized statement to prevent SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        
        # Execute the query with the state_name as a parameter
        cursor.execute(query, (state_name,))

        # Fetch all the results
        rows = cursor.fetchall()

        # Print each row in the required format
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: e")
    
    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    main()
