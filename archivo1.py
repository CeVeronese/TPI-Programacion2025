def horariosReales():
    from datetime import datetime
    hora_usuario = datetime.strptime(hora_llegada, "%H:%M").time()
    horarios_parada = paradas_G1_16B,paradas_G1_16B[parada_user]
    horarios_validos = []
    for hora in horarios_parada:
        hora_colectivo = datetime.strptime(hora, "%H:%M").time()
        if hora_colectivo < hora_usuario:
            horarios_validos.append(hora)
    for horario in horarios_validos: 
            return horario

paradas_C1_16 = {
    '1': [
        "06:15", "07:00", "07:45", "08:30", "09:15", "10:15", "11:00", "11:45","12:30", "13:15", "14:00", "14:45", 
        "15:30", "16:15", "17:00", "18:00","18:45", "19:30", "20:15", "21:00"
    ],
    '2': [
        "06:20", "07:05", "07:50", "08:35", "09:20", "10:20", "11:05", "11:50","12:35", "13:20", "14:05", "14:50", 
        "15:35", "16:20", "17:05", "18:05", "18:50", "19:35", "20:20", "21:20"
    ],
    '3': [
        "06:25", "07:10","07:55", "08:40", "09:25",	"10:25", "11:10", "11:55", "12:40", "13:25", "14:10", "14:55",
        "15:40", "16:25", "17:10", "18:10", "18:55", "19:40", "20:25", "21:10"
    ],
    '4': [
        "06:30", "07:15", "08:00", "08:45", "09:30", "10:30", "11:15", "12:00", "12:45", "13:30", "14:15", "15:00",
        "15:45", "16:30", "17:15", "18:15", "19:00", "19:45", "20:30", "21:15"
    ],
    '5': [
        "06:40", "07:25", "08:10", "08:55",	"09:40", "10:40", "11:25", "12:10", "12:55", "13:40", "14:25", "15:10",
        "15:55", "16:40", "17:25",	"18:25", "19:10", "19:55", "20:40",	"21:25"
    ],
    '6': [
        "06:45","07:30","08:15","09:00","09:45","10:45", "11:30","12:15", "13:00", "13:45",	"14:30", "15:15", "16:00",
        "16:45","17:30", "18:30", "19:15", "20:00", "20:45", "21:30"
    ],
    '7': [
        "06:50", "07:35", "08:20", "09:05",	"09:50", "10:50", "11:35", "12:20", "13:05", "13:50", "14:35", "15:20", "16:05",
        "16:50", "17:35", "18:35", "19:20",	"20:05", "20:50", "21:35"
    ],
    '8': [
        "06:55", "07:40", "08:25", "09:10",	"09:55", "10:55", "11:40", "12:25", "13:10", "13:55", "14:40", "15:25",	"16:10",
        "16:55", "17:40", "18:40", "19:25",	"20:10", "20:55", "21:40"
    ]
}
paradas_G1_16B = {
    '1': [
        "07:20", "08:20", "09:20", "10:20",	"11:20", "12:20", "13:20", "14:20", "15:20", "16:20", "17:20", "18:20",	"19:20", "20:20",
        "21:20"
    ],
    '2': [
        "07:35", "08:35", "09:35", "10:35",	"11:35", "12:35", "13:35", "14:35", "15:35", "16:35", "17:35", "18:35", "19:35", "20:35", "21:35"
    ],
    '3': [
        "07:45", "08:45", "09:45", "10:45",	"11:45", "12:45", "13:45", "14:45", "15:45", "16:45", "17:45", "18:45", "19:45", "20:45", "21:45"
    ],
    '4': [
        "07:55", "08:55", "09:55", "10:55", "11:55", "12:55", "13:55", "14:55", "15:55", "16:55", "17:55", "18:55",	"19:55", "20:55", "21:55"
    ],
    '5': [
        "07:57", "08:57", "09:57", "10:57",	"11:57", "12:57", "13:57", "14:57", "15:57", "16:57", "17:57", "18:57", "19:57", "20:57", "21:57"
    ],
    '6': [
        "08:00", "09:00", "10:00", "11:00",	"12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",	"20:00", "21:00", "22:00"
    ],
    '7': [
        "08:05", "09:05", "10:05", "11:05", "12:05", "13:05", "14:05", "15:05", "16:05", "17:05", "18:05", "19:05",	"20:05", "21:05", "22:05"
    ],
    '8': [
        "08:10", "09:10", "10:10", "11:10",	"12:10", "13:10", "14:10", "15:10", "16:10", "17:10", "18:10", "19:10", "20:10", "21:10", "22:10"
    ],
}
try:
    print("🚌 𝐋𝐢𝐧𝐞𝐚𝐬 𝐃𝐢𝐬𝐩𝐨𝐧𝐢𝐛𝐥𝐞𝐬 🚌 \n🧡 C1-16 / 🩶 G1-16B")
    linea = input()
    if linea == "C1-16":
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
        parada_user = input("Ingrese la parada de colectivo más cercana: ")
        hora_llegada = input("Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30): ")
        horariosReales()
    elif linea == "G1-16B":
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
            parada_user = input("Ingrese la parada de colectivo más cercana: ")
            hora_llegada = input("Ingrese la hora a la que quiere llegar a la UTN (ej: 12:30): ")
            horariosReales()
    else:
        print("ERROR, LA LINEA NO EXIS")
    

except KeyError:
    print("⚠️ERROR: No hay una linea para esa parada")



"""
horarios_parada = paradas_C1_16.get(parada_user)
    
    # 3b. Si la parada no se encontró en C1_16, intentar en G1_16B
    if horarios_parada is None:
        horarios_parada = paradas_G1_16B.get(parada_user)
        
        # 3c. Si la parada sigue sin encontrarse, lanzamos el error manualmente
        if horarios_parada is None:
            raise KeyError # Se lanza la excepción KeyError para ser capturada abajo

"""