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
    """
    origen, destino: [lat, lon]
    devuelve: lista de puntos [[lat, lon], ...] siguiendo calles (si OSRM responde)
    """
    # OSRM espera "lon,lat"
    lon1, lat1 = origen[1], origen[0]
    lon2, lat2 = destino[1], destino[0]
    url = f"http://router.project-osrm.org/route/v1/{profile}/{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson"
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        coords = data["routes"][0]["geometry"]["coordinates"]  # lista [lon, lat]
        # convertimos a [lat, lon] para folium
        ruta = [[pt[1], pt[0]] for pt in coords]
        return ruta
    except Exception as e:
        # si falla, devolvemos None para que el llamador haga fallback
        # (no abortamos el programa)
        # print("Advertencia OSRM:", e)
        return None


coords_paradas_16 = {
    1: [-32.409430, -63.246268],    # Centro de Transferencias
    2: [-32.416295, -63.240207],    # Av. Irigoyen / San Luis
    3: [-32.414313, -63.233163],    # Bv. Alvear / Prol. Sarmiento
    4: [-32.408427, -63.221721],    # Prol. Sarmiento / Av. Universidad
    5: [-32.408427, -63.221721],    # Lacar / Aconcagua
    6: [-32.420183, -63.241467],    # M.M. Moreno / Prol. Sarmiento
    7: [-32.413076, -63.234585],    # Bv. Alvear / San Luis
    8: [-32.409158, -63.216909]     # UTN Villa María (Lisandro de la Torre / Bs. As.)
}

coords_paradas_16B = {
    1: [-32.409430, -63.246268],    # Centro de Transferencias
    2: [-32.410070, -63.255739],    # Bv Italia / Jujuy
    3: [-32.419213, -63.239599],    # Gruta
    4: [-32.414313, -63.233163],    # Terminal de Omnibús
    5: [-32.411279, -63.236068],    # Bv Alvear / Mendoza
    6: [-32.404321, -63.242458],    # Bv España / La Rioja
    7: [-32.384046, -63.259246],    # Jauretche / Bv España (UNVM)
    8: [-32.398598, -63.247446]     # UTN Villa María (Rawson / Bv España)
}

UTN_COORDS_16 = coords_paradas_16[8]
UTN_COORDS_16B = coords_paradas_16B[8]

