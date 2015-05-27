class Arbol:
	def __init__(self,valor):
		self.valor = valor
		self.evento1 = None
		self.evento2 = None
		self.evento3 = None
		self.bandera = 0 #Bandera para que busque


#Metodo para agregar nodos a la evento1 del arbol, no importando que nodo
#del arbol queremos como padre de este
	def AgregaEvento1(self,padre,dato):
		if self.valor != padre:
			if self.evento1 !=None:
				self.evento1.AgregaEvento1(padre,dato)
			if self.evento2 !=None:
				self.evento2.AgregaEvento1(padre,dato)
			if self.evento3 !=None:
				self.evento3.AgregaEvento1(padre,dato)
		else: 
			self.evento1=Arbol(dato)
#Metodo para agregar nodos a la evento2, no importando que nodo del arbol
#queremos como padre de este
	def AgregaEvento2(self,padre,dato):
		if self.valor != padre:
			if self.evento1 != None:
				self.evento1.AgregaEvento2(padre,dato)
			if self.evento2!=None:
				self.evento2.AgregaEvento2(padre,dato)
			if self.evento3 !=None:
				self.evento3.AgregaEvento2(padre,dato)
		else: 
			self.evento2 = Arbol(dato)

	# Puntero 3
	def AgregaEvento3(self,padre,dato):
		if self.valor != padre:
			if self.evento1 != None:
				self.evento1.AgregaEvento3(padre,dato)
			if self.evento2!=None:
				self.evento2.AgregaEvento3(padre,dato)
			if self.evento3 !=None:
				self.evento3.AgregaEvento3(padre,dato)
		else: 
			self.evento3 = Arbol(dato)
	#Metodo que nos permite buscar un elemento en forma recursiva
	def BuscaNodo(self,dato):
		dato= 35
		print "valorrrr", self.valor
		if self.valor == dato:
			print "ya encontro"
			return self.valor
		else:
			if self.evento1 !=None:
				return self.evento1.BuscaNodo(dato)

			if self.evento2!=None:
				print "entro al evento2", self.valor
				return self.evento2.BuscaNodo(dato)

			if self.evento3!=None:
				print "....", self.valor
				return self.evento3.BuscaNodo(dato)
			
#Metodo para impresion del arbol comenzando Primero evento1 usando recursividad
	def ImprimeEvento1(self):
		if self.valor!=None:
			print self.valor
			if self.evento1!=None:
				self.evento1.ImprimeEvento1()
			if self.evento2!=None:
				self.evento2.ImprimeEvento1()
			if self.evento3!=None:
				self.evento3.ImprimeEvento1()
#Metodo para impresion del arbol comenzando primero por la evento2 usando recursividad
	def ImprimeEvento2(self):
		if self.valor!=None:
			print self.valor
			if self.evento2!=None:
				self.evento2.ImprimeEvento2()
			if self.evento1!=None:
				self.evento1.ImprimeEvento2()
			if self.evento3!=None:
				self.evento3.ImprimeEvento2()

	def ImprimeEvento3(self):
		if self.valor!=None:
			print self.valor
			if self.evento3!=None:
				self.evento3.ImprimeEvento3()
			if self.evento2!=None:
				self.evento2.ImprimeEvento3()
			if self.evento1!=None:
				self.evento1.ImprimeEvento3()

arbol= Arbol(9)
#arbol.AgregaEvento1(9,23)
arbol.AgregaEvento1(9,35)
arbol.AgregaEvento2(9,28)
arbol.AgregaEvento3(9,19)

#print 'Impresion del arbol comenzando por la evento1'
#arbol.ImprimeEvento1()

arbol.ImprimeEvento3()

vb = 35
#print 'Buscando un valor',vb
valor = arbol.BuscaNodo(vb)
print  valor
