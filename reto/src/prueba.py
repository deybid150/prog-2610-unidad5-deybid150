import csv
import matplotlib as plt
with open("C:\\Users\\B09S202est\\Documents\\Programacion deybid2026\\prog-2610-unidad5-deybid150\\archivos.csv\\AEROPUERTOS_DE_OPERACIÓN_AEROLINEA_SATENA_20260429.csv", "r", encoding="utf-8") as archivo:
   lector = csv.DictReader(archivo)
   columnas = lector.fieldnames
   Ncol = len(columnas)
   print("columnas disponibles")
   i = 0
   for i in range(Ncol) :
      print(f"{i}) {columnas[i]}")
      i += 1
   seleccion = input("ingrese el nombre de la columna a analizar\n(asegurate de escribirlo bien): ")
   for nombre in lector[seleccion]:
      pass