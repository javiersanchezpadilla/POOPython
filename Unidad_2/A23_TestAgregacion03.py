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
    

class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print('==============================')
        print(' Bienvenido al juego de datos ')
        print('==============================')
        while True:
            self.play_round()


    def play_round(self):
        # Welcome to the user
        print('----------------- New Round ----------------')
        input('Oprime cualquier tecla para aventar el dado ')

        # Aventando los datos
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Mostrando los valores de los dados
        print(f'Tu dado {player_value}')
        print(f'dado de la computadora {computer_value}')

        # DEterminar el ganador y el perdedor
        if player_value > computer_value:
            print('Ganaste el round!!')
            self._player.decrement_counter()    # ganador
            self._computer.increment_counter()  # perdedor
        elif computer_value > player_value:
            print('LA computadora gano este round, intenta de nuevo')
            self._computer.decrement_counter()  # ganador
            self._player.increment_counter()    # perdedor
        else:
            print('Es un empate')

        # Mostrando los contadores
        print(f'Tu contador: {self._player.counter}')
        print(f'Contador de la computadora: {self._computer.counter}')


# Creando instancias
dado_jugador = Die()
dado_computadora = Die()

juego_humano = Player(dado_jugador, is_computer=False)
juego_computadora = Player(dado_computadora, is_computer=True)

game = DiceGame(juego_humano, juego_computadora)

# Iniciamos el juego
game.play()
