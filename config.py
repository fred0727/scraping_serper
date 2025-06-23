from datetime import datetime
import os

# API_KEY = "d610c594d99e9914f73ea072d3904a8758f107cb"
API_KEY = os.getenv("SERPER_API_KEY")

CIUDADES = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"]

# Lista base unificada con marcador {ciudad} para insertar la ciudad dinámica
PROMPTS_ROTATIVOS = [
    "taller de música en español {} site:.org OR site:.edu",
    "workshop música en español {} 2025",
    "taller de improvisación musical en español {}",
    "taller de canto en español {} comunidad hispana",
    "talleres latinos de música en español en {} Australia 2025",
    "clases de español con música para niños en {}",
    "enseñar español a través de la música en {} comunidad latina",
    "clases de español integrando música latinoamericana en {}",
    "centro cultural hispano en {} talleres musicales mayo junio 2025",
    "centro comunitario latino en {} actividades familiares recientes",
    "asociaciones culturales latinas en {} actividades infantiles",
    "centro de apoyo hispano en {} con talleres musicales recientes",
    "colectivo hispano en {} talleres de música comunitaria",
    "grupo de integración cultural usando música latina en {}",
    "actividades para familias hispanohablantes con niños en {} junio 2025",
    "eventos para familias latinas con niños en {} mayo junio 2025",
    "programas recreativos en español para niños en {}",
    "educación comunitaria en español para familias migrantes en {}",
    "actividades para familias migrantes hispanas en {} 2025",
    "taller de arte o música para niños hispanohablantes en {}",
    "clases de español para niños con canciones en {}",
    "apoyo a familias migrantes hispanas con hijos en {}",
    "enseñanza del español con percusión o piano en {}",
    "español para niños con canciones en {} comunidad hispana",
    "academias de español con actividades musicales en {}",
    "escuelas hispanohablantes en {} que usan música para enseñar español",
    "método musical para enseñar español en {} academias culturales",
    "eventos culturales hispanos en {} Australia 2025",
    "organizaciones latinas en {} que participaron en festivales culturales 2025",
    "festival cultural latino en {} con talleres musicales en español",
    "eventos recientes en {} con colectivos hispanohablantes y música en vivo",
    "danza y percusión en vivo en eventos latinos en {} junio 2025",
    "festival latinoamericano en {} con canto, percusión o piano",
    "taller de integración social con música en español en {}",
    "programas de cohesión social con música en {} para latinos",
    "actividades comunitarias con canto y percusión en {} comunidad hispana",
    "programas de integración para nuevos migrantes hispanos en {} con música",
    "percusión colectiva como herramienta de integración en {} comunidad latina",
    "eventos para integración de hispanohablantes con música en {}",
    "música colaborativa como puente cultural en {} comunidad latina",
    "Spanish music workshop {} site:eventbrite.com",
    "Latin family programs {} site:eventbrite.com",
    "Spanish through music {} site:eventbrite.com",
    "Learn Spanish with music {} Australia"
]

LIMITE_POR_CIUDAD = 200

HEADERS = {
    'X-API-KEY': API_KEY,
    'Content-Type': 'application/json'
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36"
]
