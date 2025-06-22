from db import DB_CONFIG
import mysql.connector
from mysql.connector import Error

def cargar_estado(ciudad):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("SELECT email FROM estado_scraping WHERE ciudad = %s", (ciudad,))
        emails = set(row[0] for row in cursor.fetchall())

        cursor.execute("SELECT url FROM estado_scraping WHERE ciudad = %s", (ciudad,))
        urls = set(row[0] for row in cursor.fetchall())

        cursor.close()
        conn.close()
        return emails, urls

    except Error as e:
        print(f"[❌] Error cargando estado: {e}")
        return set(), set()

def guardar_estado(ciudad, emails, urls):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        for email in emails:
            cursor.execute("""
                INSERT IGNORE INTO estado_scraping (ciudad, email, url)
                VALUES (%s, %s, '')
            """, (ciudad, email))

        for url in urls:
            cursor.execute("""
                INSERT IGNORE INTO estado_scraping (ciudad, email, url)
                VALUES (%s, '', %s)
            """, (ciudad, url))

        conn.commit()
        cursor.close()
        conn.close()

    except Error as e:
        print(f"[❌] Error guardando estado: {e}")

def cargar_prompt_actual(ciudad):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT indice_prompt_actual FROM estado_prompt WHERE ciudad = %s", (ciudad,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row[0] if row else -1
    except Error as e:
        print(f"[❌] Error cargando prompt actual: {e}")
        return -1

def guardar_prompt_actual(ciudad, indice):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO estado_prompt (ciudad, indice_prompt_actual)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE indice_prompt_actual = %s
        """, (ciudad, indice, indice))
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(f"[❌] Error guardando prompt actual: {e}")
