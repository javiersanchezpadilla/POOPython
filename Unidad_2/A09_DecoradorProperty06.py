class Mochila:

    def __init__(self):
        self._articulos = []

    @property
    def articulos(self):
        print('Llamando al getter')
        return self._articulos
    
    @articulos.setter
    def articulos(self, lista_articulos):
        print('Llamando al setter')
        if isinstance(lista_articulos, list):
            self._articulos = lista_articulos
        else:
            print("Proporcione valores adecuados")

    
mi_mochila = Mochila()    
print(mi_mochila.articulos)
mi_mochila.articulos = ['lapiz', 'cuaderno', ' botella de agua']
print(mi_mochila.articulos)

