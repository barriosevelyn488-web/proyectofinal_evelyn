from archivo_json import guardar_coleccion

#1
def añadir_elemento(coleccion, categoria): 
    print(f"\n--- Agregando a {categoria.upper()} ---")
    
    t = input ("Titulo").strip()
    a = input("Autor/Artista: ").strip()
    g = input("Género: ").strip()
    v = input("Valoración: ").strip()

    for e in coleccion[categoria]:
        # Si el título es igual Y el autor también es igual...
        if e['titulo'].lower() == t.lower() and e['autor'].lower() == a.lower():
            print(f"\n¡ERROR! Ya existe '{t}' de ese mismo autor.")
            return # Aquí sí es un duplicado real y se detiene
    nuevo = {
        "titulo": t,
        "autor": a,
        "genero": g,
        "valoracion": v
    } 
    coleccion[categoria].append(nuevo)
    guardar_coleccion(coleccion)
    print("¡Guardado exitosamente!")

#2
def ver_todo(coleccion):
    print("\n" + "="*45)
    print("       VISTA GENERAL DE LA COLECCIÓN")
    print("="*45)
    for cat, lista in coleccion.items():
        print(f"\n>>> {cat.upper()}")
        for e in lista:
            print(f" - {e['titulo']}")

#3
def buscar_universal(coleccion, campo):
    valor = input(f"\nBuscar {campo}: ").lower().strip()
    encontrado = False
    for cat, lista in coleccion.items():
        for e in lista:
            if valor in e[campo].lower():
                print(f"[{cat.upper()}] {e['titulo']} - {e['autor']}")
                encontrado = True
    if not encontrado: print("No hay coincidencias.")

#4
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

#5
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

#6
def ver_por_categoria(coleccion, categoria):
    """Esta es la función de la Opción 6"""
    print(f"\n===========================================")
    print(f"    LISTADO DETALLADO DE: {categoria.upper()}")
    print("===========================================")
    
    lista = coleccion.get(categoria, [])
    
    if not lista:
        print(f"La sección de {categoria} está vacía actualmente.")
    else:
        # El ciclo recorre cada diccionario dentro de la lista de la categoría
        for i, elemento in enumerate(lista, 1):
            print(f"{i}. TÍTULO:    {elemento['titulo']}")
            print(f"   AUTOR:     {elemento['autor']}")
            print(f"   GÉNERO:    {elemento['genero']}")
            print(f"   VALORACIÓN: {elemento['valoracion']}")
            print("-" * 30)
            
            
def reporta_porgenero(coleccion,categoria):

    for cate, lista in coleccion.items():
             print(f"\n>>> {cate.upper()} ({len(lista)} elementos)")
             encontrado = True
    if not encontrado: print("No hay coincidencias.")

    for cate, lista in coleccion.items():
       print(f"\n>>> {cate.upper()} ({len(lista)} elementos)")
  #  for e in lista:
         #  print(f" - {e['titulo']}")

