""" 

    El Guerrero (Más flexible)
    --------------------------
    La composición permite cambiar el comportamiento en tiempo de ejecución, 
    algo que la herencia no puede hacer fácilmente.
"""
class Espada:
    def usar(self):
        print("Atacando con un tajo de espada")

class Magia:
    def usar(self):
        print("Lanzando una bola de fuego")

class Personaje:
    def __init__(self, arma):
        self.arma = arma # Composición: el personaje "tiene" un arma

    def combatir(self):
        self.arma.usar()

# Podemos cambiar el arma fácilmente (Inyección de dependencias)
guerrero = Personaje(Espada())
guerrero.combatir()

# El MISMO personaje ahora puede usar magia sin cambiar de clase
guerrero.arma = Magia()
guerrero.combatir()
