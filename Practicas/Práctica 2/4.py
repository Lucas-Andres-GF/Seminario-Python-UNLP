from cgitb import reset
from operator import le

evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

partes = evaluar.split(":")
titulo = partes[1].split("titulo")
titulo = titulo[0].split("resumen")
oraciones = partes[2].split(".")
palabras_titulo = titulo[0].split()
# print(oraciones)
# print(palabras_titulo)

if (oraciones[len(oraciones)-1] == ""):
    oraciones.pop(len(oraciones)-1)

if (len(palabras_titulo) <= 10):
    print(". titulo está ok")
else: 
    print(". titulo está pasado de palabras")
    print(len(palabras_titulo))

#print(oraciones)
#print ("cantidad de oraciones ",len(oraciones))

easy,agree,hard,very_hard = 0,0,0,0

for oracion in oraciones:
    oracion = oracion.split()
    #print ("Palabras: ",len(oracion))
    if (len(oracion) <= 12):
        easy += 1
    elif (len(oracion) <= 17):
        agree += 1
    elif (len(oracion) <= 25):
        hard += 1
    else:
        very_hard += 1
    
print(f". Cantidad de oraciones fáciles de leer:{easy}, aceptables para leer:{agree}, dificil de leer:{hard}, muy dificil de leer:{very_hard}")




