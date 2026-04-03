""" HERENCIA

    Como asignar la herencia
    Crearemos una clase padre llamada Poligono
    y dos subclases que hereden de la clase padre Poligno    

    Verificar si una clase es una subclase de otra clase
    ----------------------------------------------------

    issubclass()  Con esta función, podemos verificar si una clase es
                  una subclase de otra clase.
"""

class Poligono:
    pass


class Triangulo(Poligono):
    pass 


class Cuadraro(Poligono):
    pass



print('Es una subclase Cuadrado de Poligono? ', issubclass(Cuadraro, Poligono))
print('Es una subclase Triangulo de Poligono? ', issubclass(Triangulo, Poligono))
