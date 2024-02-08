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
    # Requête pour calculer la superficie totale des étages
    cursor.execute("SELECT SUM(superficie) AS superficie_totale FROM etage")
    superficie_result = cursor.fetchone()[0]

    # Affichage du résultat
    print(f"La superficie de La Plateforme est de {superficie_result} m2")

finally:
    # Fermeture du curseur et de la connexion
    cursor.close()
    conn.close()
