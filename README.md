# 🕸️ Scraper Cultural Hispano

Este proyecto realiza scraping automatizado utilizando la API de Serper (Google Search) para encontrar páginas web con correos electrónicos de organizaciones culturales hispanohablantes en distintas ciudades. Los resultados se almacenan tanto en archivos CSV como en una base de datos MySQL.

---

## ⚙️ Tecnologías utilizadas

- Python 3.8+
- Serper API (https://serper.dev)
- MySQL (remoto o local)
- BeautifulSoup4 + requests
- Conexión MySQL con `mysql-connector-python`

---

## 📁 Estructura del proyecto

```bash
scraper/
├── main.py                  # Script principal
├── config.py                # Parámetros de configuración (ciudades, prompts)
├── serper_api.py           # Módulo de consulta Serper
├── scraper.py              # Extracción de emails desde URL
├── utils.py                # Funciones de estado y CSV
├── db.py                   # (opcional) Guardado en base de datos
├── requirements.txt        # Dependencias del proyecto
└── csv_output/             # Carpeta donde se guardan los CSV generados
└── estado/                 # Carpeta donde se guardan los estados de los prompts y asi rotar cada vez que se ejecute
