import json

def cargar_coleccion():
    try:
        with open("coleccion.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"libros": [], "peliculas": [], "musica": []}

def guardar_coleccion(coleccion):
    with open("coleccion.json", "w", encoding="utf-8") as archivo:
        json.dump(coleccion, archivo, indent=4, ensure_ascii=False) #jas