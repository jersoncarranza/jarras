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
		self.LJ1=0 #litros de agua que tiene el jarro1
		self.LJ2=0 #litros de agua que tiene el jarro2
		
		self.AJ1=None #Auxiliar Jarro 1
		self.AJ2=None #Auxiliar Jarro 2
		self.AMet = None #Auxiliar para la meta

	#variables
	def variables():
		self.LJ1=0
		self.LJ2=0


	def vacia(self):
		if self.cabeza==None:
			return True
		else:
			return False

	def Insertar(self,J1,J2,Meta):
		self.LJ1= J1
		self.LJ2= J2
		self.AMet = Meta
		temporal=Nodo(self.LJ1, self.LJ2, self.AMet)

		if self.vacia()==True:
			self.cabeza=temporal
			self.cola=temporal
		else:
			temporal.siguiente=self.cabeza
			self.cabeza.anterior=temporal
			self.cabeza=temporal

	def listar(self):
		print("*****Listar*****")
		temporal=self.cabeza
		while temporal != None:
			print(temporal.verNodo())
			temporal= temporal.siguiente

	def listarDesdeCola(self):
		print("****Listar*****")
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
		print "Litros agua jarra 1 es :", self.LJ1
		print "Litros agua jarra 2 es :", self.LJ2
		self.Evento1()
		#if self.LJ1>0 and self.LJ2 < J2:
		#	print "Aqui"
			#LJ1 is LJ1 -1
			#LJ2 is LJ2 + 1
			#J1aJ2()
	
	#Utilizar los auxiliares
	def UtiAux(self,J1,J2,Meta):
		print "vamos a salvar valores"
		self.AJ1= J1
		self.AJ2= J2
		self.AMet = Meta

		#Genera el primer estado 
		self.Insertar(0,0,self.AMet)

	#Evento 1 llenar jarro 1
	def Evento1(self):
		self.LJ1 = self.AJ1
		print "******El jarro 1 tiene", self.AJ1, "Litros."
		self.Insertar(self.LJ1, self.LJ2, self.AMet)

	#Evento 2 llenar jarro 2
	def Evento2(self):
		self.LJ2 = self.AJ2
		print "******El jarro 2 tiene", self.AJ2, "Litros."
		self.Insertar(self.LJ1, self.LJ2, self.AMet)
		
	#Evento 3 pasar agua del jarro2 al jarro1
	def Evento3(self):
		print "LJ1 es ",self.LJ1
		print "AJ1 es ",self.AJ1
		print "LJ2 es ",self.LJ2
		if self.LJ2>0 and self.LJ1 < self.AJ1:
			self.LJ2 = self.LJ2 -1
			self.LJ1 = self.LJ1 + 1
			self.Evento3()
		else:
			self.Insertar(self.LJ1, self.LJ2, self.AMet)

	#Evento 5 vaciar el jarro 1
	def Evento5(self):

		self.LJ1=0
		self.Insertar(self.LJ1, self.LJ2, self.AMet)

	#nos dice si llego a la meta
	def FunMeta(self,Meta):
		if self.LJ1+self.LJ2 == Meta:
			return True
		else:
			return False
	#nos regresa un nuevo estado
	def CrearEstado(self):
		self.Evento1()#que llene de jarro 1
		#if self.FunMeta(self.AMet) == False:
		#	self.Evento2()#que llene el jarro2
		#else:
		#	print "llego a la meta"
		self.Evento2()
		self.Evento5()
		self.Evento3()

listas = Lista()
ja1 = 5 # capacidad que tiene  el jarro 1
ja2 = 3 # capacidad que tiene  el jarro 2
meta = 5 #meta litros agua

listas.UtiAux(ja1,ja2,meta)
#listas.Insertar(ja1,ja2,meta)

if True == listas.FunMeta(meta):
	print ("llego a la meta.. ya no haga mas hijos")
else:
	listas.CrearEstado()
listas.listarDesdeCola()
#listas.Nuevo()

