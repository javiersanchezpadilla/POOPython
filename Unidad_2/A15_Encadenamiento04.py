""" Encadenamiento en nuestras Propias Clases

    Cada método debe retornar al propio objeto usando return self.

    Ventajas para tu clase:
    -----------------------
    A)  Código más limpio: Evitas crear variables temporales que solo usas 
        una vez.
    B)  Lectura fluida: El código se lee casi como una oración: 
        "Crea al héroe, entrénalo y equilpale un escudo".

    ADVERTENCIA!!!!:
    ----------------
    No se debe abusar del encanamiento, un encadenamiento de 10 métodos en 
    una sola línea es muy difícil de depurar (hacer debug). 
    Si algo falla en la mitad, es difícil saber exactamente en qué punto 
    ocurrió el error.
"""

class Heroe:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
        self.escudo = False

    def entrenar(self):
        self.energia += 10
        print(f"{self.nombre} entrenó. Energía: {self.energia}")
        return self  # <--- ¡ESTO permite el encadenamiento!

    def equipar_escudo(self):
        self.escudo = True
        print(f"{self.nombre} ahora tiene escudo.")
        return self  # <--- ¡ESTO permite el encadenamiento!

# Ahora podemos hacer esto en una sola línea:
mi_heroe = Heroe("Arturo").entrenar().equipar_escudo()
