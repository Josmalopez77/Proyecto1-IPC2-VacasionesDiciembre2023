class Nodo:
    def __init__(self, nombre, imagen, canciones):
        self.nombre = nombre
        self.imagen = imagen
        self.canciones = canciones
        self.siguiente = None
        self.anterior = None

class  Lista_album:
    def __init__(self):
        self.inicio = None
        self.fin = None
        
    def agregar_Album(self,nombre, imagen, canciones):
        nuevo = Nodo(nombre, imagen, canciones)
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
            print(actual.nombre, actual.imagen)
            print("CANCIONES")
            actual.canciones.mostrar()
            actual = actual.siguiente