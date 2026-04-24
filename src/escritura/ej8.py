from pathlib import Path

archivo_buscado = Path("actividades\\archivo.txt")

if archivo_buscado.exists():
    print("¡El archivo existe! Procediendo a leer...")
    with open(archivo_buscado, "r") as f:
        print(f.read())
else:
    print("Lo siento, el archivo no se encuentra en esa ruta.")