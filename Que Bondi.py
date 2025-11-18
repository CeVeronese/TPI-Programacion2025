import folium
import requests

def mostrar_horarios_validos(paradas_dict, parada_ingresada, hora_llegada):
    horarios_parada = paradas_dict[parada_ingresada]
    horarios_validos = []
    for hora in horarios_parada:
        if hora < hora_llegada:
            horarios_validos.append(hora)
    for hora in horarios_validos:
        print(hora)
def buscarCalles(paradas_calles, calle_usuario):
    encontrados = []
    calle_minuscula = calle_usuario.lower()
    for i in range(len(paradas_calles)):
        parada_minuscula = paradas_calles[i].lower()
        if calle_minuscula in parada_minuscula:
            encontrados.append((i+1, paradas_calles[i]))
    return encontrados
def obtener_ruta_osrm(origen, destino, profile='driving'):
    lon1, lat1 = origen[1], origen[0]
    lon2, lat2 = destino[1], destino[0]
    url = f"http://router.project-osrm.org/route/v1/{profile}/{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson"
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        coords = data["routes"][0]["geometry"]["coordinates"]
        ruta = [[pt[1], pt[0]] for pt in coords]
        return ruta
    except Exception as e:
        return None

coords_paradas_16 = {
    '1': [-32.40922918051604, -63.24704791802116],
    '2': [-32.41556158412005, -63.24016165776168],
    '3': [-32.41475653064061, -63.23318341425801],
    '4': [-32.408472525229534, -63.22228564186324],
    '5': [-32.41344669085965, -63.213247354385636],
    '6': [-32.42020279446054, -63.241487324275184],
    '7': [-32.412995567372135, -63.23467241609939],
    '8': [-32.40981969999223, -63.241289102263075]
}
coords_paradas_16B = {
    '1': [-32.41034738674454, -63.24589656756981], 
    '2': [-32.409576491715356, -63.256501018244826],
    '3': [-32.41925152818723, -63.23966898692198],
    '4': [-32.41423228533785, -63.23310172127251],
    '5': [-32.41108108054281, -63.236555832913446],
    '6': [-32.40449997545647, -63.242501000141296],
    '7': [-32.38430085748814, -63.25985676442258],
    '8': [-32.398204191708956, -63.24765747893508]
}
utn_coords = [-32.409771241180664, -63.21655973021679]

