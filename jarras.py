class Arbol:
	def __init__(self,dato):
		raiz = []
		Cj1 = 5 #capacidad de jarro1
		Cj2 = 2 #capacidad de jarro2
		Lj1 = 0 #litros que tiene de jarro1
		Lj2 = 0 #litros que tiene de jarro2
		self.dato=dato
		self.derecha=None
	
	def CondEspa(self):
		res = false
		if (Lj1 <= Cj1 and Lj2 <= Cj2):
			res = true
		print self.res

	#def Insertar(self,dato):


	def hola(self,dato):
		print 'hola mundo'


		

def main():
	#radio=raw_input("Dame el radio")
	arbol= Arbol(9)
	arbol.hola()
	#arbol.Insertar(5)
main()