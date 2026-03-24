""" CREACION DE LOS DADOS

"""

import random
# Pondremos a prueba el concepto de agregación

class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value
    

# Probando la clase
if __name__ == '__main__':
    mi_dado = Die()

    # Forma UNO para obtener valores
    print(mi_dado.value)
    mi_dado.roll()
    print(mi_dado.value)
    mi_dado.roll()
    print(mi_dado.value)
    mi_dado.roll()

    # Forma DOS para obtener valores
    nuevo_valor = mi_dado.roll()
    print(nuevo_valor)
    nuevo_valor = mi_dado.roll()
    print(nuevo_valor)
    nuevo_valor = mi_dado.roll()
    print(nuevo_valor)
    nuevo_valor = mi_dado.roll()
    print(nuevo_valor)

    # Forma TRES para obtener valores
    print(mi_dado.roll())
    print(mi_dado.roll())
    print(mi_dado.roll())
    
