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
    # Requête pour calculer la capacité totale des salles
    cursor.execute("SELECT SUM(capacite) AS capacite_totale FROM salle")
    capacite_result = cursor.fetchone()[0]

    # Affichage du résultat en console
    print(f"La capacité totale des salles est de {capacite_result}")

finally:
    # Fermeture du curseur et de la connexion
    cursor.close()
    conn.close()
