#!/usr/bin/python3
""" List all states with a name starting with N from the hbtn_0e_0_usa """


import sys
import MySQLdb


def main():
    # Checking arguments
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name>")
        return
    
    # Retrieving arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]


    try:
        # Database connexion
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
            passwd=mysql_password, db=database_name)

        #cursor creation
        cursor = db.cursor()

        #Execute SQL query to retrieve reports sorted by id
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

        # Retrieving and displaying results
        states = cursor.fetchall()
        for state in states:
            print(state)
    
    except MySQLdb.Error as e:
        print(f"Error {e}")

    finally:
        # Close to connexion
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    main()