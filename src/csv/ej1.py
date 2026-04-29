import csv

with open(".\\archivos.csv\\AEROPUERTOS_DE_OPERACIÓN_AEROLINEA_SATENA_20260429.csv", 'r', encoding="utf-8") as csvfile:
    lector = csv.reader(csvfile, delimiter=",")
    encabezado = next(lector)
    i = 0
    elevacion_t = 0
    for fila in lector:
        dato = fila[7].replace(",",".")
        elevacion_t += float(dato)
        i += 1
        print(f"aeropuerto: {fila[1]}, con coordenadas: {fila[10]},{fila[11]}")
   
    ele_promedio = elevacion_t/i
    print(f"la elevacion promedio de los aeropuertos en colombia es: {ele_promedio:.2f} ft.")