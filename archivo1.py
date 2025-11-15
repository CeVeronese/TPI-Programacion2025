paradas = {
    'Centro de Transferencias': [
        "06:15", "07:00", "07:45", "08:30", "09:15", "10:15", "11:00", "11:45","12:30", "13:15", "14:00", "14:45", 
        "15:30", "16:15", "17:00", "18:00","18:45", "19:30", "20:15", "21:00"
    ],
    'Av. Irigoyen / San Luis': [
        "06:20", "07:05", "07:50", "08:35", "09:20", "10:20", "11:05", "11:50","12:35", "13:20", "14:05", "14:50", 
        "15:35", "16:20", "17:05", "18:05", "18:50", "19:35", "20:20", "21:20"
    ]
}
try:
    parada_user = input("Ingrese su parada más cercana: ")
    hora_user = input("Ingrese la hora límite a la que quiere llegar a la UTN (ej: 12:30): ")

    horarios_parada = paradas[parada_user]
    for i in range(len(horarios_parada)):
        if horarios_parada[i] == hora_user:
            posicion = i
            print("Colectivos que puede tomar: ")
            for i in range(0,posicion):
                print(horarios_parada[i])

except KeyError:
    print("La parada NO EXISTE")