from typing import Callable

def obtener_nombres (archivo)-> list[str]:
    name = archivo.read().replace(",","").replace("'","").replace(" ","").split()
    archivo.close()
    return name

def obtener_notas (archivo)-> list[str]:
    name = archivo.read().replace(","," ").replace("\n"," ").strip().split()
    archivo.close()
    return name

def procesar_archivo (ruta: str,funcion:Callable):
    archivo = open(ruta,"r",encoding="utf-8")
    resultado = funcion(archivo)
    archivo.close()
    return resultado

def promedio (alumnos:dict)-> float:
    suma = 0
    for x in alumnos:
        suma += alumnos [x]
    prom = (suma / len(alumnos))
    return prom

def no_superan (alumnos:dict): 
    prom = promedio(alumnos)
    print(f"El promedio general es: {prom:.2f}")
    print ("Alumnos que no superan el promedio:")
    for a in alumnos:
        if (alumnos[a] < prom ):
            print(f"-{a}-") 

nombres = procesar_archivo("nombres_1.txt",obtener_nombres) 

notas_1 = procesar_archivo("eval1.txt",obtener_notas)    

notas_2 = procesar_archivo("eval2.txt",obtener_notas)    

alumnos = {}
for nombre, n1,n2 in zip(nombres,notas_1,notas_2):
    alumnos[nombre] = int (n1) + int(n2)

print("Alumnos")
for nombre,nota in alumnos.items():
    print(f"{nombre} - nota: {nota} ")
    
#print (f"El promedio es {promedio(alumnos):.2f}") #Obtener unicamente el promedio
no_superan(alumnos)

