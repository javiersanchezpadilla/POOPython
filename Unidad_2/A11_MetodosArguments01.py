""" ARGUMENTOS POR AUSENCIA EN LOS MÉTODOS

    La opración es la misma que en las funciones.

            def < method_name > (self, < param > = < value > ) :
                # Code

    Los parámetros con argumentos por defecto tienen que estar al final de la lista!!!!!!.

"""

class Jugador:

    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def mover_arriba(self, cambio=5):
        self.y += cambio

    def mover_abajo(self, cambio=5):
        self.y -= cambio

    def mover_izquierda(self, cambio=2):
        self.x += cambio 

    def mover_derecha(self, cambio=2):
        self.x -= cambio 


mi_jugador = Jugador(5, 10)
mi_jugador.mover_arriba()
print(f'({mi_jugador.x}, {mi_jugador.y})')
