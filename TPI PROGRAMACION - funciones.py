def mostrar_horarios_validos(paradas_dict, parada_user, hora_llegada):
    hora_usuario = datetime.strptime(hora_llegada, "%H:%M").time()
    horarios_parada = paradas_dict[parada_user]
    horarios_validos = []

    for hora in horarios_parada:
        hora_colectivo = datetime.strptime(hora, "%H:%M").time()
        if hora_colectivo < hora_usuario:
            horarios_validos.append(hora)

    for hora in horarios_validos:
        print(hora)
