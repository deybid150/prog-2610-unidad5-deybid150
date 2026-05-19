import codigo_texto
import case1
import codigo_csv
e = True
while e == True:
    print("1) Explorar directorio\n2) Procesar Bitácoras / Textos Reales (.txt)\n3) Analizar Dataset de Datos Abiertos (.csv)\n4) Salir del programa")
    O = int(input("ingresa una opcion numericamente: "))
    match O:
        case 1:
            case1.explorar_directorio()
        case 2:
            codigo_texto.archivos_de_texto()
        case 3:
            codigo_csv.archivos_csv()
        case 4:
            print("saliendo del programa...")
            e = False
        case _:
            print("ingrese un valor correcto")