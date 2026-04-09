""" EXTENDIENDO LA FUNCIONALIDAD DE LOS MÉTODOS

    Podemos extender la funcionalidad de los métodos llamando dentro del
    método sobreescrito al método super
"""

class Mochila:

    def __init__(self):
        self.articulos = []

    def agregar_antojo(self, antojo):
        print("Agregando un antojo a la mochila")
        self.articulos.append(antojo)
        print(f"{antojo.capitalize()} fue agregado")


class MochilaEscolar(Mochila):

    def agregar_antojo(self, antojo):
        """ Duplicará el antojo dentro de la mochila, ya que llama al método
            dos veces (en cada llamada usa tecnica distinta)"""
        print("Es tiempo de ir a la escuela")
        # Aquí estamos extendiente la funcionalidad
        super().agregar_antojo(antojo)          # <-- podemos llamarlo así
        Mochila.agregar_antojo(self, antojo)    # <-- o también así
        print("Ahora tu mochila tiene estos antojos", self.articulos)


mi_mochila = MochilaEscolar()
mi_mochila.agregar_antojo('Dulce')
