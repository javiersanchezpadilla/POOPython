""" Seguimos con los valores por ausencia o valores por defecto"""


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

    # Vamos a crear una funcion para ordenar el contenido de la mochils
    def muestra_articulos(self, ordenados=False):
        if ordenados:
            print(sorted(self._articulos))
        else:
            print(self._articulos)


mi_mochila = Mochila()
print(mi_mochila.articulos)

# Agregamos una botella de agua a la mochila
mi_mochila.agregar_articulos("Botella de Agua")
mi_mochila.agregar_articulos("Bolsa de dormir")
mi_mochila.agregar_articulos("Dulces")
mi_mochila.agregar_articulos("Clips")

print("Desordenada")
mi_mochila.muestra_articulos()

print("Ordenada")
mi_mochila.muestra_articulos(True)

