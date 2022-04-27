from fileinput import close


r_numpy = open ("readme_numpy.txt","r", encoding="utf-8")
archivo = r_numpy.read().split("\n")

for linea in archivo:
    if ("http" in linea):
        print("Linea - ",linea)
    

