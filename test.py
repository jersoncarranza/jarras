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
		self.LJ1=0
		self.LJ2=0
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
	#pasar agua del jarro1 al jarro2
	def J1aJ2(self):
		print "poraqui", self.LJ2
		print "poraqui", self.LJ1
		self.nuevo()
		#if self.LJ1>0 and self.LJ2 < J2:
		#	print "Aqui"
			#LJ1 is LJ1 -1
			#LJ2 is LJ2 + 1
			#J1aJ2()
	#pasar agua del jarro2 al jarro1
	def J2aJ1():
		if self.LJ2>0 and self.LJ1 < self.J1:
			LJ2 is LJ2 -1
			LJ1 is LJ1 + 1
			J2aJ1()
	#nuecos estados
	def Nuevo(self):
		print ("llego aca")
		if self.LJ1 == 0 :
			self.LJ1 is J1
			#print ("tiene 0")
		else:
			print ("estaba lleno el jarro 1")
	#nos dice si llego a la meta
	def FunMeta(self,Meta):
		if self.LJ1+self.LJ2 == Meta:
			return True
		else:
			return False
	#nos regresa un nuevo estado
	def estado(self):
		self.J1aJ2()#que llene de jarro 1 a jarro 2
		
listas = Lista()
ja1 = 5 # capacidad que tiene  el jarro 1
ja2 = 3 # capacidad que tiene  el jarro 2
meta = 1 #metalitros agua
listas.InsertarPrimero(ja1,ja2,meta)
listas.listarDesdeCola()
if True == listas.FunMeta(meta):
	print ("llego a la meta")
else:
	listas.estado()
#listas.Nuevo()

