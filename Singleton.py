class minombre ():

	__instancia = None
	nombre = None

	def __str__(self):
		return self.nombre

	def __new__(cls):
		if minombre.__instancia is None:
			minombre.__instancia = object.__new__(cls)
		return minombre.__instancia

nombre1 = minombre()
nombre1.nombre= "christian Ramirez"
print (nombre1)

nombre2 = minombre()
nombre2.nombre= "Pablo Escobar"
print (nombre2)
print (nombre1)
