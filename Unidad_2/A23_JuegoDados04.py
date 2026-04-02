""" DESARROLLO DEL JUEGO"""

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
    
    def incrementar_contador(self):
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

    
class JuegoDeDados:

    def __init__(self, jugador, computadora):
        self._jugador = jugador
        self._computadora = computadora

    def jugar(self):
        print('==============================')
        print(' Bienvenido al juego de dados ')
        print('==============================')
        while True:
            self.jugar_partida()
            juego_terminado = self.checa_fin_de_juego()
            if juego_terminado:
                break

    def jugar_partida(self):
        # Bienvenida al ususario
        self.mostrar_bienvenida_juego()

        # Aventando los datos, llamamos indirectamente el método
        # rueda_el_dato() de la clase dato (agregación)
        puntos_jugador = self._jugador.rueda_el_dado()
        puntos_computadora = self._computadora.rueda_el_dado()

        # mostramos los valores de los dados
        self.muestra_contadores()

        # Mostrando los valores de los dados
        print(f'Tu dado {puntos_jugador}')
        print(f'dado de la computadora {puntos_computadora}')

        # Determinar el ganador y el perdedor
        if puntos_jugador > puntos_computadora:
            print('Ganaste el round!!')
            self.actualiza_contadores(ganador=self._jugador, perdedor=self._computadora)
        elif puntos_computadora > puntos_jugador:
            print('La computadora gano este round, intenta de nuevo')
            self.actualiza_contadores(ganador=self._computadora, perdedor=self._jugador)
        else:
            print('Es un empate')

    # Metodo para darla bienvenida
    def mostrar_bienvenida_juego(self):
        print('-------------- Nueva Partida --------------')
        input('Oprime cualquier tecla para aventar el dado ')

    # Mostrar los valores de los dados de cada jugador
    def mostrar_dados(self, valor_jugador, valor_computadora):
        print(f'Tu dado {valor_jugador}')
        print(f'dado de la computadora {valor_computadora}')

    # afecta los contadores del perdedor(le suma 1) y del ganador (le resta 1)
    def actualiza_contadores(self, ganador, perdedor):
        ganador.decrementar_contador()
        perdedor.incrementar_contador()

    # # Mostrar los contadores
    def muestra_contadores(self):
        print(f'Tu contador: {self._jugador.contador}')
        print(f'Contador de la computadora: {self._computadora.contador}')    

    # Verifica el fin del juego
    def checa_fin_de_juego(self):
        if self._jugador.contador == 0:
            self.muestra_juego_terminado(self._jugador)
            return True
        elif self._computadora.contador == 0:
            self.muestra_juego_terminado(self._computadora)
            return True
        else:
            return False
        
    def muestra_juego_terminado(self, ganador):
        if ganador._es_la_computadora:
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



# Creando instancias de los dados
dado_jugador = Dado()
dado_computadora = Dado()

# Creamos las instalcias de los jugadores
juego_humano = Jugador(dado_jugador, es_la_computadora=False)
juego_computadora = Jugador(dado_computadora, es_la_computadora=True)

# Creamos la instncia del juego
game = JuegoDeDados(juego_humano, juego_computadora)
game.jugar()                                # Iniciamos el juego
