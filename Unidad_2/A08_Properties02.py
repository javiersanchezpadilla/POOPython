""" Ejemplo del uso de property(get, set)"""


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

    radio = property(get_radio, set_radio)

    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        if new_color in Circulo.COLORES_VALIDOS:
            self._color = new_color
        else:
            print('Proporcione un color valido')
        
    color = property(get_color, set_color)


circulo01 = Circulo(10, 'Rojo')
print(f'Valores radio {circulo01.radio}, color= {circulo01.color}')
circulo01.radio = 20
circulo01.color = 'Verde'
print(f'Valores radio {circulo01.radio}, color= {circulo01.color}')

