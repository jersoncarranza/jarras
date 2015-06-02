class Arbol:
    def __init__ (self, J1, J2, Meta):
        self.siguiente = None
        self.anterior = None
        self.raiz = [J1,J2,Meta]

    def Raiz(self):
        return self.raiz

    def crearArbol(self):
        J1= self.raiz[0]
        J2= self.raiz[1]
        Meta= self.raiz[2]
        
        NA=NodoArbol(J1,J2,Meta)
        NA.crearHijos()

    def solucion():
        Li=Lista(J1,J2,Meta)
        Li.listarSolucion()

class NodoArbol:
    def __init__ (self,J1,J2,Meta):
        self.siguiente = None
        self.anterior = None
        self.ptrPadre = None
        self.datos = [J1,J2,Meta]

    def verNodo(self):
        return self.datos


    def crearHijos(self):
        print "Los datos NodoArbol:", self.datos
        Li=Lista(J1,J2,Meta)
        Li.CrearEstado()
        #Li.listar()


class Lista:
    def __init__(self,J1,J2,Meta):
        self.aux = None
        self.cabeza=None
        self.padre = None
        self.cola=None
        self.LJ1=0 #litros de agua que tiene el jarro1
        self.LJ2=0 #litros de agua que tiene el jarro2

        self.NodoSolucion = None
        
        self.AJ1=J1 #Auxiliar Jarro 1
        self.AJ2=J2 #Auxiliar Jarro 2
        self.AMet = Meta #Auxiliar para la meta

        self.ban=0
        self.ban2=0
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

    def listarSolucion(self):
        #print "hola 0 --> ", self.NodoSolucion

        print "hola 1-- > " ,self.NodoSolucion
        temporal = self.padre

        while temporal != None:
            print "hola 1-- > ", temporal.verNodo()
            temporal = temporal.ptrPadre

            
        #    pass
        #print "hola 2-- > ", temporal.verNodo()

        #temporal = self.padre.ptrPadre.ptrPadre
        #print "hola 3-- > ", temporal.verNodo()

        #nueva = temporal.padre
        #print "hola 3-- > ", nueva.verNodo()


        #nueva = self.padre.verNodo()
        #print "ho-- > ", nueva

        #temporal=self.NodoSolucion
        #while temporal != None:
         #   print(temporal.verNodo())
         #   temporal = temporal.ptrPadre
    #retornar
    def retornar(self):
        print("****Retornar Solucion *****")
        temporal=self.NodoSolucion
        print(temporal.verNodo())

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
    def CrearPrimerEstado(self,J1,J2,Meta):
        print "vamos a salvar raizes"
        self.AJ1= J1
        self.AJ2= J2
        self.AMet = Meta
        #Genera el primer estado 
        self.Insertar(self.AJ1, self.AJ2, self.AMet)

    def Insertar(self,PJ1,PJ2,Meta):
        self.LJ1= PJ1
        self.LJ2= PJ2
        temporal=NodoArbol(PJ1, PJ2 , self.AMet)
        if self.vacia()==True:
            self.cabeza=temporal
            #self.cola=temporal
            self.aux = self.cabeza
            self.padre = self.cabeza
        else:
            self.aux.siguiente = temporal
            self.aux = temporal
            self.aux.ptrPadre = self.padre 

    #Evento 1 llenar jarro 1
    def Evento1(self, LJ1, LJ2):
        if LJ1 != self.AJ1:
            LJ1 = self.AJ1
            self.Insertar(LJ1, LJ2, self.AMet)
        
    #Evento 2 llenar jarro 2
    def Evento2(self, LJ1, LJ2):
        if LJ2 != self.AJ2:
            LJ2 = self.AJ2
            self.Insertar(LJ1, LJ2, self.AMet)
        
    #Evento 3 pasar agua del jarro2 -->al jarro1
    def Evento3(self, LJ1, LJ2):
        #print LJ1, LJ2, self.AJ1        
        if LJ2>0 and LJ1 < self.AJ1:
            LJ2 = LJ2 -1
            LJ1 = LJ1 + 1
            self.ban =  self.ban + 1
            self.Evento3(LJ1, LJ2)
        else:
            if self.ban > 0:
                self.ban = 0
                self.Insertar(LJ1, LJ2, self.AMet)
            
    #Evento 4 pasar agua del jarro1 al jarro2
    def Evento4(self, LJ1, LJ2):
        if LJ1>0 and LJ2 < self.AJ2:
            LJ1 = LJ1 - 1
            LJ2 = LJ2 + 1
            self.ban = self.ban + 1
            self.Evento4(LJ1, LJ2)
        else:
            if self.ban > 0:
                self.ban = 0
                self.Insertar(LJ1, LJ2, self.AMet)
            
    #Evento 5 vaciar el jarro 1
    def Evento5(self, LJ1, LJ2):
        if LJ1 > 0:
            LJ1=0
            self.Insertar(LJ1, LJ2, self.AMet)
        
    #Evento 6 vaciar el jarro 2
    def Evento6(self,  LJ1, LJ2):
        if LJ2 > 0:
            LJ2=0
            self.Insertar(LJ1, LJ2, self.AMet)
        
    #nos dice si llego a la meta
    def FunMeta(self,Meta):
        if self.LJ1+self.LJ2 == Meta:
            return True
        else:
            return False
    #nos regresa un nuevo estado
    def CrearEstado(self):

        while self.ban2 == 0:
            if self.cabeza == None:
                self.Insertar(self.LJ1, self.LJ2, self.AMet)
            else:
                self.padre= self.padre.siguiente
                
            #temporal=self.padre
            #while temporal != None:
                #temporal2 =temporal.verNodo()
                #temporal= temporal.siguiente
            temporal = self.padre.verNodo()
            #print "El padre 0", temporal

            J1 = temporal[0]
            J2 = temporal[1]
            Meta = temporal[2]

            self.Evento1(J1,J2)
            self.Evento2(J1,J2)
            self.Evento3(J1,J2)
            self.Evento4(J1,J2)
            self.Evento5(J1,J2)
            self.Evento6(J1,J2)
            #print("------Buscar la Meta -----")
            temporal=self.cabeza
            while temporal != None:
                self.NodoSolucion = (temporal.verNodo())
                respuesta = self.NodoSolucion[0] + self.NodoSolucion[1]
                if respuesta == self.AMet:
                    #print "nodo Solucion ----- >", self.NodoSolucion
                    self.listarSolucion()
                    #self.listar()
                    #exit()
                    self.ban2=1
                    temporal = None
                else:
                    temporal= temporal.siguiente

            self.CrearEstado()
            #print("------No La Encontro hara mas hijos -----")
            #temporal = self.padre.verNodo()
            #print "El padre 1:", temporal
            #self.padre = self.padre.siguiente
            #temporal = self.padre.verNodo()
            #print "El padre 2:", temporal
        #else:
        #    print "chao !!"

J1 = 5 # capacidad que tiene  el jarro 1
J2 = 4 # capacidad que tiene  el jarro 2
Meta= 3 #Meta litros agua
arb = Arbol(J1,J2,Meta)
#arb.PrimerInsertar(J1,J2,Meta)
arb.crearArbol()

#creado por jerson carranza

