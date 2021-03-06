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
        self.padre = None
        self.cola=None
        self.LJ1=0 #litros de agua que tiene el jarro1
        self.LJ2=1 #litros de agua que tiene el jarro2
        
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
        self.Insertar(self.AJ1, self.AJ2, self.AMet)

    def Insertar(self,PJ1,PJ2,Meta):
        self.LJ1= PJ1
        self.LJ2= PJ2
        temporal=NodoArbol(self.LJ1, self.LJ2, self.AMet)
        if self.vacia()==True:
            self.cabeza=temporal
            self.cola=temporal
            self.aux = self.cabeza
            self.padre = self.cabeza
        else:
            self.aux.siguiente = temporal
            self.aux = temporal

    #Evento 1 llenar jarro 1
    def Evento1(self):
        if self.LJ1 != self.AJ1:
            self.LJ1 = self.AJ1
            self.Insertar(self.LJ1, self.LJ2, self.AMet)
        else:
            print "No se pudo insertar 1 Evento"

    #Evento 2 llenar jarro 2
    def Evento2(self):
        if self.LJ2 != self.AJ2:
            self.LJ2 = self.AJ2
            self.Insertar(self.LJ1, self.LJ2, self.AMet)
        else:
            print "No se pudo insertar 2 Evento"
        
    #Evento 3 pasar agua del jarro2 al jarro1
    def Evento3(self):
        ban = 0
        if self.LJ2>0 and self.LJ1 < self.AJ1:
            self.LJ2 = self.LJ2 -1
            self.LJ1 = self.LJ1 + 1
            ban =  ban + 1
            self.Evento3()
        else:
            if ban > 0:
                self.Insertar(self.LJ1, self.LJ2, self.AMet)
            else:
                print "no se inserto 3 Evento"

    #Evento 4 pasar agua del jarro1 al jarro2
    def Evento4(self):
        ban = 0
        if self.LJ1>0 and self.LJ2 < self.AJ2:
            self.LJ1 = self.LJ1 - 1
            self.LJ2 = self.LJ2 + 1
            ban = ban + 1
            self.Evento4()
        else:
            if ban > 0:
                self.Insertar(self.LJ1, self.LJ2, self.AMet)
            else:
                print "no se inserto 4 Evento"
    
    #Evento 5 vaciar el jarro 1
    def Evento5(self):
        if self.LJ1 > 0:
            self.LJ1=0
            self.Insertar(self.LJ1, self.LJ2, self.AMet)
        else:
            print "no se inserto 5 Evento"


    #Evento 6 vaciar el jarro 2
    def Evento6(self):
        if self.LJ2 > 0:
            self.LJ2=0
            self.Insertar(self.LJ1, self.LJ2, self.AMet)
        else:
            print "no se inserto 6 Evento"

    #nos dice si llego a la meta
    def FunMeta(self,Meta):
        if self.LJ1+self.LJ2 == Meta:
            return True
        else:
            return False
    #nos regresa un nuevo estado
    def CrearEstado(self):
        if self.cabeza == None:
            self.Insertar(self.LJ1, self.LJ2, self.AMet)
        self.Evento1()
        self.Evento2()
        self.Evento3()
        self.Evento4()
        self.Evento5()
        self.Evento6()

J1 = 5 # capacidad que tiene  el jarro 1
J2 = 3 # capacidad que tiene  el jarro 2
Meta= 7 #Meta litros agua
arb = Arbol(J1,J2,Meta)
#arb.PrimerInsertar(J1,J2,Meta)
arb.crearArbol()

