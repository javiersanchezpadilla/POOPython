""" HERENCIA DE LOS MÉTODOS.

    Las subclases tendrán acceso a los métodos de las clases padre o 
    superclases


    MUY IMPORTANTE!!! Cuando usar self y cuando no.
    -----------------------------------------------
    A)  Cuando llamamos un método mediante el nombre de la superclase, es 
        necesario incluir la palabra self.
    B)  Cuando llamamos un método mediante la función super(), no debemos 
        especificar el argumento sefl.

    EJEMPLO, digamos que tenemos Una clase polígono, una clase triangulo
    y una clase cuadrado, estas dos clases tienen algunos métodos en común, 
    por ejemplo, podemos querer imprimir su tamaño y también hallar su 
    perímetro, la suma de la longitud de todos sus lados, estas son 
    operaciones comunes en ambas clases que pueden ser implementadas y 
    funcionar para cualquier polígono que creemos. 
    Así que para evitar la repetición de código, podemos simplemente definir 
    este método en la superclase en Poligono y hacer que las clases hijas 
    hereden estos métodos o funcionalidades automáticamente. 
"""

class Poligono:

    def __init__(self, numero_lados, color):
        self.numero_lados = numero_lados
        self.color = color

    def describe_poligono(self):
        print(f"Este poligono tiene {self.numero_lados} lados y es {self.color}.")

class Triangulo(Poligono):

    NUMERO_LADOS = 3

    def __init__(self, base, height, color):
        Poligono.__init__(self, Triangulo.NUMERO_LADOS, color)
        self.base = base
        self.height = height

    def encuentra_area(self):
        return (self.base * self.height) / 2


class Cuadrado(Poligono):

    NUMERO_LADOS = 4

    def __init__(self, longitud_lado, color):
        Poligono.__init__(self, Cuadrado.NUMERO_LADOS, color)
        self.longitud_lado = longitud_lado

    def encuentra_area(self):
        return self.longitud_lado ** 2


mi_triangulo = Triangulo(10, 20, 'Azul')
mi_triangulo.describe_poligono()
print('El area de mi triangulo es: ', mi_triangulo.encuentra_area())

mi_cuadro = Cuadrado(4, 'Morado')
mi_cuadro.describe_poligono()
print('El area de mi cuadrado es :', mi_cuadro.encuentra_area())

