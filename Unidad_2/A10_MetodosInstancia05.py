""" Otro ejemplo"""

class Mochila:

    def __init__(self):
        self._articulos = []

    @property
    def articulos(self):
        return self._articulos
    
    def agregar_articulos(self, articulo):
        if isinstance(articulo, str):
            self._articulos.append(articulo)
        else:
            print("Por favor provee un articulo valido")
    
    def elimina_articulo(self, articulo):
        if articulo in self._articulos:
            self._articulos.remove(articulo)
            return 1
        else:
            print("Este articulo no se encuentra en la mochila")
            return 0
        
    def tiene_el_articulo(self, articulo):
        return articulo in self._articulos
    

mi_mochila = Mochila()
print(mi_mochila.articulos)

# Agregamos una botella de agua a la mochila
mi_mochila.agregar_articulos("Botella de Agua")
print(mi_mochila.articulos)

# Agregamos una bolsa de dormir
mi_mochila.agregar_articulos("Bolsa de dormir")
print(mi_mochila.articulos)

# Verificamos si tenemos una botella de agua en la mochila
tiene_agua = mi_mochila.tiene_el_articulo("Botella de Agua")
print(tiene_agua)

# Sacamos de la mochila la botella de agua
mi_mochila.elimina_articulo("Botella de Agua")
print(mi_mochila.articulos)

# Sacamos de la mochila la bolda de dormir
mi_mochila.elimina_articulo("Bolsa de dormir")
print(mi_mochila.articulos)

# Intentamos eliminar algo que no esta en la mochila
mi_mochila.elimina_articulo("Dulce")
print(mi_mochila.articulos)
