def calcular_promedio(lista):
    """ Calcula el promedio de los valores dentro de la lista dada como argumento"""
    cant_elementos = len(lista)
    return 0 if cant_elementos == 0 else sum(lista)/cant_elementos