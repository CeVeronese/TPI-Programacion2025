mostrar_menuPrincipal = True
while mostrar_menuPrincipal == True:
    print("="*22)
    print("Bienvenido a Qué Bondi")
    print("="*22)
    print("\n¿Que desea hacer?")
    print("\n0. Salir del programa")
    print("1. Viajar Hasta la UTN")
    print()
    try:
        opcion_menu = int(input("Elija una opcion: "))
        if opcion_menu != 0 and opcion_menu != 1:
            print("\nLa entrada no es valida. intentelo nuevamente")
            print()
            continue
            
    except ValueError:
        print("\nLa entrada no es valida. intentelo nuevamente")
        print()
        continue
        
    if opcion_menu == 0:
        mostrar_menuPrincipal = False
        print("\nFinalizando el programa...")
        break
        
    mostrar_busqueda = True
    while mostrar_busqueda == True:
        if opcion_menu == 1:
            print("\n¿Como desea iniciar la busqueda?")
            print("\n1. Por número de línea")
            print("2. Nombre de calle")
            print("3. Volver al menu")
            print()
            busqueda = int(input("Elija una opción: "))
            if busqueda == 3:
                mostrar_busqueda = False
                break