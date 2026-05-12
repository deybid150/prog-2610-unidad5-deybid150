

def Resumen_Estadístico_del_Texto(archivo):
    contenido = archivo.read()
    texto = contenido.lower()
    lineas = archivo.readlines()
    c_lineas = len(lineas)
    palabras = texto.split()
    c_palabras = len(palabras)
    signos = ".,;:!?¡¿"
    for signo in signos:
        texto = archivo.replace(signo, " ")
    frecuencias = {}
    for palabra in palabras:
        
    
    print(f"la cantidad de lineas es {c_lineas}\nLa cantidad de palabras es {c_palabras}\n")


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
                        pass
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