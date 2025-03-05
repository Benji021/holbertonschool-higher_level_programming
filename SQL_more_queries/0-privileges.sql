import mysql.connector

# Configuration de connexion
HOST = "localhost"
USER = "root"  # Remplacez par un utilisateur ayant les droits nécessaires
PASSWORD = "votre_mot_de_passe"

try:
    # Connexion à la base MySQL
    conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
    cursor = conn.cursor()
    
    # Liste des utilisateurs à vérifier
    users = ["user_0d_1", "user_0d_2"]
    
    for user in users:
        cursor.execute(f"SHOW GRANTS FOR '{user}'@'localhost';")
        grants = cursor.fetchall()
        print(f"Privileges of {user}:")
        for grant in grants:
            print(grant[0])
        print("-" * 50)
    
    # Fermeture de la connexion
    cursor.close()
    conn.close()
except mysql.connector.Error as e:
    print(f"MySQL Error: {e}")
