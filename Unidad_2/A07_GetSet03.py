""" Continuamos con el uso de getters y Setters"""
class Mochila:

    def __init__(self):
        self._articulos = []

    def get_articulos(self):
        return self._articulos
    
    def set_articulos(self, nuevos_articulos):
        if isinstance(nuevos_articulos, list):
            self._articulos = nuevos_articulos
        else:
            print('Por favor introduzca una lista de articulos validos')

    
mi_mochila = Mochila()
print(mi_mochila.get_articulos())
mi_mochila.set_articulos(['Botella de agua', 'Bolsa de dormir', 'Lapiz'])
print(mi_mochila.get_articulos())
mi_mochila.set_articulos('Hola mundo')
print(mi_mochila.get_articulos())
mi_mochila.set_articulos(['Cuaderno'])
print(mi_mochila.get_articulos())
