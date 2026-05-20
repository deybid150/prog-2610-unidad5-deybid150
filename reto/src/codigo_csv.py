import csv # Librería para trabajar con archivos CSV
import statistics # Librería para cálculos estadísticos
import matplotlib.pyplot as plt # Librería para gráficos
import pathlib as pt

# VISTA PREVIA DE DATOS
def vista_previa_de_datos(archivo): # Función para mostrar primeras y últimas filas
    archivo.seek(0) # Regresa al inicio del archivo
    lector = csv.DictReader(archivo) # Lee el CSV como diccionarios
    datos = [] # Lista vacía para guardar las filas
    for fila in lector: # Recorre cada fila del CSV
        datos.append(fila) # Guarda la fila en la lista
    print("\n--- PRIMERAS 10 FILAS ---") 
    for fila in datos[:10]: 
        print(fila) 
    print("\n--- ÚLTIMAS 5 FILAS ---") 
    for fila in datos[-5:]: 
        print(fila) 

# ESTADÍSTICAS DESCRIPTIVAS
def calculo_estadisticas(archivo): 
    archivo.seek(0) # Regresa al inicio del archivo
    lector = csv.DictReader(archivo) # Lee el CSV como diccionario
    columnas = lector.fieldnames # Obtiene nombres de columnas
    print("\nColumnas disponibles:") 
    for i, col in enumerate(columnas): # Recorre columnas con índice
        print(i, "-", col) # Muestra número y nombre
    columna = columnas[int(input("Seleccione columna numérica: "))] 
    numeros = [] 
    for fila in lector: # Recorre cada fila
        valor = fila[columna].strip() 
        # Obtiene el valor de la columna y elimina espacios
        if valor != "": # Verifica que no esté vacío
            try: # Intenta convertir a número
                numeros.append(float(valor)) 
                # Convierte a float y lo guarda
            except ValueError: 
                # Si no puede convertir
                pass # Ignora el error
    if len(numeros) == 0: # Si no hay números válidos
        print("No hay datos válidos") 
        return 
    print("\n--- ESTADÍSTICAS ---") 
    print("Total válidos:", len(numeros))     
    print("Promedio:", statistics.mean(numeros))     
    print("Mediana:", statistics.median(numeros))     
    print("Máximo:", max(numeros))     
    print("Mínimo:", min(numeros)) 

def grafico_pastel(archivo):
    lector = csv.DictReader(archivo)
    columnas = lector.fieldnames
    Ncol = len(columnas)
    print("columnas disponibles")
    i = 0
    for i in range(Ncol) :
      print(f"{i}) {columnas[i]}")
      i += 1
    seleccion = input("ingrese el nombre de la columna a analizar\n(asegurate de escribirlo bien): ")
    categorias = {}
    for fila in lector:
      dato = fila[seleccion]
      if dato in categorias:
         categorias[dato] += 1
      else:
         categorias[dato] = 1
    nombres = list(categorias.keys())
    cantidades = list(categorias.values())
    plt.pie(cantidades, labels=nombres)
    plt.title(f"Participación de {seleccion}")
    plt.show()   
# GRÁFICO DE LÍNEAS
def grafico_lineas(archivo): 
    archivo.seek(0) # Regresa al inicio del archivo
    lector = csv.DictReader(archivo) # Lee el CSV como diccionario 
    columnas = lector.fieldnames # Obtiene nombres de columnas
    print("\nColumnas disponibles:")
    for i, col in enumerate(columnas): 
        print(i, "-", col) 
    columna_x = columnas[int(input("Seleccione columna X: "))]
    columna_y = columnas[int(input("Seleccione columna Y numérica: "))]
    x = [] 
    y = [] 
    for fila in lector: 
        try: # Intenta guardar datos válidos
            x.append(fila[columna_x]) 
            # Guarda dato de la columna X
            y.append(float(fila[columna_y])) 
            # Convierte y guarda dato numérico Y
        except:
            pass
    plt.plot(x, y, marker='o') 
    plt.title("Gráfico de Líneas")    
    plt.xlabel(columna_x) 
    plt.ylabel(columna_y) 
    plt.tight_layout() 
    plt.show() 
def grafico_dispersion(archivo):
    archivo.seek(0)
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

def archivos_csv():
    while True:
        ruta_texto = input("ingrese la ruta del archivo de texto con el que desea trabajar: ")
        ruta = pt.Path(ruta_texto)
        if not ruta.exists():
            print("el archivo no existe en esta ruta")
            continue

        print("¡El archivo existe! Procediendo a leer...")
        with ruta.open("r", encoding="utf-8") as archivo:
            while True:
                print("1) vista previa de datos\n2) calculo de estadisticas\n3) Grafico de pastel\n4)Grafico de lineas \n5)Grafico de dispersion \n6) Salir")
                opcion = input("elige una opcion numerica: ")
                if opcion == "1":
                    vista_previa_de_datos(archivo)
                elif opcion == "2":
                    calculo_estadisticas(archivo)
                elif opcion == "3":
                    grafico_pastel(archivo)
                elif opcion == "4":
                    grafico_lineas(archivo)
                elif opcion == "5":
                    grafico_dispersion(archivo)
                elif opcion == "6":
                    print("saliendo de la seccion de texto...")
                    break
                else:
                    print("ingrese un valor correcto")
            break