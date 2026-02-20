""" EJERCICIO DE CODIFICACIÓN

    Ahora practicarás la creación de una instancia de una clase.
    Crear una clase basada en los siguientes requerimientos: 

    Paso 1: crea una instancia de una clase, El nombre debe ser "Solovino"
            su edad debería ser 5 y su peso debe ser 15. "Solovino" debe ser 
            un perro macho.

    Paso 2: Asigne esta instancia a una variable llamada mi_perro.
"""

class Perro():

    def __init__(self, nombre, edad, peso, es_macho):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.es_macho = es_macho


mi_perro = Perro('Firulais', 5, 15, True)
print('El nombre es:', mi_perro.nombre)
print('La edad es:', mi_perro.edad)
print('El peso es:', mi_perro.peso)
print('Es macho:', mi_perro.es_macho)
