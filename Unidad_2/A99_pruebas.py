""" Desarrollo de la clase para las naves enemigas"""

import random as ran

class Nave:

    min_mov = 0
    max_mov = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y


n1 = Nave(0, 0)
n2 = Nave(1, 10)

naves = [n1, n2]

print(n1.max_mov)
print(n1.min_mov)

