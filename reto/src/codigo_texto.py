import matplotlib.pyplot as plt
import pathlib as pt
def Resumen_Estadístico_del_Texto(archivo):
    contenido = archivo.read()
    archivo.seek(0) 
    texto = contenido.lower()
    lineas = archivo.readlines()
    c_lineas = len(lineas)
    signos = ".,;:!?¡¿"
    for signo in signos:
        texto = texto.replace(signo, " ")
    palabras = texto.split()
    c_palabras = len(palabras)
    print(f"la cantidad de lineas es {c_lineas}\nLa cantidad de palabras es {c_palabras}\n")
    conectores = ["de", "la", "que", "el", "en", "y", "a", "los", "del", "se",
    "las", "por", "un", "para", "con", "no", "una", "su", "al"]
    signos = ".,;:!?¡¿"
    for signo in signos:
        texto = texto.replace(signo, " ")
    frecuencia = {}
    for palabra in palabras:
        if palabra not in conectores:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
    F = frecuencia.items()
    lista = sorted(F)
    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            if lista[j][1] < lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("Las palabras más frecuentes son:")
    i = 0
    while i < len(lista):
        if i == 5:
            break
        print(f"{lista[i][0]}: {lista[i][1]}")
        i = i + 1

def archivos_log(archivo):
    contenido = archivo.read()
    contenido_mayus = contenido.upper()
    errores = {"ERROR": contenido_mayus.count("ERROR"), "404": contenido.count("404")}
    frecuencia_fechas = {}
    texto = contenido
    for signo in ".,;:!?¡¿()[]{}<>\"'":
        texto = texto.replace(signo, " ")
    palabras = texto.split()
    for palabra in palabras:
        if len(palabra) == 10:
            if palabra[4] == "-" and palabra[7] == "-" and palabra[0].isdigit() and palabra[1].isdigit() and palabra[2].isdigit() and palabra[3].isdigit() and palabra[5].isdigit() and palabra[6].isdigit() and palabra[8].isdigit() and palabra[9].isdigit():
                if palabra in frecuencia_fechas:
                    frecuencia_fechas[palabra] += 1
                else:
                    frecuencia_fechas[palabra] = 1
            elif palabra[2] == "/" and palabra[5] == "/" and palabra[0].isdigit() and palabra[1].isdigit() and palabra[3].isdigit() and palabra[4].isdigit() and palabra[6].isdigit() and palabra[7].isdigit() and palabra[8].isdigit() and palabra[9].isdigit():
                if palabra in frecuencia_fechas:
                    frecuencia_fechas[palabra] += 1
                else:
                    frecuencia_fechas[palabra] = 1
            elif palabra[2] == "-" and palabra[5] == "-" and palabra[0].isdigit() and palabra[1].isdigit() and palabra[3].isdigit() and palabra[4].isdigit() and palabra[6].isdigit() and palabra[7].isdigit() and palabra[8].isdigit() and palabra[9].isdigit():
                if palabra in frecuencia_fechas:
                    frecuencia_fechas[palabra] += 1
                else:
                    frecuencia_fechas[palabra] = 1

    print("Errores encontrados:")
    for patron, cuenta in errores.items():
        print(f"  {patron}: {cuenta}")

    if frecuencia_fechas:
        print("Fechas encontradas:")
        fechas_items = list(frecuencia_fechas.items())
        n = len(fechas_items)
        for i in range(n):
            for j in range(n - 1):
                if fechas_items[j][1] < fechas_items[j + 1][1]:
                    fechas_items[j], fechas_items[j + 1] = fechas_items[j + 1], fechas_items[j]
        for fecha, cuenta in fechas_items:
            print(f"  {fecha}: {cuenta}")
    else:
        print("No se encontraron fechas con formato conocido.")

def grafico_de_barras(archivo):
    texto = archivo.read()
    palabras = texto.split()
    palabra = ""
    signos = ".,;:!?¡¿"
    for signo in signos:
        texto = texto.replace(signo, " ")
    palabras = texto.split()
    conectores = ["de", "la", "que", "el", "en", "y", "a", "los", "del", "se",
    "las", "por", "un", "para", "con", "no", "una", "su", "al"]
    signos = ".,;:!?¡¿"
    for signo in signos:
        texto = texto.replace(signo, " ")
    frecuencia = {}
    for palabra in palabras:
        if palabra not in conectores:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
    F = frecuencia.items()
    lista = sorted(F)
    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            if lista[j][1] < lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    i = 0 
    while i < len(lista):
        if i == 10:
            break
        i = i + 1
    palabras_10 = [] # se crea lista vacia para las 10 primeras
    frecuencias_10 = [] # lista vacia para las 10 primeras
    for i in range(min(10, len(lista))): # recorre las 10 primeras posiciones
          palabras_10.append(lista[i][0]) # guarda la palabra
          frecuencias_10.append(lista[i][1]) # guarda la frecuencia

    plt.barh(palabras_10, frecuencias_10) #crea grafico de barras horizontales 
    plt.title("Frecuencia de palabras") # titulo de la grafica
    plt.xlabel("Frecuencia") # nombre de eje x
    plt.ylabel("Palabras") # Nombre de eje y
    plt.show()

def histograma (archivo):
    lineas = archivo.readlines() # Lee las lineas del archivo
    longitudes = [] # Lista vacía
    for linea in lineas:
        cantidad = 0
        for caracter in linea:
            if caracter != "\n":
                cantidad += 1
        longitudes.append(cantidad)
    plt.hist(longitudes, [0,50,51,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800])
    plt.title ("Distribución de Longitud de Líneas")
    plt.xlabel ("Cantidad de caracteres")
    plt.ylabel ("Númerod e lineas")
    plt.show()

def archivos_de_texto():
    while True:
        ruta_texto = input("ingrese la ruta del archivo de texto con el que desea trabajar: ")
        ruta = pt.Path(ruta_texto)
        if not ruta.exists():
            print("el archivo no existe en esta ruta")
            continue

        print("¡El archivo existe! Procediendo a leer...")
        with ruta.open("r", encoding="utf-8") as archivo:
            while True:
                print("1) Resumen Estadístico del Texto\n2) Extracción de Patrones(Logs)\n3) Frecuencia de Palabras Clave(Grafico)\n4) Distribución de Longitud de Líneas(Grafico)\n5) Salir")
                opcion = input("elige una opcion numerica: ")
                if opcion == "1":
                    archivo.seek(0)
                    Resumen_Estadístico_del_Texto(archivo)
                elif opcion == "2":
                    archivo.seek(0)
                    archivos_log(archivo)
                elif opcion == "3":
                    archivo.seek(0)
                    grafico_de_barras(archivo)
                elif opcion == "4":
                    archivo.seek(0)
                    histograma(archivo)
                elif opcion == "5":
                    print("saliendo de la seccion de texto...")
                    break
                else:
                    print("ingrese un valor correcto")
            break