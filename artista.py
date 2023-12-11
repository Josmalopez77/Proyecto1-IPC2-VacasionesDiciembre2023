class Nodo:
    def __init__(self, nombre, album):
        self.nombre = nombre
        self.album = album
        self.siguiente = None
        self.anterior = None

class  Lista_artistas:
    def __init__(self):
        self.inicio = None
        self.fin = None
        
    def agregar_Artista(self,nombre, album):
        nuevo = Nodo(nombre,album)
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
            print(actual.nombre)
            print("ALBUMES")
            actual.album.mostrar()
            actual = actual.siguiente
            
    
    
    