""" Podemos definir al igual que las propiedades un nombre distinto al atributo
    de instancia, el ejemplo a desarrollar no es una buena práctica
"""

class Pelota:

    def __init__(self, precio):
        self._precio = precio

    @property
    def prexioso(self):             # Creamos la propiedad prexioso (getter)
        return self._precio
    
    @prexioso.setter                # continuamos usando la propiedad prexioso
    def prexioso(self, new_precio):
        self._precio = new_precio

 
my_pelota = Pelota(10)
print(my_pelota.prexioso)           # Llama al gettes
my_pelota.prexioso = 20             # llama al setter
print(my_pelota.prexioso)

