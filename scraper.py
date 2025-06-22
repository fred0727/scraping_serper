import re
import time
import random
import requests
import urllib3
from bs4 import BeautifulSoup, FeatureNotFound
from config import USER_AGENTS

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "es-ES,es;q=0.9",
        "Referer": "https://www.google.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

def es_email_valido(email):
    tlds_validos = {
        "com", "org", "net", "edu", "gov", "co", "es", "info", "pe", "au", "nz",
        "int", "mil", "biz", "tv", "us", "uk", "ca", "eu", "ar", "mx", "cl", "br"
    }
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        dominio = email.split(".")[-1].lower()
        return dominio in tlds_validos
    return False

def extraer_emails_desde_url(url, retries=3):
    for intento in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=10, headers=get_headers(), verify=False)

            if r.status_code == 403:
                raise Exception("Acceso prohibido (403)")

            if r.status_code != 200:
                raise Exception(f"HTTP {r.status_code}")

            content_type = r.headers.get("Content-Type", "").lower()
            if "text/html" not in content_type:
                raise Exception(f"Tipo de contenido no soportado: {content_type}")

            try:
                soup = BeautifulSoup(r.text, "lxml")
            except FeatureNotFound:
                soup = BeautifulSoup(r.text, "html.parser")

            text = soup.get_text(separator=" ", strip=True)
            titulo = soup.title.string.strip() if soup.title and soup.title.string else "Desconocido"

            correos = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
            return [(email, titulo) for email in filter(es_email_valido, correos)]

        except requests.exceptions.RequestException as e:
            print(f"[⚠️] Error en intento {intento} en {url}: {e}")
            time.sleep(2 ** intento + random.uniform(0.5, 1.5))  # backoff exponencial
        except Exception as e:
            print(f"[⚠️] Error en intento {intento} en {url}: {e}")
            time.sleep(2 ** intento + random.uniform(0.5, 1.5))

    return []
