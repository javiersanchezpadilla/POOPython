""" Para crear las instancias hacemos lo siguiente"""

class Nave:
    
    def __init__(self, x, y):   # Error común: olvidar el parámetro para la instancia
        self.x = x
        self.y = y

# Creamos tres instancias de la forma normal
n1 = Nave(10, 20)
n2 = Nave(100, 200)
n3 = Nave(0,350)

