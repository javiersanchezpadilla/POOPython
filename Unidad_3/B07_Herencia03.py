""" ATRIBUTOS HEREDADOS CON __init___()

    Vamos a ver como hacer que una clase herede los atributos de una clase.
    CUANDO NO INDICAMOS MÉTODO __init__() en la clase hija de donde creamos la
    instancia, automaticamente se ejecuta el método __init__() de la clase
    padre (en este caso Poligono)

 """

class Poligono:

    def __init__(self, numero_lados, color):
        self.numero_lados = numero_lados
        self.color = color
        

class Triangulo(Poligono):
    pass


# creamos una instancia de triangulo, sin embargo como hereda dela clase padre
# Poligono es necesario incluir los atributos requeridos por la clase padre
# que son el numero de lados, así como el color
mi_triangulo = Triangulo(3, 'Rojo')
print(mi_triangulo.numero_lados)        # Resultado 3
print(mi_triangulo.color)               # Resultado 'Rojo'
