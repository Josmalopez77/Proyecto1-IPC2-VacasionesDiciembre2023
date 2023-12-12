from artista import Lista_artistas
from album import Lista_album
from cancion import Lista_canciones
lista = Lista_artistas()

cont = 1
a = "artista"
albumm = "album"
cancionn = "cancion"
imagen = "imagen"
ruta = "ruta"

if  lista.validar(a):
    print("Encontro el artista")
    if lista.validarAlbum(a, albumm):
        print("Encontro el album")
        lista.agregar_Artista_Existente_Album(a, albumm, cancionn, ruta)
    else:
        album = Lista_album()
        cancion = Lista_canciones()
        cancion.agregar_Cancion(cancionn, ruta)
        lista.agregar_Artista_Existente(a, albumm, imagen, cancion)     
else:
    cancion = Lista_canciones()
    cancion.agregar_Cancion(cancionn, ruta)
    album = Lista_album()
    album.agregar_Album(albumm, imagen, cancion)
    lista.agregar_Artista(a, album)
    
cancionn = "cancion2"
ruta = "ruta2"  
if  lista.validar(a):
    print("Encontro el artista")
    if lista.validarAlbum(a, albumm):
        print("Encontro el album")
        lista.agregar_Artista_Existente_Album(a, albumm, cancionn, ruta)
    else:
        album = Lista_album()
        cancion = Lista_canciones()
        cancion.agregar_Cancion(cancionn, ruta)
        lista.agregar_Artista_Existente(a, albumm, imagen, cancion)     
else:
    cancion = Lista_canciones()
    cancion.agregar_Cancion(cancionn, ruta)
    album = Lista_album()
    album.agregar_Album(albumm, imagen, cancionn)
    lista.agregar_Artista(a, album)

albumm="album2"
if  lista.validar(a):
    print("Encontro el artista")
    if lista.validarAlbum(a, albumm):
        print("Encontro el album")
        lista.agregar_Artista_Existente_Album(a, albumm, cancionn, ruta)
    else:
        album = Lista_album()
        cancion = Lista_canciones()
        cancion.agregar_Cancion(cancionn, ruta)
        lista.agregar_Artista_Existente(a, albumm, imagen, cancion)     
else:
    cancion = Lista_canciones()
    cancion.agregar_Cancion(cancionn, ruta)
    album = Lista_album()
    album.agregar_Album(albumm, imagen, cancionn)
    lista.agregar_Artista(a, album)


    
lista.mostrar()