import pathlib as pt

def explorar_directorio():
    ruta_directorio = input("ingrese la ruta del directorio a explorar: ")
    ruta = pt.Path(ruta_directorio)
    if not ruta.exists() or not ruta.is_dir():
        print("La ruta no existe o no es un directorio.")
        return

    archivos = []
    for item in ruta.iterdir():
        if item.is_file() and item.suffix.lower() in {".txt", ".csv"}:
            archivos.append(item.name)

    if archivos:
        print("Archivos .txt y .csv encontrados:")
        for nombre in sorted(archivos):
            print(f" - {nombre}")
    else:
        print("No se encontraron archivos .txt ni .csv en ese directorio.")