

def Resumen_Estadístico_del_Texto(archivo):
    contenido = archivo.read()
    texto = contenido.lower()
    lineas = archivo.readlines()
    c_lineas = len(lineas)
    palabras = texto.split()
    c_palabras = len(palabras)
    print(f"la cantidad de lineas es {c_lineas}\nLa cantidad de palabras es {c_palabras}\n")
    conectores = ["de", "la", "que", "el", "en", "y", "a", "los", "del", "se",
    "las", "por", "un", "para", "con", "no", "una", "su", "al"]
    signos = ".,;:!?¡¿"
    for signo in signos:
        texto = archivo.replace(signo, " ")
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
    i = 0
    while i < n:
        i += 1
        j = 0
        while j < (n - 1):
            j += 1
            if lista[j][1] < lista[j + 1][1]:
                t = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = t
    i = 0 
    while i < len(lista):
        if i == 5:
            break
    print(lista[i][0], lista[i][1])
    i = i + 1

def archivos_log(archivo):
    pass
def archivos_de_texto():
    a = True
    while a == True:
        ruta = input("ingrese la ruta del archivo de texto con el que desea trabajar: ") 
        if ruta.exists():
            print("¡El archivo existe! Procediendo a leer...")
            with open(ruta, "r", encoding="utf-8") as archivo:
                print("1) Resumen Estadístico del Texto\n2) Extracción de Patrones(Logs)\n3) Frecuencia de Palabras Clave(Grafico)\n4) Distribución de Longitud de Líneas(Grafico)\n5) Salir")
                t = int(input("elige una opcion numerica: "))
                match t:
                    case 1:
                        Resumen_Estadístico_del_Texto(archivo)
                    case 2:
                        archivos_log(archivo)
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        print("saliendo de la seccion de texto...")
                        a = False
                    case _:
                        print("ingrese un valor correcto")
        else:
            print("el archivo no existe en esta ruta")