paradas_16 = {
    '1': [
        "06:15", "07:00", "07:45", "08:30", "09:15", "10:15", 
        "11:00", "11:45","12:30", "13:15", "14:00", "14:45", 
        "15:30", "16:15", "17:00", "18:00","18:45", "19:30", 
        "20:15", "21:00"
    ],
    '2': [
        "06:20", "07:05", "07:50", "08:35", "09:20", "10:20", 
        "11:05", "11:50","12:35", "13:20", "14:05", "14:50", 
        "15:35", "16:20", "17:05", "18:05", "18:50", "19:35", 
        "20:20", "21:20"
    ],
    '3': [
        "06:25", "07:10","07:55", "08:40", "09:25", "10:25", 
        "11:10", "11:55", "12:40", "13:25", "14:10", "14:55",
        "15:40", "16:25", "17:10", "18:10", "18:55", "19:40", 
        "20:25", "21:10"
    ],
    '4': [
        "06:30", "07:15", "08:00", "08:45", "09:30", "10:30", 
        "11:15", "12:00", "12:45", "13:30", "14:15", "15:00",
        "15:45", "16:30", "17:15", "18:15", "19:00", "19:45", 
        "20:30", "21:15"
    ],
    '5': [
        "06:40", "07:25", "08:10", "08:55",    "09:40", "10:40", 
        "11:25", "12:10", "12:55", "13:40", "14:25", "15:10",
        "15:55", "16:40", "17:25",    "18:25", "19:10", "19:55", 
        "20:40",    "21:25"
    ],
    '6': [
        "06:45","07:30","08:15","09:00","09:45","10:45", "11:30",
        "12:15", "13:00", "13:45",    "14:30", "15:15", "16:00",
        "16:45","17:30", "18:30", "19:15", "20:00", "20:45", "21:30"
    ],
    '7': [
        "06:50", "07:35", "08:20", "09:05","09:50", "10:50", "11:35", 
        "12:20", "13:05", "13:50", "14:35", "15:20", "16:05","16:50", 
        "17:35", "18:35", "19:20","20:05", "20:50", "21:35"
    ],
    '8': [
        "06:55", "07:40", "08:25", "09:10","09:55", "10:55", "11:40", 
        "12:25", "13:10", "13:55", "14:40", "15:25","16:10","16:55", 
        "17:40", "18:40", "19:25",    "20:10", "20:55", "21:40"
    ]
}
paradas_16B = {
    '1': [
        "07:20", "08:20", "09:20", "10:20", "11:20", "12:20", 
        "13:20", "14:20", "15:20", "16:20", "17:20", "18:20",
        "19:20", "20:20", "21:20"
    ],
    '2': [
        "07:35", "08:35", "09:35", "10:35","11:35", "12:35", 
        "13:35", "14:35", "15:35", "16:35", "17:35", "18:35", 
        "19:35", "20:35", "21:35"
    ],
    '3': [
        "07:45", "08:45", "09:45", "10:45","11:45", "12:45", 
        "13:45", "14:45", "15:45", "16:45", "17:45", "18:45", 
        "19:45", "20:45", "21:45"
    ],
    '4': [
        "07:55", "08:55", "09:55", "10:55", "11:55", "12:55", 
        "13:55", "14:55", "15:55", "16:55", "17:55", "18:55",    
        "19:55", "20:55", "21:55"
    ],
    '5': [
        "07:57", "08:57", "09:57", "10:57", "11:57", "12:57", 
        "13:57", "14:57", "15:57", "16:57", "17:57", "18:57", 
        "19:57", "20:57", "21:57"
    ],
    '6': [
        "08:00", "09:00", "10:00", "11:00","12:00", "13:00", 
        "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
        "20:00", "21:00", "22:00"
    ],
    '7': [
        "08:05", "09:05", "10:05", "11:05", "12:05", "13:05", 
        "14:05", "15:05", "16:05", "17:05", "18:05", "19:05",
        "20:05", "21:05", "22:05"
    ],
    '8': [
        "08:10", "09:10", "10:10", "11:10", "12:10", "13:10", 
        "14:10", "15:10", "16:10", "17:10", "18:10", "19:10", 
        "20:10", "21:10", "22:10"
    ],
}

