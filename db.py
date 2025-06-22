import mysql.connector
from mysql.connector import Error
import os

DB_CONFIG = {
    'host': os.environ["DB_HOST"],
    'database': os.environ["DB_NAME"],
    'user': os.environ["DB_USER"],
    'password': os.environ["DB_PASS"],
    'port': int(os.environ.get("DB_PORT", 3306)),
}

def insertar_scraping(email, organizacion, url, ciudad):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql = """
        INSERT INTO scraping (email, organizacion, url, ciudad,fecha)
        VALUES (%s, %s, %s, %s, NOW())
        ON DUPLICATE KEY UPDATE email=email;
        """

        cursor.execute(sql, (email, organizacion, url, ciudad))
        conn.commit()

        cursor.close()
        conn.close()
    except Error as e:
        print(f"[❌] Error guardando en DB: {e}")
