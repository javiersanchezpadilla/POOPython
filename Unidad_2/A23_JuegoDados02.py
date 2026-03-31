""" DESARROLLO DE LA CLASE JUGADOR
"""

import random
# Pondremos a prueba el concepto de agregación

class Dado:

    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor
    
    def rodar_dado(self):
        nuevo_valor = random.randint(1, 6)
        self._valor = nuevo_valor
        return nuevo_valor

    

class Jugador:

    # los atributos seran solo de lectura
    def __init__(self, dado, es_la_computadora=False):
        self._dado = dado
        self._es_la_computadora = es_la_computadora
        self._contador = 10

    @property
    def dado(self):
        return self._dado
    
    @property
    def es_la_computadora(self):
        return self._es_la_computadora
    
    @property
    def contador(self):
        return self._contador
    
    def incementar_contador(self):
        valor_calculado = self._contador + 1
        self._contador = valor_calculado
        return valor_calculado

    def decrementar_contador(self):
        valor_calculado = self._contador - 1
        self._contador = valor_calculado
        return valor_calculado
    
    def rueda_el_dado(self):
        """ Llamamos al método para rodar el dado de la clase
            Dado que permite hacer rodar el dado"""
        return self._dado.rodar_dado()
    

# Probamos la declaracion de la clase
if __name__ == "__main__":
    mi_dado = Dado()
    mi_jugador = Jugador(mi_dado, True)
    # Aqui podemos comprobar que son instancias diferentes con distintas
    # asignaciones de memoria
    print(mi_jugador)
    print(mi_jugador.dado)
    print(mi_jugador.es_la_computadora)
    print(mi_jugador.contador)
    mi_jugador.incementar_contador()
    print(mi_jugador.contador)
    mi_jugador.decrementar_contador()
    print(mi_jugador.contador)

    print('*********** Ponemos a rodar el dado **********')
    print(mi_dado.valor)
    mi_jugador.rueda_el_dado()
    print(mi_dado.valor)

    # Otra forma de acceder a los atributos (Esta es la mas correcta)
    print('Accediendo mediante la clase a la clase agregada')
    print(mi_jugador.dado.valor)
    mi_jugador.rueda_el_dado()
    print(mi_jugador.dado.valor)
    