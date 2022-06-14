#Dada la clase Pila definida en el módulo estructuras, indicá si el código del archivo test1.py es correcto o no. Describí detalladamente qué hace y en caso de tener un error, corregirlo.

import unittest
from estructuras import Pila


class TestPila(unittest.TestCase):

   def test_pila__recien_creada(self):
       print('Esto es un test') 
       pila = Pila()
       pila.apilar(1)
       self.assertTrue(pila.es_vacia())


if __name__ == '__main__':
   unittest.main()
