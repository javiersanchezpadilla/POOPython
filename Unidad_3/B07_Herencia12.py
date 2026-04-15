""" EJEMPLO

"""

class Personaje:

    def __init__(self, x, y, vidas):
        self.x = x
        self.y = y
        self.vidas = vidas


class Jugador(Personaje):

    X_INICIAL = 0
    Y_INICIAL = 0
    VIDAS_INICIALES = 10

    def __init__(self, score=0):

        Personaje.__init__(self, Jugador.X_INICIAL, Jugador.Y_INICIAL, Jugador.VIDAS_INICIALES)
        self.score = score


class Enemigo(Personaje):

    def __init__(self, x=15, y=15, vidas=8, es_venenoso=False):
        Personaje.__init__(self, x, y, vidas)
        self.es_venenoso = es_venenoso


mi_jugador = Jugador()
print('X = ', mi_jugador.x)
print('Y = ', mi_jugador.y)
print('Vidas = ', mi_jugador.vidas)

enemigo_facil = Enemigo(vidas=1)
enemigo_dificil = Enemigo(vidas=56, es_venenoso=True)

print('\nENEMIGO FACIL')
print('X =', enemigo_facil.x)
print('Y =', enemigo_facil.y)
print('Vidas =', enemigo_facil.vidas)
print('Venenoso? ', enemigo_facil.es_venenoso)

print('\nENEMIGO DIFICIL')
print('X =', enemigo_dificil.x)
print('Y =', enemigo_dificil.y)
print('Vidas =', enemigo_dificil.vidas)
print('Venenoso? ', enemigo_dificil.es_venenoso)

