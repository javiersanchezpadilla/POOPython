""" Este ejempo se resolvio anteriormente solo con la propiedad
    property, ahora se resolvera con decoradores
    
    Recursión Infinita: Si dentro del setter de precio escriben 
    self.precio = new_precio en lugar de self.__precio = new_precio, el 
    programa entrará en un bucle infinito y se detendrá con un RecursionError. 
    Es el error más común al aprender @property.
    """

class Pelota:

    def __init__(self, precio, tamanio, marca):
        self._precio = precio
        self._tamanio = tamanio
        self._marca = marca

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, new_precio):
        self._precio = new_precio

    @property
    def tamanio(self):
        return self._tamanio
    
    @tamanio.setter
    def tamanio(self, new_tamanio):
        self._tamanio = new_tamanio

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, new_marca):
        self._marca = new_marca


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
