archivo = open("C:\\Users\\B09S202est\\Documents\\Programacion deybid2026\\prog-2610-unidad5-deybid150\\actividades\\modo a", "a")
texto = input("ingresa una frase: "), edad = int(input("ingrese su edad: ")), estatura = float(input("ingrese su estatura en metros: "))
archivo.write(f"nueva entrada de registro\n Texto: {texto}\nEdad: {str(edad)}\nEstatura: {str(estatura)}")
archivo.close()