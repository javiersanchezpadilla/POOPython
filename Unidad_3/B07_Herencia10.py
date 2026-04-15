""" ATRIBUTOS HEREDADOS.

    Cuando en la subclase existe o cuenta con su propio método __init__()
    los atributos de la superclase no se heredan de forma automática, 
    anteriormente si se pudo porque la subclase no tenia el método __init__()
    pero en este caso ya no cumple esta regla, entonces tenemos que escribirlo
    de forma explicita (llamarlo manualmente)

        <superclase>.__init__(self, <argumentos>)

"""


class Poligono:

    def __init__(self, numero_lados, color):
        self.numero_lados = numero_lados
        self.color = color
        

class Triangulo(Poligono):

    NUMERO_LADOS = 3

    def __init__(self, base, altura, color):
        # inicializamos atributos de la superclase o clase padre
        Poligono.__init__(self, Triangulo.NUMERO_LADOS, color) 
        self.base = base
        self.altura = altura


# creamos una instancia de triangulo, sin embargo como hereda dela clase padre
# Poligono es necesario incluir los atributos requeridos por la clase padre
# que son el numero de lados, así como el color, y los atributos propios de la
# lase hija que en este caso son la base y la altura, al ser un triangulo el
# numero de lados lo asignamos como un atributo de clase NUMERO_LADOS = 3
mi_triangulo = Triangulo(5, 4, 'Rojo')

print('Lados = ', mi_triangulo.numero_lados)        # Resultado 3
print('Color = ', mi_triangulo.color)               # Resultado 'Rojo'
print('Base = ', mi_triangulo.base)                # 5
print('Altura = ', mi_triangulo.altura)              # 4

