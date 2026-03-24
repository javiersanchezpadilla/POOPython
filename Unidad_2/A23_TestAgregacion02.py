""" 
"""

import random

# Pondremos a prueba el concepto de agregación

class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value
    

class Player:

    # los atributos seran solo de lectura
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        valor_calculado = self._counter + 1
        self._counter = valor_calculado
        return valor_calculado

    def decrement_counter(self):
        valor_calculado = self._counter - 1
        self._counter = valor_calculado
        return valor_calculado
    
    def roll_die(self):
        return self._die.roll()
    

# Probamos la declaracion de la clase
if __name__ == "__main__":
    mi_dado = Die()
    mi_jugador = Player(mi_dado, True)
    # Aqui podemos comprobar que son instancias diferentes con distintas
    # asignaciones de memoria
    print(mi_jugador)
    print(mi_jugador.die)
    print(mi_jugador.is_computer)
    print(mi_jugador.counter)
    mi_jugador.increment_counter()
    print(mi_jugador.counter)
    mi_jugador.decrement_counter()
    print(mi_jugador.counter)

    print('*********** Ponemos a rodar el dado **********')
    print(mi_dado.value)
    mi_jugador.roll_die()
    print(mi_dado.value)

    # Otra forma de acceder a los atributos (Esta es la mas correcta)
    print('Accediendo mediante la clase a la clase agregada')
    print(mi_jugador.die.value)
    mi_jugador.roll_die()
    print(mi_jugador.die.value)
    