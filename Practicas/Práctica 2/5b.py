cadena = input("""Ingresa la clave (debe tener menos de 10 caracteres y 
no ↪→contener los símbolos:@ y !):""")
if (len(cadena)<10): 
   if not('@'in cadena) and not('!'in cadena):
      print("Clave válida")
   else:
      print("Ingresaste alguno de estos símbolos: @ o !" )
else: 
   print ("La cadena supera los 10 caracteres")
   

# cadena = input("""Ingresa la clave (debe tener menos de 10 caracteres y no␣
#                ↪→contener los símbolos:@ y !):""")
# if len(cadena) > 10:
#    print("Ingresaste más de 10 carcateres")
# cant = 0
# for car in cadena:
#    if car == "@" or car == "!":
#       cant = cant + 1
# if cant >= 1:
#    print("Ingresaste alguno de estos símbolos: @ o !" )
# else:
#    print("Clave válida")

