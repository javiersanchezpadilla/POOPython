""" En este ejemplo verificar que el radio sea un valor flotante
    y que además sea mayor a cero"""

class Circulo:

    def __init__(self, radio):
        self._radio = radio

    def get_radio(self):
        return self._radio
    
    def set_radio(self, new_radio):
        if isinstance(new_radio, float) and new_radio > 0:
            self._radio = new_radio
        else:
            print('Proporcione un valor de radio correcto')

    
mi_circulo = Circulo(40.0)
print(mi_circulo.get_radio())
mi_circulo.set_radio(1)
mi_circulo.set_radio(-20)
mi_circulo.set_radio("Hola")
mi_circulo.set_radio(10.0)
print(mi_circulo.get_radio())

