import collections 
from collections import Counter

r_numpy = open("readme_numpy.txt","r")

palabras = (r_numpy.read().split())

cant_palabras = Counter(palabras)

print ("La palabra/carecter que mas veces aparece es: ", cant_palabras.most_common(1))

solo_palabras = Counter(filter(lambda  palabra: palabra.isalpha(), palabras))

#print (f"{solo_palabras.most_common(1) = }") 

print ("La palabra que mas veces aprece es: " , solo_palabras.most_common(1))

#print ( Counter(filter(lambda palabra: palabra.isalpha(), palabras )).most_common(1))


