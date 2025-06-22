import http.client
import json
from config import HEADERS

def buscar_links_serper(query):
    try:
        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = json.dumps({
            "q": query,
            "num": 100
        })
        conn.request("POST", "/search", payload, HEADERS)
        res = conn.getresponse()
        datos = json.loads(res.read().decode("utf-8"))

        links = [r.get("link") for r in datos.get("organic", []) if r.get("link")]
        print(f"[🔍] Query '{query}' → {len(links)} resultados")
        return links
    except Exception as e:
        print(f"[❌] Error Serper API: {e}")
        return []
