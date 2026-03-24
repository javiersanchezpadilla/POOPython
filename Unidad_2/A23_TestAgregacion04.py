""" 

"""

import random

# Pondremos a prueba el concepto de agregación

class Dado:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value
    

class Jugador:

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
    

class JuegoDados:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print('==============================')
        print(' Bienvenido al juego de datos ')
        print('==============================')
        print("\U0001F1FD")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome to the user
        self.print_round_welcome()        

        # Aventando los datos
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Mostrando los valores de los dados
        self.show_dice(player_value, computer_value)

        # DEterminar el ganador y el perdedor
        if player_value > computer_value:
            print('Ganaste el round!!')
            self.update_counters(winner=self._player, loser=self._computer)
        elif computer_value > player_value:
            print('LA computadora gano este round, intenta de nuevo')
            self.update_counters(winner=self._computer, loser=self._player)
        else:
            print('Es un empate')

        # Mostrando los contadores
        self.show_counters()

    # Metodo para darla bienvenida
    def print_round_welcome(self):
        print('----------------- New Round ----------------')
        input('Oprime cualquier tecla para aventar el dado ')

    # Mostrar los valores de los dados de cada jugador
    def show_dice(self, player_value, computer_value):
        print(f'Tu dado {player_value}')
        print(f'dado de la computadora {computer_value}')

    # afecta los contadores del perdedor y disminuye el del ganador
    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    # Mostrar los contadores
    def show_counters(self):
        print(f'Tu contador: {self._player.counter}')
        print(f'Contador de la computadora: {self._computer.counter}')

    # Verifica el fin del juego
    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False
        
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n====================")
            print("  G A M E   O V E R")
            print("=====================")
            print("La computadora gano el juego. Lo siento")
            print("=======================================")
        else:
            print("\n====================")
            print("  G A M E   O V E R")
            print("=====================")
            print("Ganaste el juego, felicidades!!!!")
            print("=================================")
        

# Creando instancias
dado_jugador = Dado()
dado_computadora = Dado()

juego_humano = Jugador(dado_jugador, is_computer=False)
juego_computadora = Jugador(dado_computadora, is_computer=True)

game = JuegoDados(juego_humano, juego_computadora)

# Iniciamos el juego
game.play()
