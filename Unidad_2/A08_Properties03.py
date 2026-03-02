""" Lo mas interesante de las propiedades es que podemos acceder a los
    atributos de instancia incluso con un nombre distinto al real"""


class Circulo:

    COLORES_VALIDOS = ('Rojo', 'Azul', 'Verde')

    def __init__(self, radio, color):
        self._radio = radio
        self._color = color

    def get_radio(self):
        return self._radio
    
    def set_radio(self, new_radio):
        if isinstance(new_radio, int) and new_radio > 0:
            self._radio = new_radio
        else:
            print('Proporcione un valor de radio correcto')

    radiosote = property(get_radio, set_radio)

    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        if new_color in Circulo.COLORES_VALIDOS:
            self._color = new_color
        else:
            print('Proporcione un color valido')
        
    colorsote = property(get_color, set_color)

circulo01 = Circulo(10, 'Rojo')
print(f'Valores radio {circulo01.radiosote}, color= {circulo01.colorsote}')
circulo01.radiosote = 20
circulo01.colorsote = 'Verde'
print(f'Valores radio {circulo01.radiosote}, color= {circulo01.colorsote}')

