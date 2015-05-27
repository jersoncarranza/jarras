class Arbol:

	def __init__(self,valor):
		self.valor = valor
		self.izquierda = None
		self.derecha = None

#Metodo para agregar nodos a la izquierda del arbol, no importando que nodo
#del arbol queremos como padre de este
	def AgregaIzquierda(self,padre,dato):
		if self.valor != padre:
			if self.izquierda != None:
				self.izquierda.AgregaIzquierda(padre,dato)
			if self.derecha!=None:
				self.derecha.AgregaIzquierda(padre,dato)
		else: 
			self.izquierda=Arbol(dato)
#Metodo para agregar nodos a la derecha, no importando que nodo del arbol
#queremos como padre de este
	def AgregaDerecha(self,padre,dato):
		if self.valor != padre:
			if self.izquierda != None:
				self.izquierda.AgregaDerecha(padre,dato)
			if self.derecha!=None:
				self.derecha.AgregaDerecha(padre,dato)
		else: 
			self.derecha = Arbol(dato)
	#Metodo que nos permite buscar un elemento en forma recursiva
	def BuscaNodo(self,dato):
		if self.valor != dato:
			if self.izquierda!=None:
				return self.izquierda.BuscaNodo(dato)
			if self.derecha!=None:
				return self.derecha.BuscaNodo(dato)
		else:
			return self.valor

	#Metodo que nos permite buscar un elemento en forma recursiva
	def BuscaNodoD(self,dato):
		if self.valor != dato:
			if self.derecha!=None:
				return self.derecha.BuscaNodoD(dato)
			if self.izquierda!=None:
				return self.izquierda.BuscaNodoD(dato)
		else:
			return self.valor


	#Metodo para impresion del arbol comenzando Primero Izquierda usando recursividad
	def ImprimeArbolIzq(self):
		if self.valor!=None:
			print self.valor
		if self.izquierda!=None:
			self.izquierda.ImprimeArbolIzq()
		if self.derecha!=None:
			self.derecha.ImprimeArbolIzq()
#Metodo para impresion del arbol comenzando primero por la derecha usando recursividad
	def ImprimeArbolDer(self):
		if self.valor!=None:
			print self.valor
		if self.derecha!=None:
			self.derecha.ImprimeArbolDer()
		if self.izquierda!=None:
			self.izquierda.ImprimeArbolDer()

arbol= Arbol(9)
# AgregaIzquierda(padre,dato)
arbol.AgregaIzquierda(9,23)

arbol.AgregaIzquierda(23,230)

arbol.AgregaIzquierda(230,830)
arbol.AgregaDerecha(230,431)





print
print 'Impresion del arbol comenzando por la izquierda'
arbol.ImprimeArbolIzq()
print
print
print 'Impresion del arbol comenzando por la derecha'
arbol.ImprimeArbolDer()

print 'Buscando un valor' 
valor = arbol.BuscaNodo(431)
print valor
print
