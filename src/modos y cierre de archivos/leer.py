fp = open("C:\\Users\\B09S202est\\Documents\\Programacion deybid2026\\prog-2610-unidad5-deybid150\\actividades\\ejercicio1.txt", "r", encoding="utf-8")
datos_1 = fp.readlines()
print("Primera lectura:", datos_1)

datos_2 = fp.read(5)
print("Segunda lectura:", datos_2)

datos_3 = fp.read()
print("Tercera lectura:", datos_3)
fp.close()