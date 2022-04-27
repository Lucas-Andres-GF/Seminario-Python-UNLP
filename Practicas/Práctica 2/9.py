incognita = ['-*-*-',
             '--*--',
             '----*',
             '*----',]

tablero = [ ]
for x in incognita:
    l = list (x) 
    tablero.append(l)
print(tablero)

linea1 = (tablero[0])

#print(linea1.replace("*",0))

# for x in range(0,5):
#     print(x)
#     if (linea1[x] != "*"):
#         linea1[x] = 1
# print(linea1)
