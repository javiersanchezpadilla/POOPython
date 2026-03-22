""" SOBRECARGA DE OPERADORES.

    Sobrecargar el operador de suma de tal manera que permita sumas las 
    coordenadas (x, y) de dos instancias, cuando sumamos dos puntos, sumamos 
    las coordenadas correspondientes, la coordenada 'Xa' con la coordenada 
    'Xb' y la coordenada 'Ya' con la coordenada 'Yb' respectivamente, el 
    resultado es otro punto con dos coordenadas.
"""
class Punto2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        nueva_x = self.x + other.x
        nueva_y = self.y + other.y
        return Punto2D(nueva_x, nueva_y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

puntoA = Punto2D(5, 6)
print(type(puntoA))
print(puntoA)

puntoB = Punto2D(2, 3)
print(type(puntoB))
print(puntoB)

puntoC = puntoA + puntoB
print(type(puntoC))
print(puntoC)

