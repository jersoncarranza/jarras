class Arbol:

	def __init__(self,arbol,dato):
		self.derecha=None
		self.izquierda=None
		self.info =dato

	def agregar(self,arbol,dato):
		if arbol.info > dato:
			self.agregarIzquierda(arbol,dato)
		elif arbol.info < dato:
			self.agregarDerecha(arbol, dato)

	def agregarIzquierda(self, arbol,dato):
		if arbol.izquierda==None:
			arbol.izquierda=Arbol(arbol)
		else:
			self.agregar(arbol.izquierda, dato)

	def agregarDerecha(self, arbol, dato):
		if arbol.derecha == None:
			arbol.derecha= Arbol(arbol,dato)
		else:
			self.agregar(arbol.derecha, dato)

	def preOrden(self, arbol):
		print arbol.info
		if arbol.izquierda != None:
			self.preoIzquierda(arbol)
		if

		
		