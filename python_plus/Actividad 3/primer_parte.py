#Explicá detalladamente qué hace este código y por qué da error al ejecutarlo. Proponé una mínima modificación para que funcione correctamente.


class Persona:
	def __init__(self, nom, ape, doc, fech):
		self._nombre = nom
		self._apellido = ape
		self._dni = doc
		self._fecha_nac = fech
		
	def __str__(self):
		return  f'{self._nombre} {self._apellido} con documento: {self._dni}'
		
class Becario:
	def __init__(self,  cat_beca = 'A', tip ='Extensión'): 
		self._categoria_beca = cat_beca
		self._tipo_beca = tip
		
	def __str__(self): 
		return (f' Beca de tipo {self._tipo_beca} con la categoría: {self._categoria_beca} ' )
		
	def cambio_nombre(self, dato_nuevo): 
		self._tipo_beca = dato_nuevo		
	
class Estudiante(Persona, Becario):
    def __init__(self, nro_lega, car, nombre, apellido, documento, fecha): 
        super().__init__(nombre, apellido, documento,fecha)
        Becario.__init__(self)
        self.nro_legajo = nro_lega
        self.carrera = car
		
    def __str__(self): 
        return (super().__str__() + ' con beca ' + Becario.__str__(self))
	
	
estudiante_nuevo = Estudiante('123/8','licenciado en Comunicación', 'Rocío', 'Gomez', 34555999,'15/7/89')
resp = input ('Desea cambiar el tipo de beca del/de la estudiante (S/N): ').upper()
if resp == 'S':
	estudiante_nuevo.cambio_nombre(input('Ingrese tipo de beca nueva: '))

print (estudiante_nuevo)


