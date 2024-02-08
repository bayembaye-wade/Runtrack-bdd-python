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
    # Récupération des noms et des capacités des salles
    cursor.execute("SELECT nom, capacite FROM salle")

    # Affichage des résultats en console
    for salle in cursor.fetchall():
        nom, capacite = salle
        print(f"Nom de la salle : {nom}, Capacité : {capacite}")

finally:
    # Fermeture du curseur et de la connexion
    cursor.close()
    conn.close()
