e = True
while e == True:
    try: 
        valor = float(input("ingrese un valor numerico: "))
    except (ValueError, ZeroDivisionError):
            print("Error: ingrese un numero.")
    else:
        resultado = valor/10
        print(f"resultado = {resultado}")
    finally:
         print("proceso ejecutado")