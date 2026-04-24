from random import randint

lista = []
for i in range(50):
    lista.append(randint(0, 100))

maximo = str(max(lista))
minimo = str(min(lista))
prom = str(sum(lista)/len(lista))

file_datos = open("C:\\Users\\B09S202est\\Documents\\Programacion deybid2026\\prog-2610-unidad5-deybid150\\actividades\\datos.txt", "a", encoding="utf-8")
file_datos.write("El valor máximo es: " + maximo + "\nEl valor mínimo es: " + minimo + "\nEl promedio es: " + prom + "\n")
file_datos.close()
print("Archivo creado con éxito. Revisa tu carpeta.")