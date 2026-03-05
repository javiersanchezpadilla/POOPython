""" CReamos una clase Pelota resolviendo con properties

    este mismo ejemplo se resuelve mas ademante mediante decoradores
"""

class Pelota:

    def __init__(self, precio, tamanio, marca):
        self._precio = precio
        self._tamanio = tamanio
        self._marca = marca

    def get_precio(self):
        return self._precio
    
    def set_precio(self, new_precio):
        self._precio = new_precio

    def get_tamanio(self):
        return self._tamanio
    
    def set_tamanio(self, new_tamanio):
        self._tamanio = new_tamanio

    def get_marca(self):
        return self._marca
    
    def set_marca(self, new_marca):
        self._marca = new_marca

    precio = property(get_precio, set_precio)
    tamanio = property(get_tamanio, set_tamanio)
    marca = property(get_marca, set_marca)

my_pelota = Pelota(10, 10, "Gada")
print(my_pelota.precio)
print(my_pelota.tamanio)
print(my_pelota.marca)
my_pelota.precio = 20
my_pelota.tamanio = 20
my_pelota.marca = "Gadagada"
print(my_pelota.precio)
print(my_pelota.tamanio)
print(my_pelota.marca)
