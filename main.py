from archivo_json import cargar_coleccion, guardar_coleccion 
# Quitamos la carga de reporte aquí porque el reporte se genera desde gestion_coleccion
import gestion_coleccion as gestor 

def main():
    coleccion = cargar_coleccion() 
    
    while True: 
        print("\n===========================================")
        print("        Administrador de Colección")
        print("===========================================")
        print("1. Añadir un Nuevo Elemento")
        print("2. Ver Todos los Elementos")
        print("3. Buscar un Elemento")
        print("4. Editar un Elemento")
        print("5. Eliminar un Elemento")
        print("6. Ver Elementos por Categoría")
        print("7. Generar Reporte de Géneros (Total)") # Nombre más claro
        print("8. Guardar y Cargar Datos")
        print("9. Salir")
        print("===========================================")
        
        opcion = input("Selecciona una opción (1-9): ")

        if opcion == "1":
            print("\n¿Qué categoría?\n1. Libros | 2. Películas | 3. Música")
            sub = input("Selección: ")
            cats = {"1": "libros", "2": "peliculas", "3": "musica"}
            if sub in cats: 
                gestor.añadir_elemento(coleccion, cats[sub])
        
        elif opcion == "2":
            gestor.ver_todo(coleccion)

        elif opcion == "3":
            print("\nBuscar por: 1. Título | 2. Autor | 3. Género")
            sub = input("Opción: ")
            campos = {"1": "titulo", "2": "autor", "3": "genero"}
            if sub in campos: 
                gestor.buscar_universal(coleccion, campos[sub])

        elif opcion == "4":
            print("\nCategoría: 1. Libros | 2. Películas | 3. Música")
            cat_op = input("Selección: ")
            cats = {"1": "libros", "2": "peliculas", "3": "musica"}
            if cat_op in cats:
                print("\nCampo: 1. Título | 2. Autor | 3. Género | 4. Valoración")
                campo_op = input("Selección: ")
                campos = {"1": "titulo", "2": "autor", "3": "genero", "4": "valoracion"}
                if campo_op in campos:
                    gestor.editar_elemento(coleccion, cats[cat_op], campos[campo_op])

        elif opcion == "5":
            print("\nEliminar de: 1. Libros | 2. Películas | 3. Música")
            sub = input("Selección: ")
            cats = {"1": "libros", "2": "peliculas", "3": "musica"}
            if sub in cats: 
                gestor.eliminar_elemento(coleccion, cats[sub])

        elif opcion == "6":
            print("\n¿Qué categoría desea inspeccionar?")
            print("1. Libros\n2. Películas\n3. Música\n4. Regresar")
            sub = input("Selección: ")
            cats = {"1": "libros", "2": "peliculas", "3": "musica"}
            if sub in cats:
                gestor.ver_por_categoria(coleccion, cats[sub])

        # --- CORRECCIÓN CLAVE: Opción 7 ---
        elif opcion == "7": # Debe llevar COMILLAS porque input() devuelve texto
            # Llamamos a la función que recorre TODO y guarda el reporte
            gestor.reporte_por_genero(coleccion)
        
        elif opcion == "8":
            print("\n1. Guardar | 2. Recargar")
            sel = input("Selección: ")
            if sel == "1":
                guardar_coleccion(coleccion)
                print("¡Disco actualizado!")
            else:
                coleccion = cargar_coleccion()
                print("¡Memoria recargada!")

        elif opcion == "9":
            print("Saliendo del Administrador de Colección...")#jadhfjajkdhn
        
            break

if __name__ == "__main__":
    main()