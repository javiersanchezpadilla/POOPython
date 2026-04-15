""" HERENCIA MULTIPLE MRO (Method Resolution Order).

    Cuando dos padres tienen un método con el mismo nombre, Python utiliza 
    una regla llamada MRO (Method Resolution Order). Básicamente, lee a los 
    padres de izquierda a derecha.

    El 'Problema del Diamante' (Conflicto de Nombres)
    ------------------------------------------------
    Imagina que tenemos un sistema de personajes donde un Mago y un Guerrero 
    tienen ambos un método llamado atacar(). Si creamos un MagoGuerrero, 
    ¿cómo ataca?

    con __mro__ (method resolution order) se despliega el orden para considerar
"""
class Mago:
    def __init__(self):
        print("Mago listo")
        
    def atacar(self):
        print("Lanzando un hechizo de fuego")

class Guerrero:
    def __init__(self):
        print("Guerrero listo")
        
    def atacar(self):
        print("Golpeando con una espada de acero")

# El orden aquí es CLAVE: Mago va primero
class MagoGuerrero(Mago, Guerrero):
    def habilidad_especial(self):
        print("Usando magia en la espada...")

# Prueba de ejecución
personaje = MagoGuerrero()
# ¿Qué pasará?
# Python ejecutará el método de Mago porque aparece primero en la lista 
# (Mago, Guerrero). Si invirtieras el orden a (Guerrero, Mago), el personaje 
# usaría la espada.
personaje.atacar()
print(MagoGuerrero.__mro__)
