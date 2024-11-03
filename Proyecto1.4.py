# Lista principal para almacenar los activos como sublistas
activos = []

# Bucle principal para el menú interactivo
while True:
    # Mostrar el menú de opciones
    print("\nMenú de Gestión de Activos")
    print("1. Agregar activo")
    print("2. Consultar activo")
    print("3. Modificar activo")
    print("4. Eliminar activo")
    print("5. Listado completo de activos")
    print("6. Salir")
    
    # Solicitar al usuario una opción del menú
    opcion = input("Seleccione una opción: ").strip()
    
    # Opción 1: Agregar activo
    if opcion == '1':
        # Solicitar los datos del nuevo activo
        equipo = input("Equipo: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        num_serie = input("Número de serie: ")
        estado = input("Estado: ")
        bodega = input("Bodega: ")
        
        # Crear una lista para el nuevo activo y agregarla a la lista principal
        activo = [equipo, marca, modelo, num_serie, estado, bodega]
        activos.append(activo)
        
        # Confirmar que el activo fue agregado
        print("Activo agregado con éxito.")
    
    # Opción 2: Consultar activo
    elif opcion == '2':
        # Solicitar el número de serie del activo a consultar
        num_serie_buscar = input("Ingrese el número de serie del activo: ")
        encontrado = False  # Variable para verificar si se encuentra el activo
        
        # Buscar el activo en la lista por el número de serie
        for activo in activos:
            if activo[3] == num_serie_buscar:
                # Mostrar los detalles del activo si se encuentra
                print(f"\nEquipo: {activo[0]}")
                print(f"Marca: {activo[1]}")
                print(f"Modelo: {activo[2]}")
                print(f"Número de serie: {activo[3]}")
                print(f"Estado: {activo[4]}")
                print(f"Bodega: {activo[5]}")
                encontrado = True
                break  # Detener la búsqueda si se encuentra el activo
        
        # Mensaje si no se encuentra el activo
        if not encontrado:
            print("Activo no encontrado.")
    
    # Opción 3: Modificar activo
    elif opcion == '3':
        # Solicitar el número de serie del activo a modificar
        num_serie_modificar = input("Ingrese el número de serie del activo a modificar: ")
        encontrado = False  # Variable para verificar si se encuentra el activo
        
        # Buscar el activo en la lista para modificarlo
        for activo in activos:
            if activo[3] == num_serie_modificar:
                # Solicitar nuevos datos (presionar Enter para dejar sin cambios)
                print("\nIngrese los nuevos datos del activo (presione Enter para dejar sin cambios):")
                nuevo_equipo = input(f"Equipo ({activo[0]}): ") or activo[0]
                nueva_marca = input(f"Marca ({activo[1]}): ") or activo[1]
                nuevo_modelo = input(f"Modelo ({activo[2]}): ") or activo[2]
                nuevo_estado = input(f"Estado ({activo[4]}): ") or activo[4]
                nueva_bodega = input(f"Bodega ({activo[5]}): ") or activo[5]
                
                # Actualizar los datos del activo
                activo[0] = nuevo_equipo
                activo[1] = nueva_marca
                activo[2] = nuevo_modelo
                activo[4] = nuevo_estado
                activo[5] = nueva_bodega
                
                print("Activo modificado con éxito.")
                encontrado = True
                break  # Detener la búsqueda si se encuentra y modifica el activo
        
        # Mensaje si no se encuentra el activo
        if not encontrado:
            print("Activo no encontrado.")
    
    # Opción 4: Eliminar activo
    elif opcion == '4':
        # Solicitar el número de serie del activo a eliminar
        num_serie_eliminar = input("Ingrese el número de serie del activo a eliminar: ")
        encontrado = False  # Variable para verificar si se encuentra el activo
        
        # Buscar el activo en la lista y eliminarlo
        for i, activo in enumerate(activos):
            if activo[3] == num_serie_eliminar:
                activos.pop(i)  # Eliminar el activo de la lista
                print("Activo eliminado con éxito.")
                encontrado = True
                break  # Detener la búsqueda si se encuentra y elimina el activo
        
        # Mensaje si no se encuentra el activo
        if not encontrado:
            print("Activo no encontrado.")
    
    # Opción 5: Listado completo de activos
    elif opcion == '5':
        # Verificar si hay activos en la lista
        if len(activos) == 0:
            print("No hay activos registrados.")
        else:
            # Mostrar todos los activos registrados
            print("\nListado completo de activos:")
            for activo in activos:
                print(f"\nEquipo: {activo[0]}")
                print(f"Marca: {activo[1]}")
                print(f"Modelo: {activo[2]}")
                print(f"Número de serie: {activo[3]}")
                print(f"Estado: {activo[4]}")
                print(f"Bodega: {activo[5]}")
    
    # Opción 6: Salir del programa
    elif opcion == '6':
        print("Saliendo del programa...")
        break  # Terminar el bucle y salir del programa
    
    # Mensaje para opciones inválidas
    else:
        print("Opción no válida. Intente de nuevo.")
