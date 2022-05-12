import csv
import os

ruta_csv = os.path.join(os.getcwd(),'BBB_nuevo.csv')
usuarios = set() #Guardaremos los uruarios en un set, para no obtener repetidos
with open (ruta_csv,'r',encoding='utf-8') as dataset: 
    reader = csv.reader (dataset,delimiter=','); 
    reader.__next__ #Salteamos el encabezado 
    for linea in reader :
        if ('6/04/2022' in linea[0]) and ('Grabación vista' in linea[2]):
            usuarios.add(linea[1])

ruta_archivo_usuarios = os.path.join(os.getcwd(),'asistencia_abril6.txt')
with open (ruta_archivo_usuarios,'x') as archivo_usuarios:
    archivo_usuarios.write('-Asistencia del dia 6 de abril- \n')
    for user in usuarios: 
        archivo_usuarios.write(user + '\n')
