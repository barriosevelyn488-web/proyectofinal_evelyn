from archivo_json import guardar_coleccion, guardar_reporte

def añadir_elemento(coleccion, categoria):
    print(f"\n--- Agregando a {categoria.upper()} ---") 
    
    t = input("Título: ").strip()
    a = input("Autor/Artista: ").strip()
    g = input("Género: ").strip()
    v = input("Valoración: ").strip()

    # Verificación de duplicados por título
    for e in coleccion[categoria]:
        if e['titulo'].lower() == t.lower():
            print(f"\n¡ERROR! El título '{t}' ya existe en {categoria}.")
            return 

    nuevo = {
        "titulo": t,
        "autor": a,
        "genero": g,
        "valoracion": v
    }
    
    coleccion[categoria].append(nuevo) 
    guardar_coleccion(coleccion) 
    print("¡Guardado exitosamente!")

def ver_todo(coleccion):
    print("\n" + "="*45) 
    print("        VISTA GENERAL DE LA COLECCIÓN")
    print("="*45) 
    for cat, lista in coleccion.items(): 
        print(f"\n>>> {cat.upper()} ({len(lista)} elementos)") 
        for e in lista: 
              print(f" - {e['titulo']} ({e['genero']})") 

def ver_por_categoria(coleccion, categoria):
    print(f"\n===========================================")
    print(f"    LISTADO DETALLADO DE: {categoria.upper()}")
    print("===========================================")
    
    lista = coleccion.get(categoria, [])
    if not lista:
        print(f"La sección de {categoria} está vacía.")
    else:
        for i, elemento in enumerate(lista, 1):
            print(f"{i}. TÍTULO:    {elemento['titulo']}")
            print(f"   AUTOR:     {elemento['autor']}")
            print(f"   GÉNERO:    {elemento['genero']}")
            print(f"   VALORACIÓN: {elemento['valoracion']}")
            print("-" * 30)

def buscar_universal(coleccion, campo):
    valor = input(f"\nBuscar {campo}: ").lower().strip()
    encontrado = False
    for cat, lista in coleccion.items():
        for e in lista:
            if valor in e[campo].lower():
                print(f"[{cat.upper()}] {e['titulo']} - {e['autor']}")
                encontrado = True
    if not encontrado: print("No hay coincidencias.")

def editar_elemento(coleccion, categoria, campo):
    lista = coleccion[categoria]
    if not lista: return print("\nCategoría vacía.")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item['titulo']}")
    try:
        idx = int(input("\nSeleccione el número a editar: ")) - 1
        if 0 <= idx < len(lista):
            lista[idx][campo] = input(f"Nuevo {campo}: ").strip()
            guardar_coleccion(coleccion)
            print("¡Actualizado!")
    except: print("Error en el ingreso.")

def eliminar_elemento(coleccion, categoria):
    lista = coleccion[categoria]
    if not lista: return
    for i, item in enumerate(lista, 1): print(f"{i}. {item['titulo']}")
    try:
        idx = int(input("\nNúmero a eliminar: ")) - 1
        if 0 <= idx < len(lista):
            coleccion[categoria].pop(idx)
            guardar_coleccion(coleccion)
            print("Eliminado.")
    except: print("Error.")

# --- FUNCIÓN 7: REPORTE POR GÉNERO (REQUISITO EXAMEN) ---
def reporte_por_genero(coleccion):
    print("\n===========================================")
    print("      REPORTE DE TOTALES POR GÉNERO")
    print("===========================================")
    
    # Diccionario de frecuencias: {"Género": cantidad}
    conteo_generos = {}

    # 1. Recorrer toda la colección (todas las categorías)
    for categoria, lista in coleccion.items():
        # 2. Recorrer cada elemento de la lista actual
        for elemento in lista:
            # Normalizamos el texto (sin espacios, primera letra mayúscula)
            gen = elemento['genero'].strip().capitalize()
            # 3. Lógica del contador
            if gen in conteo_generos:
                conteo_generos[gen] += 1
            else:
                conteo_generos[gen] = 1

    # 4. Mostrar en pantalla
    if not conteo_generos:
        print("No hay datos suficientes para generar el reporte.")
    else:
        for gen, cantidad in conteo_generos.items():
            print(f"GÉNERO: {gen.ljust(15)} | TOTAL: {cantidad}")
        
        # 5. Guardar en reporte.json usando la función de archivo_json.py
        guardar_reporte(conteo_generos)
        print("\n[OK] Reporte exportado exitosamente a 'reporte.json'") #hasdjjajdjf
