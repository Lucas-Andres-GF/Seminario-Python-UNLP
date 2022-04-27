frase = input("Ingrese una frase para verificar: ").lower().replace(" ","")

if (len(frase) == len(set(frase))):
    print ("La palabra/frase/oracion es heterograma")
else:
    print("La palabra/frase/oracion no es heterograma")

# def informar (x:int):
#     return x<=1

# cants = Counter(list(frase))

# if (len(list(filter(informar, cants.values()))) == len(cants.values())):
#     print ("La palabra/frase/oracion es heterograma")
# else:
#     print("La palabra/frase/oracion no es heterograma")
