""" Creación de otras clases"""

class Circulo:

    def __init__(self, radio, color):
        self.radio = radio
        self.color = color


class CirculoFijo:

    def __init__(self, radio):
        self.radio = radio
        self.color = 'Azul'


class Rectangulo:

    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        

class Pelicula:

    def __init__(self, titulo, anio, lenguaje, raiting):
        self.titulo = titulo
        self.anio = anio
        self.lenguaje = lenguaje
        self.raiting = raiting
