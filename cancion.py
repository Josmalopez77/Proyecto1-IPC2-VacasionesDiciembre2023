from graphviz import Digraph
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
            
    def validar(self, nombre):
        actual = self.inicio
        while actual:
            if nombre == actual.nombre:
                print("La cancion ya existe")
                return True
            actual = actual.siguiente
            
    def mostrar(self,):
        actual = self.inicio
        while actual:
            print("NOMBRE DE CANCION -> ",actual.nombre,"RUTA DE CANCION -> ", actual.ruta)
            actual = actual.siguiente
            
    def generar_grafo(self):
        dot = Digraph(comment='Lista de Canciones')

        actual_cancion = self.inicio
        while actual_cancion:
            dot.node(actual_cancion.nombre)

            if actual_cancion.siguiente:
                dot.edge(actual_cancion.nombre, actual_cancion.siguiente.nombre)

            actual_cancion = actual_cancion.siguiente

        return dot

        