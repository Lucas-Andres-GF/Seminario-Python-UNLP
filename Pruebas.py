# import json
# from textwrap import indent
# archivo = open("bandas.json", "w")
# datos = [{"nombre": "William Campbell", "ciudad": "La Plata", "ref": "www.instagram.com/williamcampbellok"},
#         {"nombre": "Buendia", "ciudad": "La Plata", "ref":"https://buendia.bandcamp.com/"},
#         {"nombre": "Lumine", "ciudad": "La Plata", "ref": "https://www.instagram.com/luminelp/"}]
# json.dump(datos, archivo, indent=4)
# archivo.close()

# archivo = open("bandas.json",'r')

# datos_de_las_bandas = json.load(archivo) #Descargo los datos 
# print(datos_de_las_bandas)

# json_de_las_badas = json.dumps(datos_de_las_bandas,indent=4)
# print(json_de_las_badas) #Imprimo en "como" formato JSON

# archivo.close

# from asyncore import write
# import csv 

# import os 

# ruta = os.path.join(os.getcwd(),'netflix_titles.csv')

class Jugador():
    """Define la entidad que representa a un jugador en el juego"""
    #Propiedades
    def __init__(self, nom, nic):
        self.nombre = nom
        self.nick = nic
        self.puntos = 0
    #Métodos
    def incrementar_puntos(self, puntos):
        self.puntos += puntos

tony = Jugador('tony','ironman')
tony.incrementar_puntos(10)
print(tony.nick)
print(tony.nombre)
print(tony.puntos)

peter = Jugador('peter','spiderman')
peter.incrementar_puntos(20)
print(peter.nick)
print(peter.nombre)
print(peter.puntos)
