frase = """Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban
trigo tres tristes tigres."""

palabras = frase.lower().replace("."," ").replace(",", " ").split() 

palabra = input("Ingrese su palabra: ")
palabra_min = palabra.lower()
cant = 0

for p in palabras: 
    if (palabra_min == p): 
        cant += 1

print ("Para la frase: ", frase)
print ("Palabra: ", palabra)
print ("Resultado: ", cant)

