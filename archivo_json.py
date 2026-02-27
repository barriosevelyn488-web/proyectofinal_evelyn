import json

def cargar_coleccion():
    try:
        with open("coleccion.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"libros": [], "peliculas": [], "musica": []}

def guardar_coleccion(coleccion):
    with open("coleccion.json", "w", encoding="utf-8") as archivo:
        json.dump(coleccion, archivo, indent=4, ensure_ascii=False)

# --- CORRECCIÓN AQUÍ ---
def cargar_reporte():
    try:
        # Debe leer reporte.json, no coleccion.json
        with open("reporte.json", "r", encoding="utf-8") as nuevoarchivo:
            return json.load(nuevoarchivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # El reporte suele ser un diccionario simple de géneros
        return {} 

def guardar_reporte(datos_reporte):
    # Debe escribir en reporte.json
    with open("reporte.json", "w", encoding="utf-8") as nuevoarchivo:
        json.dump(datos_reporte, nuevoarchivo, indent=4, ensure_ascii=False) #jdhjajdhsfjk