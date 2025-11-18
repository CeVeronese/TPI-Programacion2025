opcion = -1  
while opcion != 0:
    print("="*18)
    print("Bienvenido a Qué Bondi")
    print("¿Como desea iniciar la busqueda?")
    print("="*18)
    print("")
    print("Las opciones a elegir son:")
    print("0. Salir del programa")
    print("1. Inicio de búsqueda")
    print("")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        print("\n--- Consultas ---")
        print("1. Número de línea")
        print("2. Agregar ubicación")
        subopcion = int(input("Elige una subopción (1 o 2): "))
        
        if subopcion == 1:
            print("\n📍 Líneas disponibles:")
            print("16")
            print("16-B")
            linea = input("Ingrese el número de línea que desea consultar: ")
            print(f"🔎 Consultando información para la línea {linea}...\n")
        
        elif subopcion == 2:
            print("\n🗺️ Agregar ubicación")
            origen = input("Ingrese el punto de origen: ")
            destino = input("Ingrese el destino: ")
            linea = input("Ingrese el número de colectivo (16 o 16B): ")
            parada = int(input("Ingrese el número de parada (1 a 8): "))
            hora_llegada = input("Ingrese la hora llegada (HH:MM): ")