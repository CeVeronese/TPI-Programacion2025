ancho = 50
print(
    "✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n"
    "🚌 Bienvenido a Qué Bondi 🚌\n"
    "✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n"
    "\n"
    "🤔 ¿Qué desea hacer? 🤔\n"
    "\n"
    "0️⃣  Salir del programa\n"
    "1️⃣  Viajar hasta la UTN\n"
    "\n"
)
mostrar_menuPrincipal = True
while mostrar_menuPrincipal == True:
    ancho = 50
    print(
        "✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n"
        "🚌 Bienvenido a Qué Bondi 🚌\n"
        "✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n"
        "\n"
        "🤔 ¿Qué desea hacer? 🤔\n"
        "\n"
        "0️⃣  Salir del programa\n"
        "1️⃣  Viajar hasta la UTN\n"
        "\n"
    )
    try:
        opcion_menu = int(input("👉🏽 Elija una opcion: "))

        match opcion_menu:
            case 0 :
                print()
            case 1:
                mostrar_busqueda = True
                while mostrar_busqueda == True:
                    print("\n¿Como desea iniciar la busqueda?\n"
                    "1. Por número de línea\n"
                    "2. Nombre de calle\n"
                    "3. Volver al menu\n"
                    )
                    print()
                    busqueda = int(input("👉🏽 Elija una opción: "))
                    match busqueda:
                        case 1:
                            print()
                            print("🚌 𝐋𝐢𝐧𝐞𝐚𝐬 𝐃𝐢𝐬𝐩𝐨𝐧𝐢𝐛𝐥𝐞𝐬 🚌 \n🧡 16 / 🩶 16B\n")
                            print()
                            linea = input("👉🏽 Ingrese la linea que desea tomar: ")
                            print()
                            if linea == "16":
                                print(
                                    "🚌🧡 𝐏𝐚𝐫𝐚𝐝𝐚𝐬 𝐝𝐞 𝐥𝐚 𝐋𝐢𝐧𝐞𝐚 𝐂𝟏-𝟏𝟔 🧡🚌\n"
                                    "𝟏. Centro de Transferencias\n"
                                    "𝟐. Av. Irigoyen / San Luis\n"
                                    "𝟑. Bv. Alvear / Prol. Sarmiento\n"
                                    "𝟒. Prol. Sarmiento / Av. Universidad\n"
                                    "𝟓. Lacar / Aconcagua\n"
                                    "𝟔. M.M. Moreno / Prol. Sarmiento\n"
                                    "𝟕. Bv. Alvear / San Luis\n"
                                    "𝟖. Lisandro de la Torre / Bs. As.\n"
                                )
                                parada_user = int(input("📍 Ingrese la parada de colectivo más cercana: "))
                                if parada_user < 1 or parada_user > 8:
                                    print("⚠️  La linea no pasa por la parada ingresada ⚠️")
                                else:
                                    try:
                                        hora_llegada = input("🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                        print()
                                        mostrar_horarios_validos(paradas_16, parada_user, hora_llegada)
                                        print()
                                        salida = input("👉🏽 Ingrese 0 para finalizar ")
                                        print()
                                    except ValueError:
                                        print("🕒❌ La hora ingresada no es válida ❌🕒")    
                            elif linea == "16B":
                                    print(
                                        "🚌🩶 𝐏𝐚𝐫𝐚𝐝𝐚𝐬 𝐝𝐞 𝐥𝐚 𝐋𝐢𝐧𝐞𝐚 𝐆𝟏-𝟏𝟔𝐁 🩶🚌\n"
                                        "𝟏. Centro de Transferencias\n"
                                        "𝟐. Bv Italia / Jujuy\n"
                                        "𝟑. Gruta\n"
                                        "𝟒. Terminal de Omnibús\n"
                                        "𝟓. Bv Alvear / Mendoza\n"
                                        "𝟔. Bv España / La Rioja\n"
                                        "𝟕. Jauretche / Bv España (UNVM)\n"
                                        "𝟖. Rawson / Bv España\n"
                                    )
                                    print()
                                    parada_user = int(input("📍 Ingrese la parada de colectivo más cercana: "))
                                        
                                    if parada_user < 1 or parada_user > 8:
                                        print("⚠️  La linea no pasa por la parada ingresada ⚠️")
                                        print()
                                    else:
                                        try:
                                            hora_llegada = input("🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                            print()
                                            mostrar_horarios_validos(paradas_16B, parada_user, hora_llegada)
                                            print()
                                            salida = input("👉🏽 Ingrese 0 para finalizar ")
                                            print()
                                        except ValueError:
                                            print("🕒❌ La hora ingresada no es válida ❌🕒")
                                
                            break
