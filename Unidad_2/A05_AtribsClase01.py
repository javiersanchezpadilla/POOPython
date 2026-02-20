""" DEFINICIÓN DE LOS ATRIBUTOS DE CLASE.

    Los atributos de clase pertenecen a una clase y no a una instancia 
    concreta.
    Todas las instancias de la clase tienen acceso a este atributo.
    Ellos comparten el mismo valor, así que cualquier cambio a este valor 
    afecta a todas las instancias.
    Todos ellos comparten el mismo valor, así que cualquier cambio realizado 
    a este valor afectará a todas las instancias.

            class ClassName:
	            # Atributos de clase
	            def __init__ (self):
	            # Métodos

*) Los atributos de clase pertenecen a la clase.
*) Son compartidos por todas las instancias de la clase.
*) Los atributos de clase se pueden utilizar para definir constantes a nivel 
   de clase o valores predeterminados que debe compartirse entre todas las instancias.
"""

# Creación de los atributos de una clase.
class Perro:

    especie = "Canis lupus"

    def __init__ (self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza


class Mochila:

    num_max_artics = 10

    def __init__(self):
        self.articulos = []

print(Perro.especie)
print(Mochila.num_max_artics)