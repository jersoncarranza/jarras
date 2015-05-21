class Nodo:
	def __init__ (self,J1,J2,Meta):
		self.siguiente = None
		self.anterior = None
		#self.info=J1
		self.datos = [J1,J2,Meta]

	def verNodo(self):
		return self.datos


class Lista:

	def __init__(self):
		self.cabeza=None
		self.cola=None
		self.LJ1=None
		self.LJ2=None
	#variables
	def variables():
		self.LJ1=0
		self.LJ2=0


	def vacia(self):
		if self.cabeza==None:
			return True
		else:
			return False

	def InsertarPrimero(self,J1,J2,Meta):
		temporal=Nodo(J1,J2,Meta)
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
	#nos dice si llego a la meta
	def FunMeta():
		if LJ1+LJ2 == self.Meta:
			return True
		else:
			return False
	#pasar agua del jarro1 al jarro2
	def J1aJ2():
		if self.LJ1>0 and self.LJ2 < self.J2:
			LJ1 is LJ1 -1
			LJ2 is LJ2 + 1
			J1aJ2()
	#pasar agua del jarro2 al jarro1
	def J2aJ1():
		if self.LJ2>0 and self.LJ1 < self.J1:
			LJ2 is LJ2 -1
			LJ1 is LJ1 + 1
			J2aJ1()
	#nuecos estados
	def Nuevo(self):
		if self.LJ1 == 0 :
			self.LJ1 is self.J1
			print ("se lleno el jarro 1")
		else:
			print ("esta estab lleno el jarro 1")

		


listas = Lista()
listas.LJ1 is 0
listas.InsertarPrimero(5,3,5)
listas.listarDesdeCola()
#if(True == listas.FunMeta):
#	print ("se lleno")
#else:
#	print ("no se lleno")
listas.Nuevo()

