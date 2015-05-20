class Nodo:
	def __init__ (self,J1):
		self.siguiente = None
		self.anterior = None
		#self.info=J1
		self.datos = [J1]

	def verNodo(self):
		return self.datos


class Lista:
	def __init__(self):
		self.cabeza=None
		self.cola=None

	def vacia(self):
		if self.cabeza==None:
			return True
		else:
			return False

	def InsertarPrimero(self,J1):
		temporal=Nodo(J1)
		if self.vacia()==True:
			self.cabeza=temporal
			self.cola=temporal
		else:
			temporal.siguiente=self.cabeza
			self.cabeza.anterior=temporal
			self.cabeza=temporal

	def listar(self):
		print("**********")
		temporal=self.cabeza
		while temporal != None:
			print(temporal.verNodo())
			temporal= temporal.siguiente

	def listarDesdeCola(self):
		print("*********")
		temporal=self.cola
		while temporal != None:
			print(temporal.verNodo())
			temporal = temporal.anterior

	def borrarPrimero(self):
		if self.vacia()==False:
			self.cabeza=self.cabeza.siguiente
			self.cabeza.anterior=None

	def borrarUltimo(self):
		if self.cola.anterior==None:
			self.cabeza = None
			self.cola = None
		else:
			self.cola=self.cola.anterior
			self.cola.siguiente=None

listas = Lista()
listas.InsertarPrimero(1)
listas.InsertarPrimero(2)
listas.InsertarPrimero(3)
listas.InsertarPrimero(4)
listas.listarDesdeCola()

