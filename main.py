from artista import Lista_artistas
from album import Lista_album
from cancion import Lista_canciones
lista = Lista_artistas()
album = Lista_album()
cancion = Lista_canciones()

cancion.agregar_Cancion("cancion1","ruta1")
cancion.agregar_Cancion("cancion2","ruta2")
cancion.agregar_Cancion("cancion3","ruta3")
cancion.agregar_Cancion("cancion4","ruta4")
cancion.agregar_Cancion("cancion5","ruta5")

album.agregar_Album("album1","imagen1",cancion)
album.agregar_Album("album2","imagen2",cancion)

lista.agregar_Artista("nombre1",album)
lista.mostrar()