paradas_16 = {
    1: [
        "06:15", "07:00", "07:45", "08:30", "09:15", "10:15", "11:00", "11:45","12:30", "13:15", "14:00", "14:45", 
        "15:30", "16:15", "17:00", "18:00","18:45", "19:30", "20:15", "21:00"
    ],
    2: [
        "06:20", "07:05", "07:50", "08:35", "09:20", "10:20", "11:05", "11:50","12:35", "13:20", "14:05", "14:50", 
        "15:35", "16:20", "17:05", "18:05", "18:50", "19:35", "20:20", "21:20"
    ],
    3: [
        "06:25", "07:10","07:55", "08:40", "09:25", "10:25", "11:10", "11:55", "12:40", "13:25", "14:10", "14:55",
        "15:40", "16:25", "17:10", "18:10", "18:55", "19:40", "20:25", "21:10"
    ],
    4: [
        "06:30", "07:15", "08:00", "08:45", "09:30", "10:30", "11:15", "12:00", "12:45", "13:30", "14:15", "15:00",
        "15:45", "16:30", "17:15", "18:15", "19:00", "19:45", "20:30", "21:15"
    ],
    5: [
        "06:40", "07:25", "08:10", "08:55",    "09:40", "10:40", "11:25", "12:10", "12:55", "13:40", "14:25", "15:10",
        "15:55", "16:40", "17:25",    "18:25", "19:10", "19:55", "20:40",    "21:25"
    ],
    6: [
        "06:45","07:30","08:15","09:00","09:45","10:45", "11:30","12:15", "13:00", "13:45",    "14:30", "15:15", "16:00",
        "16:45","17:30", "18:30", "19:15", "20:00", "20:45", "21:30"
    ],
    7: [
        "06:50", "07:35", "08:20", "09:05",    "09:50", "10:50", "11:35", "12:20", "13:05", "13:50", "14:35", "15:20", "16:05",
        "16:50", "17:35", "18:35", "19:20",    "20:05", "20:50", "21:35"
    ],
    8: [
        "06:55", "07:40", "08:25", "09:10",    "09:55", "10:55", "11:40", "12:25", "13:10", "13:55", "14:40", "15:25",    "16:10",
        "16:55", "17:40", "18:40", "19:25",    "20:10", "20:55", "21:40"
    ]
}
paradas_16B = {
    1: [
        "07:20", "08:20", "09:20", "10:20",    "11:20", "12:20", "13:20", "14:20", "15:20", "16:20", "17:20", "18:20",    "19:20", "20:20",
        "21:20"
    ],
    2: [
        "07:35", "08:35", "09:35", "10:35",    "11:35", "12:35", "13:35", "14:35", "15:35", "16:35", "17:35", "18:35", "19:35", "20:35", "21:35"
    ],
    3: [
        "07:45", "08:45", "09:45", "10:45",    "11:45", "12:45", "13:45", "14:45", "15:45", "16:45", "17:45", "18:45", "19:45", "20:45", "21:45"
    ],
    4: [
        "07:55", "08:55", "09:55", "10:55", "11:55", "12:55", "13:55", "14:55", "15:55", "16:55", "17:55", "18:55",    "19:55", "20:55", "21:55"
    ],
    5: [
        "07:57", "08:57", "09:57", "10:57",    "11:57", "12:57", "13:57", "14:57", "15:57", "16:57", "17:57", "18:57", "19:57", "20:57", "21:57"
    ],
    6: [
        "08:00", "09:00", "10:00", "11:00",    "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",    "20:00", "21:00", "22:00"
    ],
    7: [
        "08:05", "09:05", "10:05", "11:05", "12:05", "13:05", "14:05", "15:05", "16:05", "17:05", "18:05", "19:05",    "20:05", "21:05", "22:05"
    ],
    8: [
        "08:10", "09:10", "10:10", "11:10",    "12:10", "13:10", "14:10", "15:10", "16:10", "17:10", "18:10", "19:10", "20:10", "21:10", "22:10"
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
        
        match opcion_menu:
            case 0:
                mostrar_menuPrincipal = False
                print("\n🚫 Programa Finalizado 🚫")

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
                                parada_ingresada = int(input("📍 Ingrese la parada de colectivo más cercana: "))
                                if parada_ingresada < 1 or parada_ingresada > 8:
                                    print("⚠️  La linea no pasa por la parada ingresada ⚠️")
                                else:
                                    try:
                                        hora_llegada = input("🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                        print()
                                        print(f"Horarios disponibles antes de las {hora_llegada}: ")
                                        mostrar_horarios_validos(paradas_16, parada_ingresada, hora_llegada)

                                        print("\n🗺️ Generando mapa solo con TU parada y la UTN (ruta por calles)...")

                                        origen = coords_paradas_16[parada_ingresada]
                                        destino = UTN_COORDS_16

                                        ruta = obtener_ruta_osrm(origen, destino)
                                        if ruta is None:
                                            # fallback: línea recta
                                            ruta = [origen, destino]
                                            print("⚠️ No se pudo obtener ruta por calles (OSRM). Se dibuja línea recta como fallback.")

                                        mapa = folium.Map(location=origen, zoom_start=14)

                                        folium.Marker(origen,
                                                      popup="Tu parada",
                                                      icon=folium.Icon(color="orange")).add_to(mapa)

                                        folium.Marker(destino,
                                                      popup="UTN",
                                                      icon=folium.Icon(color="blue")).add_to(mapa)

                                        folium.PolyLine(ruta, weight=4, color="red").add_to(mapa)

                                        nombre_archivo = f"recorrido_16_parada_{parada_ingresada}.html"
                                        mapa.save(nombre_archivo)
                                        print(f"➡️ Mapa guardado como: {nombre_archivo}\n")

                                        salida = input("👉🏽 Ingrese 0 para finalizar ")
                                        if salida == '0':
                                            print("\n🚫 Programa Finalizado 🚫")
                                            mostrar_busqueda = False
                                            mostrar_menuPrincipal = False
                                            continue
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
                                parada_ingresada = int(input("📍 Ingrese la parada de colectivo más cercana: "))
                                    
                                if parada_ingresada < 1 or parada_ingresada > 8:
                                    print("⚠️  La linea no pasa por la parada ingresada ⚠️")
                                    print()
                                else:
                                    try:
                                        hora_llegada = input("🕒 Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30) 🕒: ")
                                        print()
                                        print(f"Horarios disponibles antes de las {hora_llegada}: ")
                                        mostrar_horarios_validos(paradas_16B, parada_ingresada, hora_llegada)

                                        print("\n🗺️ Generando mapa solo con TU parada y la UTN (ruta por calles)...")

                                        origen = coords_paradas_16B[parada_ingresada]
                                        destino = UTN_COORDS_16B

                                        ruta = obtener_ruta_osrm(origen, destino)
                                        if ruta is None:
                                            ruta = [origen, destino]
                                            print("⚠️ No se pudo obtener ruta por calles (OSRM). Se dibuja línea recta como fallback.")

                                        mapa = folium.Map(location=origen, zoom_start=14)

                                        folium.Marker(origen,
                                                      popup="Tu parada",
                                                      icon=folium.Icon(color="gray")).add_to(mapa)

                                        folium.Marker(destino,
                                                      popup="UTN",
                                                      icon=folium.Icon(color="blue")).add_to(mapa)

                                        folium.PolyLine(ruta, weight=4, color="purple").add_to(mapa)

                                        nombre_archivo = f"recorrido_16B_parada_{parada_ingresada}.html"
                                        mapa.save(nombre_archivo)
                                        print(f"➡️ Mapa guardado como: {nombre_archivo}\n")

                                        salida = input("👉🏽 Ingrese 0 para finalizar ")
                                        if salida == '0':
                                            print("\n🚫 Programa Finalizado 🚫")
                                            mostrar_busqueda = False
                                            mostrar_menuPrincipal = False
                                            continue

                                    except ValueError:
                                        print("🕒❌ La hora ingresada no es válida ❌🕒")
                                
                            break
    except ValueError:
        print("\nLa entrada no es valida. intentelo nuevamente")
        print()
        continue
