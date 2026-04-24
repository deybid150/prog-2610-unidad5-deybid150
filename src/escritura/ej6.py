nombre_archivo = input("Nombra tu nuevo archivo (ej: diario.txt): ")

# Contexto de escritura
with open("C:\\Users\\B09S202est\\Documents\\Programacion deybid2026\\prog-2610-unidad5-deybid150\\actividades\\"+nombre_archivo, 'w+') as archivo:
    datos = input("Escribe tu primer secreto: ")
    archivo.write(datos)
    archivo.seek(0)
    print("\n--- Leyendo tu archivo ---")
    print(archivo.read())