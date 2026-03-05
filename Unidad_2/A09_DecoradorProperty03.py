""" Atributos de "Solo Lectura": 

    Si creas un @property pero no creas su .setter,
    el atributo se vuelve imposible de cambiar desde fuera.

"""
class Movie:

    def __init__(self, titulo, valoracion):
        self.titulo = titulo
        self._valoracion = valoracion

    @property
    def valoracion(self):
        print("Estoy en el getter")
        return self._valoracion
    

mi_pelicula = Movie("Titanic", 4.3)
print(mi_pelicula.valoracion)
mi_pelicula.valoracion = 1.2        # ERROR No existe el setter
print(mi_pelicula.valoracion)


