""" Este programa permite una clase, la cual asignaremos a diez instancias a las
    cuales les daremos una coordenada inicial, posteriormente imprimimos su 
    posición, luego modificamos su posición y al final volveos a imprimir su 
    posición"""

import random

class NaveEnemiga:

    min_mov = 1
    max_mov = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y


def muestra_naves(las_naves):
    for nave in las_naves:
        print(f'Posicion nave {naves_enemigas.index(nave)+1} es ({nave.x}, {nave.y})')


def avanza_naves(las_naves):
    print('Las naves estan avanzando')
    for nave in las_naves:
        nave.x += random.randint(nave.min_mov,nave.max_mov)
        nave.y += random.randint(nave.min_mov,nave.max_mov)


n1 = NaveEnemiga(0, 0)
n2 = NaveEnemiga(10, 0)
n3 = NaveEnemiga(15, 0)
n4 = NaveEnemiga(20, 0)
n5 = NaveEnemiga(25, 0)
n6 = NaveEnemiga(30, 0)
n7 = NaveEnemiga(35, 0)
n8 = NaveEnemiga(40, 0)
n9 = NaveEnemiga(45, 0)
n10 = NaveEnemiga(50, 0)

print(n1.x,n1.y)

naves_enemigas = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

muestra_naves(naves_enemigas)
avanza_naves(naves_enemigas)
muestra_naves(naves_enemigas)
