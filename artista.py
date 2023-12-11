from graphviz import Digraph
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
            
    def generar_grafo(self):
        dot = Digraph(comment='Lista de Artistas')
        actual_artista = self.inicio
        while actual_artista:
            dot.node(actual_artista.nombre)
            if actual_artista.siguiente:
                dot.edge(actual_artista.nombre, actual_artista.siguiente.nombre)
            # Generar el grafo de álbumes y canciones para el artista actual
            if actual_artista.album:
                dot.subgraph(actual_artista.album.generar_grafo())
            actual_artista = actual_artista.siguiente
        return dot
            
  

            
    
    
    