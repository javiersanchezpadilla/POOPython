""" Creación de la clase nodo

    PEP8 recomienda que los nombres de los programas que servirán como 
    módulos sean escritos como la definición de las variable, usando
    solamente minúsculas y separando las palabras con guiones bajos, en
    este caso para matener un orden visual de desarrollo en el explorador
    de archivos fueron nombrados usando una letra mayúscula y un número
"""

class Nodo:

    def __init__(self, valor, siguiente_nodo=None):
        self._valor = valor
        self._siguiente = siguiente_nodo

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, nuevo_valor):
        self._valor = nuevo_valor

    @property
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self, nuevo_siguiente):
        self._siguiente = nuevo_siguiente
