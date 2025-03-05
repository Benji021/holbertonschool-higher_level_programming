import MySQLdb

# MySQL database connection
conn = MySQLdb.connect(
    host="localhost",
    user="root",  # Replace with your admin user if necessary
    passwd="password",  # Enter your password
    database="mysql"  # The database where privileges are stored
)

cursor = conn.cursor()

# Exécuter les commandes
users = ["user_0d_1", "user_0d_2"]
for user in users:
    cursor.execute(f"SHOW GRANTS FOR '{user}'@'localhost';")
    grants = cursor.fetchall()
    
    print(f"Privilèges pour {user}:")
    for grant in grants:
        print(grant[0])

cursor.close()
conn.close()
