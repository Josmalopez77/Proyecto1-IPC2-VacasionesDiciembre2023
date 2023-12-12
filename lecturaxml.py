import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from artista import Lista_artistas
from album import Lista_album
from cancion import Lista_canciones
lista = Lista_artistas()
def leer_xml(archivo):
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()
        for cancion in root.findall('cancion'):
            nombre = cancion.get('nombre')
            artista = cancion.find('artista').text
            album = cancion.find('album').text
            imagen = cancion.find('imagen').text
            ruta = cancion.find('ruta').text
            
            if  lista.validar(artista):
                print("Encontro el artista")
                if lista.validarAlbum(artista, album):
                    print("Encontro el album")
                    lista.agregar_Artista_Existente_Album(artista, album, nombre, ruta)
                else:
                    cancion2 = Lista_canciones()
                    cancion2.agregar_Cancion(nombre, ruta)
                    lista.agregar_Artista_Existente(artista, album, imagen, cancion2)
            else:
                cancion2 = Lista_canciones()
                cancion2.agregar_Cancion(nombre, ruta)
                album2 = Lista_album()
                album2.agregar_Album(album, imagen, cancion2)
                lista.agregar_Artista(artista, album2)

    except ET.ParseError as e:
        print(f'Error al analizar el archivo XML: {e}')
        
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[('Archivos XML', '*.xml')])
    if archivo:
        print(f'Se seleccionó el archivo: {archivo}')
        leer_xml(archivo)
seleccionar_archivo()
lista.mostrar()
