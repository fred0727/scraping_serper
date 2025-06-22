import time
import random
from config import CIUDADES, PROMPTS_ROTATIVOS, LIMITE_POR_CIUDAD
from serper_api import buscar_links_serper
from scraper import extraer_emails_desde_url
from utils import cargar_estado, guardar_estado, abrir_csv, cargar_prompt_actual, guardar_prompt_actual
from db import insertar_scraping

def obtener_siguiente_prompt(ciudad):
    total_prompts = len(PROMPTS_ROTATIVOS)
    if total_prompts == 0:
        return None
    indice_actual = cargar_prompt_actual(ciudad)
    indice_siguiente = (indice_actual + 1) % total_prompts
    guardar_prompt_actual(ciudad, indice_siguiente)
    return PROMPTS_ROTATIVOS[indice_siguiente].format(ciudad)

def ejecutar_ciudad(ciudad):
    print(f"\n🌍 Iniciando: {ciudad}")
    prompt = obtener_siguiente_prompt(ciudad)
    if not prompt:
        print(f"[❌] No hay prompts definidos")
        return

    print(f"[🎯] Usando prompt: {prompt}")

    vistos_emails, vistos_urls = cargar_estado(ciudad)
    nuevos = []
    f, writer = abrir_csv(ciudad)

    for url in buscar_links_serper(prompt):
        if url in vistos_urls or url.endswith((".pdf", ".doc", ".xls")):
            continue
        vistos_urls.add(url)
        if "facebook.com" in url:
            continue

        for email, nombre_org in extraer_emails_desde_url(url):
            email_l = email.lower()
            if email_l not in vistos_emails:
                vistos_emails.add(email_l)
                fila = [email_l, nombre_org, url, ciudad]
                nuevos.append(fila)
                writer.writerow(fila)
                insertar_scraping(email_l, nombre_org, url, ciudad)
                f.flush()
                print(f"✔️ {email_l} ({ciudad})")
            if len(nuevos) >= LIMITE_POR_CIUDAD:
                break
        if len(nuevos) >= LIMITE_POR_CIUDAD:
            break
        time.sleep(random.uniform(1.5, 3.5))

    f.close()
    if nuevos:
        guardar_estado(ciudad, vistos_emails, vistos_urls)
        print(f"[✅] CSV finalizado para {ciudad} ({len(nuevos)} nuevos)")
    else:
        print(f"[ℹ️] No se encontraron nuevos en {ciudad}")

if __name__ == "__main__":
    for ciudad in CIUDADES:
        ejecutar_ciudad(ciudad)
