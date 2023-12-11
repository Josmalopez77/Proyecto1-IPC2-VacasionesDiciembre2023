class Nodo:
    def __init__(self, nombre, ruta):
        self.nombre = nombre
        self.ruta = ruta
        self.siguiente = None
        self.anterior = None

class  Lista_canciones:
    def __init__(self):
        self.inicio = None
        self.fin = None
        
    def agregar_Cancion(self,nombre, ruta):
        nuevo = Nodo(nombre,ruta)
        if not self.inicio:
            self.inicio = nuevo
            self.fin = nuevo
        else:
            nuevo.anterior = self.fin
            self.fin.siguiente = nuevo
            self.fin=nuevo
            
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(actual.nombre, actual.ruta)
            actual = actual.siguiente
        