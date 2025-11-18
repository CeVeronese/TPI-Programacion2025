def buscarCalles(paradas_calles, calle_usuario):
    encontrados = []
    calle_minuscula = calle_usuario.lower()
    
    for i in range(len(paradas_calles)):
        parada_minuscula = paradas_calles[i].lower()
        
        if calle_minuscula in parada_minuscula:
            encontrados.append((i+1, paradas_calles[i]))
    
    return encontrados

calle_usuario = input("Ingrese el nombre de la calle donde se encuentra: ")

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
    "Terminal de Omnibús",
    "Bv Alvear / Mendoza",
    "Bv España / La Rioja",
    "Jauretche / Bv España (UNVM)",
    "Rawson / Bv España"
]

encontrados_16 = buscarCalles(paradas_16_calles, calle_usuario)

encontrados_16B = buscarCalles(paradas_16B_calles, calle_usuario)

if len(encontrados_16) > 0:
    print("\nEn la linea 16:")
    for numero,calles in encontrados_16:
        print(numero,calles)
else:
    print(f"\nNo se encontro la calle {calle_usuario} en la linea 16")

if len(encontrados_16B) > 0:
    print("\nEn la linea 16B")
    for numero,calles in encontrados_16B:
        print(numero,calles)
else:
    print(f"\nNo se encontro la calle {calle_usuario} en la linea 16B")