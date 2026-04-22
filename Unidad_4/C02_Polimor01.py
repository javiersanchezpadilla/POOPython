""" POLIMORFISMO.

    El Polimorfismo es la tercera gran columna de la POO (junto con la 
    Encapsulación y la Herencia).
    La palabra viene del griego: Poly (muchos) y Morphos (formas). 
    En programación, es la capacidad de que diferentes objetos respondan al 
    mismo mensaje (método) de maneras distintas.
    El polimorfismo es lo que nos permite escribir código que 'no sabe' 
    exactamente con qué tipo de objeto está tratando, pero sabe que 'sabe 
    hacer' lo que se le pide.

    1. El Concepto: 'Una interfaz, múltiples métodos'
    -------------------------------------------------
    Imagina que tienes un control remoto universal con un botón de 'Reproducir'
    No importa si lo apuntas a un reproductor de DVD, a Spotify o a YouTube; 
    cada uno 'reproducirá' a su manera, pero tú solo tuviste que presionar un 
    botón.

    2. Polimorfismo con Herencia (El ejemplo clásico)
    -------------------------------------------------
    Es la forma más común de enseñarlo. Varias clases heredan de un mismo padre
    y sobrescriben un método.

    ¿Por qué es poderoso? 
    ---------------------
    Porque si mañana añades una clase Vaca, la función hacer_ruido no tiene que 
    cambiar. Tu código ya es compatible con cualquier cosa que 'sepa hablar'.
"""

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "¡Guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau!"

# Aquí ocurre la magia del polimorfismo:
# Una función que acepta CUALQUIER animal
def hacer_ruido(cualquier_animal):
    print(cualquier_animal.hablar())

# No importa qué le pasemos, la función sabe qué hacer
mascotas = [Perro(), Gato()]

for m in mascotas:
    hacer_ruido(m)
