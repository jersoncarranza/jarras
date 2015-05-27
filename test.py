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
		
		self.CJ1=None #capacidad Jarro 1
		self.CJ2=None #capacidad Jarro 2
		self.AMet = None #cpara la meta

		self.EJ1 = None #estado1
		self.EJ2 = None #estado2


	def vacia(self):
		if self.cabeza==None:
			return True
		else:
			return False

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
	
	#Utilizar los auxiliares
	def PrimerInsertar(self,J1,J2,Meta):
		print "vamos a salvar valores"
		self.CJ1= J1
		self.CJ2= J2
		self.AMet = Meta
		#Genera el primer estado 
		self.Insertar(0,0,self.AMet)

	def Insertar(self,J1,J2,Meta):
		self.LJ1= J1
		self.LJ2= J2
		self.AMet = Meta
		temporal=Nodo(self.LJ1, self.LJ2, self.AMet)

		if self.vacia()==True:
			self.cabeza=temporal
			self.cola=temporal
		else:
			self.cabeza.siguiente=temporal
			temporal.anterior=self.cabeza
			temporal=self.cabeza
			#temporal.siguiente=self.cabeza
			#self.cabeza.anterior=temporal
			#self.cabeza=temporal

		temporal=self.cola
		a = temporal.verNodo()
		print (a[0])
		#print(lista1[1])
	#Evento 1 llenar jarro 1
	def Evento1(self):
		self.LJ1 = self.CJ1
		self.Insertar(self.LJ1, self.LJ2, self.AMet)

	#Evento 2 llenar jarro 2
	def Evento2(self):
		self.LJ2 = self.CJ2
		self.Insertar(self.LJ1, self.LJ2, self.AMet)
		
	#Evento 3 pasar agua del jarro2 al jarro1
	def Evento3(self):
		if self.LJ2>0 and self.LJ1 < self.CJ1:
			self.LJ2 = self.LJ2 -1
			self.LJ1 = self.LJ1 + 1
			self.Evento3()
		else:
			self.Insertar(self.LJ1, self.LJ2, self.AMet)

	#Evento 4 pasar agua del jarro1 al jarro2
	def Evento4(self):
		if self.LJ1>0 and self.LJ2 < self.CJ2:
			self.LJ1 = self.LJ1 - 1
			self.LJ2 = self.LJ2 + 1
			self.Evento4()
		else:
			self.Insertar(self.LJ1, self.LJ2, self.AMet)
	
	#Evento 5 vaciar el jarro 1
	def Evento5(self):
		self.LJ1=0
		self.Insertar(self.LJ1, self.LJ2, self.AMet)

	#Evento 6 vaciar el jarro 2
	def Evento6(self):
		self.LJ2=0
		self.Insertar(self.LJ1, self.LJ2, self.AMet)

	#nos dice si llego a la meta
	def FunMeta(self,Meta):
		if self.LJ1+self.LJ2 == Meta:
			return True
		else:
			return False
	#nos regresa un nuevo estado
	def CrearEstado(self):
		self.Evento2()
		self.Evento3()
		self.Evento2()
		self.Evento3()
		self.Evento5()
		self.Evento3()
		self.Evento2()
		self.Evento3()
		self.Evento2()


listas = Lista()
ja1 = 5 # capacidad que tiene  el jarro 1
ja2 = 3 # capacidad que tiene  el jarro 2
meta= 7 #meta litros agua

listas.PrimerInsertar(ja1,ja2,meta)
#listas.Insertar(ja1,ja2,meta)

if True == listas.FunMeta(meta):
	print ("llego a la meta.. ya no haga mas hijos")
else:
	listas.CrearEstado()
listas.listar()
#listas.Nuevo()

