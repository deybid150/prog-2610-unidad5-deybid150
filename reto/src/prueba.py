with open("C:\\Users\\B15S201est\\Documents\\progdbd20261\\prog-2610-unidad5-deybid150\\actividades\\texto_generico.txt", "r", encoding="utf-8") as archivo:
    signos = ".,;:!?¡¿"
    conectores = ["de", "la", "que", "el", "en", "y", "a", "los", "del", "se",
    "las", "por", "un", "para", "con", "no", "una", "su", "al"]
    contenido = archivo.read()
    for signo in signos:
        texto = contenido.replace(signo, " ")
    texto = texto.lower()
    palabras = texto.split()
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
        j = 0
        while j < n - 1:
            if lista[j][1] < lista[j + 1][1]:
                t = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = t

            j = j + 1
        i = i + 1
    i = 0
    while i < len(lista):
        if i == 5:
            break
    print(lista[i][0], lista[i][1])

    i = i + 1

    print(f"{contenido}\n {palabras}\n {F}\n {lista}")