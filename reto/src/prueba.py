import csv
import matplotlib.pyplot as plt
with open("archivos.csv\\AEROPUERTOS_DE_OPERACIÓN_AEROLINEA_SATENA_20260429.csv", "r", encoding="utf-8") as archivo:
   x = []
   y = []
   lector = csv.reader(archivo)
   encabezados = next(lector)
   print("\nColumnas disponibles:")
   for i, col in enumerate(encabezados): 
      print(i, "-", col) 
   columna_x = encabezados[int(input("Seleccione columna X: "))]
   columna_y = encabezados[int(input("Seleccione columna Y numérica: "))]
   indice_x = encabezados.index(columna_x)
   indice_y = encabezados.index(columna_y)
   for fila in lector:
      x.append(fila[indice_x])
      y.append(float(fila[indice_y]))
   plt.scatter (x,y)
   plt.title("Correlación de Variables:")
   plt.xlabel(columna_x)
   plt.ylabel(columna_y)
   plt.show()