mostrar_menuPrincipal = True
while mostrar_menuPrincipal == True:
    ancho = 50
    print(
        "✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n"
        "🚌 Bienvenido a Que Bondi 🚌\n"
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
    except ValueError:
        print("\n❌ Error: Opción no válida. Intente de nuevo. 🤗")
        print()
        continue
    match opcion_menu:      
        case 0:
            mostrar_menuPrincipal = False
            print("\n🚫 Programa Finalizado 🚫")

        case 1:
            mostrar_busqueda = True
            while mostrar_busqueda == True:
                print("\n¿Como desea iniciar la busqueda?\n"
                "1️⃣  Por número de línea\n"
                "2️⃣  Nombre de calle\n"
                "3️⃣  Volver al menu\n"
                )
                try:
                    busqueda = int(input("\n👉🏽 Elija una opción: "))
                except ValueError:
                    print("\n❌ Error: Opción no válida. Intente de nuevo. 🤗")
                    continue
                while busqueda != 1 and busqueda != 2 and busqueda != 3:
                    print("\n❌ Error: Opción no válida. Intente de nuevo. 🤗")
                    busqueda = int(input("👉🏽 Elija una opción: "))

                match busqueda:
                    case 1:
                        print("\n🚌 𝐋𝐢𝐧𝐞𝐚𝐬 𝐃𝐢𝐬𝐩𝐨𝐧𝐢𝐛𝐥𝐞𝐬 🚌 \n🧡 16 / 🩶 16B\n")
                        
                        linea = input("\n👉🏽 Ingrese la línea que desea tomar (16/16B): ")
                        while linea != "16" and linea != "16B":
                            print("\n❌ Error: Línea no válida. Intente de nuevo. 🤗\n")
                            linea = input("👉🏽 Ingrese la línea que desea tomar (16/16B):")
                            
                        if linea == "16":
                            print(
                                "\n🚌🧡 𝐏𝐚𝐫𝐚𝐝𝐚𝐬 𝐝𝐞 𝐥𝐚 𝐋𝐢𝐧𝐞𝐚 𝐂𝟏-𝟏𝟔 🧡🚌\n"
                                "1️⃣  Centro de Transferencias\n"
                                "2️⃣  Av. Irigoyen / San Luis\n"
                                "3️⃣  Bv. Alvear / Prol. Sarmiento\n"
                                "4️⃣  Prol. Sarmiento / Av. Universidad\n"
                                "5️⃣  Lacar / Aconcagua\n"
                                "6️⃣  M.M. Moreno / Prol. Sarmiento\n"
                                "7️⃣  Bv. Alvear / San Luis\n"
                                "8️⃣  Lisandro de la Torre / Bs. As.\n"
                            )
                            parada_ingresada = input("📍 Ingrese la parada de colectivo más cercana: ")
                            while parada_ingresada < '1' or parada_ingresada > '8':
                                print("\n❌ Error: Parada no válida. Intente de nuevo. 🤗")
                                parada_ingresada = input("\n📍 Ingrese la parada de colectivo más cercana: ")
                                
                            hora_llegada = input("\n🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                            while len(hora_llegada) != 5:
                                print("\n❌ Error: Formato de hora inválido (ej: 12:30). Intente de nuevo. 🤗\n")
                                hora_llegada = input("\n🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                    
                            print(f"\nHorarios disponibles antes de las {hora_llegada}: ")
                            mostrar_horarios_validos(paradas_16, parada_ingresada, hora_llegada)

                            print("\n🗺️ Generando mapa de recorrido desde la parada hasta la UTN...")
                            origen = coords_paradas_16[parada_ingresada]
                            destino = utn_coords

                            ruta = obtener_ruta_osrm(origen, destino)
                            if ruta is None:
                                ruta = [origen, destino]
                                print("\n⚠️ No se pudo obtener ruta por calles (OSRM).")

                            mapa = folium.Map(location=origen, zoom_start=14)
                            folium.Marker(origen,popup="Tu parada",icon=folium.Icon(color="orange")).add_to(mapa)
                            folium.Marker(destino,popup="UTN",icon=folium.Icon(color="blue")).add_to(mapa)
                            folium.PolyLine(ruta, weight=4, color="red").add_to(mapa)

                            nombre_archivo = f"recorrido_16_parada_{parada_ingresada}.html"
                            mapa.save(nombre_archivo)
                            print(f"\n➡️ Mapa guardado como: {nombre_archivo}\n")

                            salida = input("\n👉🏽 Ingrese 0 para finalizar ")
                            if salida == '0':
                                print("\n🚫 Programa Finalizado 🚫")
                                mostrar_busqueda = False
                                mostrar_menuPrincipal = False
                                continue

                        elif linea == "16B":
                            print(
                                "\n🚌🩶 𝐏𝐚𝐫𝐚𝐝𝐚𝐬 𝐝𝐞 𝐥𝐚 𝐋𝐢𝐧𝐞𝐚 𝐆𝟏-𝟏𝟔𝐁 🩶🚌\n"
                                "1️⃣ Centro de Transferencias\n"
                                "2️⃣ Bv Italia / Jujuy\n"
                                "3️⃣ Gruta\n"
                                "4️⃣ Terminal de Omnibús\n"
                                "5️⃣ Bv. Alvear / Mendoza\n"
                                "6️⃣ Bv España / La Rioja\n"
                                "7️⃣ Jauretche / Bv España (UNVM)\n"
                                "8️⃣ Rawson / Bv España\n"
                            )
                            parada_ingresada = input("📍 Ingrese la parada de colectivo más cercana: ")
                            while parada_ingresada < '1' or parada_ingresada > '8':
                                print("\n❌ Error: Parada no válida. Intente de nuevo. 🤗")
                                parada_ingresada = input("\n📍 Ingrese la parada de colectivo más cercana: ")

                            hora_llegada = input("\n🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                            while len(hora_llegada) != 5:
                                print("\n❌ Error: Formato de hora inválido (ej: 12:30). Intente de nuevo. 🤗\n")
                                hora_llegada = input("\n🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")    
                            print(f"\nHorarios disponibles antes de las {hora_llegada}: ")
                            mostrar_horarios_validos(paradas_16B, parada_ingresada, hora_llegada)

                            print("\n🗺️ Generando mapa de recorrido desde la parada hasta la UTN...")
                            origen = coords_paradas_16B[parada_ingresada]
                            destino = utn_coords
                            ruta = obtener_ruta_osrm(origen, destino)
                            
                            if ruta is None:
                                ruta = [origen, destino]
                                print("\n⚠️ No se pudo obtener ruta por calles (OSRM). Se dibuja línea recta como fallback.")
                            mapa = folium.Map(location=origen, zoom_start=14)
                            folium.Marker(origen,popup="Tu parada",icon=folium.Icon(color="gray")).add_to(mapa)
                            folium.Marker(destino,popup="UTN",icon=folium.Icon(color="blue")).add_to(mapa)
                            folium.PolyLine(ruta, weight=4, color="purple").add_to(mapa)

                            nombre_archivo = f"recorrido_16B_parada_{parada_ingresada}.html"
                            mapa.save(nombre_archivo)
                            print(f"\n➡️ Mapa guardado como: {nombre_archivo}\n")

                            salida = input("\n👉🏽 Ingrese 0 para finalizar ")
                            if salida == '0':
                                print("\n🚫 Programa Finalizado 🚫")
                                mostrar_busqueda = False
                                mostrar_menuPrincipal = False

                    case 2:
                        calle_usuario = input("\n👉🏽 Ingrese el nombre de la calle donde se encuentra: ")
                        while calle_usuario.strip() == "":
                            print("\n❌ Error: Calle no válida. Intente de nuevo. 🤗")
                            calle_usuario = input("\n👉🏽 Ingrese el nombre de la calle donde se encuentra: ")
                        paradas_16_calles = [
                            "Centro de Transferencias",
                            "Av. Irigoyen / San Luis",
                            "Bv. Alvear / Prol. Sarmiento",
                            "Prol. Sarmiento / Av. Universidad",
                            "Lacar / Aconcagua",
                            "M.M. Moreno / Prol. Sarmiento",
                            "Bv. Alvear / San Luis",
                            "Lisandro de la Torre / Bs. As."
                        ]
                        paradas_16B_calles = [
                            "Centro de Transferencias",
                            "Bv Italia / Jujuy",
                            "Gruta",
                            "Bv. Alvear / Prol. Sarmiento",
                            "Bv. Alvear / Mendoza",
                            "Bv España / La Rioja",
                            "Jauretche / Bv España (UNVM)",
                            "Rawson / Bv España"
                        ]

                        encontrados_16 = buscarCalles(paradas_16_calles, calle_usuario)
                        encontrados_16B = buscarCalles(paradas_16B_calles, calle_usuario)
                        if len(encontrados_16) > 0:
                            print("\n🧡 En la linea 16:")
                            for numero, calles in encontrados_16:
                                print(f"  {numero}. {calles}")
                        
                        if len(encontrados_16B) > 0:
                            print("\n🩶 En la linea 16B:")
                            for numero, calles in encontrados_16B:
                                print(f"  {numero}. {calles}")
                        
                        if len(encontrados_16) == 0 and len(encontrados_16B) == 0:
                            print(f"\n❌ No se encontró la calle '{calle_usuario}' en ninguna línea")
                            print("\n📍 Paradas disponibles:\n")
                            print("🧡 Línea 16:")
                            for i in range(len(paradas_16_calles)):
                                print(f"  {i+1}. {paradas_16_calles[i]}")
                            print("\n🩶 Línea 16B:")
                            for i in range(len(paradas_16B_calles)):
                                print(f"  {i+1}. {paradas_16B_calles[i]}")
                            continue
                        
                        if len(encontrados_16) > 0 or len(encontrados_16B) > 0:
                            linea = input("\n👉🏽 ¿Qué línea desea tomar? (16/16B): ")
                            while (
                            (linea == "16" and len(encontrados_16) == 0) or (linea == "16B" and len(encontrados_16B) == 0)
                            or (linea != "16" and linea != "16B")
                                ):
                                print("❌ Error: Línea no válida. Intente de nuevo. 🤗")
                                linea = input("👉🏽 ¿Qué línea desea tomar? (16/16B): ")
                            
                            if linea == "16":
                                print("\n🚌🧡 Paradas encontradas en la Línea 16 🧡🚌")
                                for numero, calles in encontrados_16:
                                    print(f"  {numero}. {calles}")
                                
                                parada_ingresada = input("\n📍 Ingrese el número de parada: ")

                                numeros_validos = []
                                for num, _ in encontrados_16:
                                    numeros_validos.append(str(num))

                                while parada_ingresada not in numeros_validos:
                                    print("❌ Error: Parada no válida. Intente de nuevo. 🤗")
                                    parada_ingresada = input("📍 Ingrese el número de parada: ")

                                hora_llegada = input("\n🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                while len(hora_llegada) != 5:
                                    print("\n❌ Error: Formato de hora inválido (ej: 12:30). Intente de nuevo. 🤗\n")
                                    hora_llegada = input("\n🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                print(f"\nHorarios disponibles antes de las {hora_llegada}: ")
                                mostrar_horarios_validos(paradas_16, parada_ingresada, hora_llegada)
     
                                print("\n🗺️ Generando mapa de recorrido desde la parada hasta la UTN...")
                                origen = coords_paradas_16[parada_ingresada]
                                destino = utn_coords
                                ruta = obtener_ruta_osrm(origen, destino)
                                if ruta is None:
                                    ruta = [origen, destino]
                                    print("\n⚠️ No se pudo obtener ruta por calles (OSRM). Se dibuja línea recta como fallback.")
                                
                                mapa = folium.Map(location=origen, zoom_start=14)
                                folium.Marker(origen, popup="Tu parada", icon=folium.Icon(color="orange")).add_to(mapa)
                                folium.Marker(destino, popup="UTN", icon=folium.Icon(color="blue")).add_to(mapa)
                                folium.PolyLine(ruta, weight=4, color="red").add_to(mapa)
                                nombre_archivo = f"recorrido_16_parada_{parada_ingresada}.html"
                                mapa.save(nombre_archivo)
                                print(f"➡️ Mapa guardado como: {nombre_archivo}\n")
                                
                                salida = input("👉🏽 Ingrese 0 para finalizar: ")
                                if salida == '0':
                                    print("\n🚫 Programa Finalizado 🚫")
                                    mostrar_busqueda = False
                                    mostrar_menuPrincipal = False
                            
                            elif linea == "16B":
                                print("\n🚌🩶 Paradas encontradas en la Línea 16B 🩶🚌")
                                for numero, calles in encontrados_16B:
                                    print(f"  {numero}. {calles}")
                                parada_ingresada = input("\n📍 Ingrese el número de parada: ")
                  
                                numeros_validos = []
                                for num, _ in encontrados_16B:
                                    numeros_validos.append(str(num))
                    
                                while parada_ingresada not in numeros_validos:
                                    print("❌ Error: Parada no válida. Intente de nuevo. 🤗")
                                    parada_ingresada = input("📍 Ingrese el número de parada: ")
                                
                                hora_llegada = input("\n🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                while len(hora_llegada) != 5:
                                    print("\n❌ Error: Formato de hora inválido (ej: 12:30). Intente de nuevo. 🤗\n")
                                    hora_llegada = input("\n🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                
                                print(f"\nHorarios disponibles antes de las {hora_llegada}: ")
                                mostrar_horarios_validos(paradas_16B, parada_ingresada, hora_llegada)
                                print("\n🗺️ Generando mapa de recorrido desde la parada hasta la UTN...")
                                origen = coords_paradas_16B[parada_ingresada]
                                destino = utn_coords
                                ruta = obtener_ruta_osrm(origen, destino)
                                if ruta is None:
                                    ruta = [origen, destino]
                                    print("⚠️ No se pudo obtener ruta por calles (OSRM). Se dibuja línea recta como fallback.")
                                
                                
                                mapa = folium.Map(location=origen, zoom_start=14)
                                folium.Marker(origen, popup="Tu parada", icon=folium.Icon(color="gray")).add_to(mapa)
                                folium.Marker(destino, popup="UTN", icon=folium.Icon(color="blue")).add_to(mapa)
                                folium.PolyLine(ruta, weight=4, color="purple").add_to(mapa)
                            
                                nombre_archivo = f"recorrido_16B_parada_{parada_ingresada}.html"
                                mapa.save(nombre_archivo)
                                print(f"\n➡️ Mapa guardado como: {nombre_archivo}\n")
                                
                                salida = input("👉🏽 Ingrese 0 para finalizar: ")
                                if salida == '0':
                                    print("\n🚫 Programa Finalizado 🚫")
                                    mostrar_busqueda = False
                                    mostrar_menuPrincipal = False
                    
                    case 3:
                        print()
                        mostrar_busqueda = False
                        break