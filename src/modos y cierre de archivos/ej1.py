archivo = open("C:\\Users\\B09S202est\\Documents\\Programacion deybid2026\\prog-2610-unidad5-deybid150\\actividades\\texto_generico.txt", "r", encoding="utf-8")
P = archivo.readlines()
for i in P:
    print(i[0])
