""" METODO __str__()

    Cuando llamamos a la función print en un objeto o a la función format, 
    estamos llamando al método __str__() indirectamente, estamos llamando 
    y el valor que vemos impreso como salida es el valor devuelto por este 
    método, el método __str__() es llamados por las funciones interconstruidas 
    str() , format()  y print().

    Entonces si se quiere personalizar el aspecto de un objeto cuando lo imprimes 
    usando la función print, tienes que implementar el método __str__ en tu clase.
"""

class Punto2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):          # Con esta implementacion resultado = (10, 30)
        return f'({self.x}, {self.y})'
    
mi_punto = Punto2D(10, 30)
print(mi_punto)                 # Res <__main__.Punto2D object at 0x734e7b702030>

