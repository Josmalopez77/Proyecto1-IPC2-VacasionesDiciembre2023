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
            
    def agregar_Artista_Existente(self, nombre, nombreAlbum, imagen, canciones):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                actual.album.agregar_Album(nombreAlbum, imagen,canciones)
                return
            actual = actual.siguiente
                
    def agregar_Artista_Existente_Album(self, nombre, nombreAlbum, cancion, ruta):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                actual.album.agregar_Album_Existente(nombreAlbum, cancion, ruta)
                return
            actual = actual.siguiente
        
    def validar(self, nombreA):
        actual = self.inicio     
        if self.inicio:
            while actual:
                if actual.nombre == nombreA:
                    return True
                actual = actual.siguiente
                
    def validarAlbum(self, nombreA,nombreAlbum ):
        actual = self.inicio     
        if self.inicio:
            while actual:
                if actual.nombre == nombreA:
                    variable = actual.album.validar(nombreAlbum)
                    return variable
                actual = actual.siguiente
                
            
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(actual.nombre)
            print("ALBUMES")
            actual.album.mostrar()
            actual = actual.siguiente
            
    def generar_grafo(self):
        dot = Digraph(comment='Lista de Artistas', rankdir='LR')  # Ajusta la orientación según sea necesario
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
            
  

            
    
    
    