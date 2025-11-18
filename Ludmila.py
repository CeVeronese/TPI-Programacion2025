opcion = -1  
while opcion != 0:
    print("="*18)
    print("Bienvenido a Qué Bondi")
    print("="*18)
    print("")
    print("0. Salir del programa")
    print("1. Viajar Hasta la UTN")
    print("")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        print("\n¿Como desea iniciar la busqueda?")
        print("1. Por número de línea")
        print("2. Nombre de calle")
        subopcion = int(input("Elige una subopción (1 o 2): "))
        
        if subopcion == 1:
            print("\n📍 Líneas disponibles:")
            print("16")
            print("16-B")
            hora_llegada = input("Ingrese la hora llegada (HH:MM): ")
            linea = input("Ingrese el número de línea que desea consultar: ")
            print(f"🔎 Consultando información para la línea {linea}...\n")
        
        elif subopcion == 2:
            origen = input("Ingrese el punto de origen: ")
            hora_llegada = input("Ingrese la hora llegada (HH:MM): ")