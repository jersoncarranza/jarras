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

class NodoArbol:
    def __init__ (self,J1,J2,Meta):
        self.siguiente = None
        self.anterior = None
        #self.info=J1
        self.datos = [J1,J2,Meta]

    def verNodo(self):
        return self.datos


    def crearHijos(self):
        print "Los datos NodoArbol:", self.datos
        Li=Lista(J1,J2,Meta)
        Li.CrearEstado()
        Li.listar()

class Lista:
    def __init__(self,J1,J2,Meta):
        self.aux = None
        self.cabeza=None
        self.cola=None
        self.LJ1=0 #litros de agua que tiene el jarro1
        self.LJ2=0 #litros de agua que tiene el jarro2
        
        self.AJ1=J1 #Auxiliar Jarro 1
        self.AJ2=J2 #Auxiliar Jarro 2
        self.AMet = Meta #Auxiliar para la meta

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
        print("****Listar desde cola*****")
        temporal=self.cola
        while temporal != None:
            print(temporal.verNodo())
            temporal = temporal.anterior
    #retornar
    def retornar(self):
        print("****retornar*****")
        temporal=self.cola
        while temporal != None:
            return temporal.verNodo()
            temporal = temporal.anterior
            #return temporal

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
        self.Insertar(0,0,self.AMet)

    def Insertar(self,PJ1,PJ2,Meta):
        self.LJ1= PJ1
        self.LJ2= PJ2
        temporal=NodoArbol(self.LJ1, self.LJ2, self.AMet)
        if self.vacia()==True:
            self.cabeza=temporal
            self.cola=temporal
            self.aux = self.cabeza
            print "cc", self.cabeza[1]
        else:
            self.aux.siguiente = temporal
            self.aux = temporal
            #temporal.siguiente=self.cabeza
            #self.cabeza.anterior=temporal
            #self.cabeza=temporal

    #Evento 1 llenar jarro 1
    def Evento1(self):
        self.LJ1 = self.AJ1
        print "Litros jarro1" , self.LJ1 , "Litros jarro2" , self.LJ2
        self.Insertar(self.LJ1, self.LJ2, self.AMet)

    #Evento 2 llenar jarro 2
    def Evento2(self):
        self.LJ2 = self.AJ2
        self.Insertar(self.LJ1, self.LJ2, self.AMet)
        
    #Evento 3 pasar agua del jarro2 al jarro1
    def Evento3(self):
        #print "LJ1 es ",self.LJ1
        #print "LJ2 es ",self.LJ2
        #print "========= "
        if self.LJ2>0 and self.LJ1 < self.AJ1:
            self.LJ2 = self.LJ2 -1
            self.LJ1 = self.LJ1 + 1
            self.Evento3()
        else:
            self.Insertar(self.LJ1, self.LJ2, self.AMet)

    #Evento 4 pasar agua del jarro1 al jarro2
    def Evento4(self):
        if self.LJ1>0 and self.LJ2 < self.AJ2:
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
        self.Evento1()
        self.Evento2()
        #self.Evento5()
        #self.Evento3()
        #self.Evento4()
        #self.Evento6()


J1 = 5 # capacidad que tiene  el jarro 1
J2 = 3 # capacidad que tiene  el jarro 2
Meta= 7 #Meta litros agua
arb = Arbol(J1,J2,Meta)
#arb.PrimerInsertar(J1,J2,Meta)
arb.crearArbol()

