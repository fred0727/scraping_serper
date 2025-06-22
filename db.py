import mysql.connector
from mysql.connector import Error

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'srv1689.hstgr.io',
    'database': 'u603781914_app',
    'user': 'u603781914_admin',
    'password': '@dminDb2024',
    'port': 3306,
    'charset': 'utf8mb4'
}

def insertar_scraping(email, organizacion, url, ciudad):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql = """
        INSERT INTO scraping (email, organizacion, url, ciudad)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE email=email;
        """

        cursor.execute(sql, (email, organizacion, url, ciudad))
        conn.commit()

        cursor.close()
        conn.close()
    except Error as e:
        print(f"[❌] Error guardando en DB: {e}")
