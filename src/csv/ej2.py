import csv

with open(".\\archivos.csv\\AEROPUERTOS_DE_OPERACIÓN_AEROLINEA_SATENA_20260429.csv", 'r', encoding="utf-8") as csvfile:
    lector = csv.DictReader(csvfile, delimiter=",")
    encabezado = next(lector)
    e = 0
    t = 0
    elevacion_t, t_total = 0, 0
    for fila in lector:
        dato = fila["ELEVACCIÓN (PIES)"].replace(",",".")
        t_total += float(fila["TEMPERATURA (°C)"])
        elevacion_t += float(dato)
        e += 1
        if float(fila["TEMPERATURA (°C)"]) != 0:
            t += 1
        print(f"aeropuerto: {fila["NOMBRE AEROPUERTO"]}, con coordenadas: {fila["LATITUD"]},{fila["LONGITUD"]}")
    t_promedio = t_total/t
    ele_promedio = elevacion_t/e
    print(f"la elevacion promedio de los aeropuertos en colombia es: {ele_promedio:.2f} ft.\nLa temperatura promedio de los aeropuertos en colombia es: {t_promedio:.2f} C°")