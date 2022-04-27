import string

texto = "Lo mismo le dije yo a Lucas Lauriente"
letra = input("Ingrese una letra: ")
if (letra in string.ascii_letters ):
    palabras = texto.split()
    for p in palabras : 
        if ((p.upper().startswith(letra))or(p.lower().startswith(letra))):
            print (p)
else:
    print("ERROR - No ha ingresado una letra")

