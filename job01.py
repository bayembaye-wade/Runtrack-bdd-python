import mysql.connector

# Paramètres de connexion à la base de données
config = {
    'user': 'root',
    'password': 'Diourbel2002@',
    'host': 'localhost',
    'database': 'LaPlateforme'
}

# Connexion à la base de données
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

try:
    # Récupération de l'ensemble des étudiants
    cursor.execute("SELECT * FROM etudiant")

    # Affichage des résultats en console
    for student in cursor.fetchall():
        print(student)

finally:
    # Fermeture du curseur et de la connexion
    cursor.close()
    conn.close()

