import os
import json
import csv
import random
from datetime import datetime

CSV_FOLDER = "csv_output"
ESTADO_FOLDER = "estado"

os.makedirs(CSV_FOLDER, exist_ok=True)
os.makedirs(ESTADO_FOLDER, exist_ok=True)

def path_estado(ciudad):
    return os.path.join(ESTADO_FOLDER, f"estado_{ciudad.lower()}.json")

def cargar_estado(ciudad):
    ruta = path_estado(ciudad)
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data.get("emails", [])), set(data.get("urls", []))
    return set(), set()

def guardar_estado(ciudad, emails, urls):
    ruta = path_estado(ciudad)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump({"emails": list(emails), "urls": list(urls)}, f, indent=2)

def abrir_csv(ciudad):
    nombre = f"{ciudad}_{datetime.now():%Y%m%d_%H%M}_{random.randint(100,999)}.csv"
    ruta = os.path.join(CSV_FOLDER, nombre)
    f = open(ruta, "w", newline="", encoding="utf-8")
    writer = csv.writer(f)
    writer.writerow(["Email", "Organización", "Fuente", "Ciudad"])
    return f, writer

# ----------------------------------------
# NUEVAS FUNCIONES PARA CONTROLAR PROMPTS
# ----------------------------------------

def path_estado_prompt(ciudad):
    return os.path.join(ESTADO_FOLDER, f"estado_prompt_{ciudad.lower()}.json")

def cargar_prompt_actual(ciudad):
    ruta = path_estado_prompt(ciudad)
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("indice", -1)  # -1 para empezar en 0 la primera vez
    return -1

def guardar_prompt_actual(ciudad, indice):
    ruta = path_estado_prompt(ciudad)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump({"indice": indice}, f, indent=2)
