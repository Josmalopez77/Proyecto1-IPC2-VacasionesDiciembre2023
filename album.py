from graphviz import Digraph
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
            
    def agregar_Album_Existente(self, nombre, cancion, ruta):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                actual.canciones.agregar_Cancion(cancion, ruta)
                print("Cancion Agregada al album existente")
                return
            actual = actual.siguiente
                
        
            
    def validar(self, nombre):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                return True
            actual = actual.siguiente
        return False
            
    
            
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(actual.nombre, actual.imagen)
            print("CANCIONES")
            actual.canciones.mostrar()
            actual = actual.siguiente
            
            
    def generar_grafo(self):
        dot = Digraph(comment='Lista de Álbumes')
        actual_album = self.inicio

        while actual_album:
            dot.node(actual_album.nombre)

            if actual_album.siguiente:
                dot.edge(actual_album.nombre, actual_album.siguiente.nombre)

            # Generar el grafo de canciones para el álbum actual
            if actual_album.canciones:
                dot.subgraph(actual_album.canciones.generar_grafo())

            actual_album = actual_album.siguiente

        return dot
        
            
