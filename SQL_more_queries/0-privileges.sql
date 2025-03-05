import mysql

# Connection configuration
HOST = "localhost"
USER = "root"  # Replace with a user with the necessary rights
PASSWORD = "votre_mot_de_passe"
DATABASE = "mysql"

try:
    # Connexion à la base MySQL
    conn = mysql.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    cursor = conn.cursor()
    
    # Liste des utilisateurs à vérifier
    users = ["user_0d_1", "user_0d_2"]
    
    for user in users:
        cursor.execute(f"SHOW GRANTS FOR '{user}'@'localhost';")
        grants = cursor.fetchall()
        print(f"Privilèges de {user}:")
        for grant in grants:
            print(grant[0])
        print("-" * 50)
    
    # Connexion closed
    cursor.close()
    conn.close()
except mysql.connector.Error as e:
    print(f"Erreur MySQL: {e}")
