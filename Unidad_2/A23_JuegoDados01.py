""" JUEGO DE DADOS

    ESPECIFICACIONES
    ----------------
    Hablemos un poco de la idea general del juego que vamos a crear.
    Va a ser un juego de dados, Vamos a tener que jugar a los dados y vamos 
    a tener dos jugadores, Uno de los jugadores representará al jugador 
    humano y el otro la computadora contra la que jugarás.
    Ambos jugadores se retan para ganar la partida, y ambos empezarán con 
    un total de diez puntos.

    El contador determinará quién gana la partida, en el juego tendremos dos 
    dados, cada jugador tendrá asociado un dado particular.

    En términos de programación orientada a objetos, cada dado será una 
    instancia y asociaremos cada jugador a cada instancia (un jugador por dado)
    haremos varias rondas tirando los dados hasta que alguien gane la partida 
    en cada ronda, cada uno de los jugadores tirará los dados y se anotará la 
    puntuación o el valor de los dados.
    Digamos tres y dos, por ejemplo, los dados pueden tomar enteros aleatorios 
    del 1 al 6, después de tirar los dados de esa ronda, compararemos los 
    valores.

    ¿El valor es mayor que otro, menor que otro?
    ¿O son iguales al jugador con mayor valor del momento?

    El jugador con el mayor valor en puntos gana el round (la ronda)
    En este caso, en nuestro ejemplo, sería tres gana la ronda y vamos a disminuir 
    el contador en uno para el jugador que gana la ronda y el jugador que pierde 
    tendrá el contador se incrementa en uno.
    Así que es como lo contrario de lo que se podría pensar inicialmente, uno 
    pensaría que si ganas la ronda, incrementamos el contador, pero en este caso lo 
    estamos incrementando y verás por qué en un segundo, recuerda, restamos uno.
    Si los valores son iguales, hay empate y no se modifican los contadores.
    Pasamos a la siguiente ronda y continuamos así en un proceso sin fin hasta que 
    uno de los contadores llegue a cero.

    El jugador cuya ficha llegue primero a cero gana la partida y todos contentos, 
    así que esperemos que seas tú.
    Si no, será el jugador del ordenador y tendrás que volver a desafiar al ordenador 
    si quieres ganar, después de eso, el juego habrá terminado y podrás empezar a 
    jugar de nuevo.
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
    

# Probando la clase
if __name__ == '__main__':
    mi_dado = Dado()

    # Forma UNO para obtener valores
    print(mi_dado.valor)
    mi_dado.rodar_dado()
    print(mi_dado.valor)
    mi_dado.rodar_dado()
    print(mi_dado.valor)
    mi_dado.rodar_dado()

    # Forma DOS para obtener valores
    nuevo_valor = mi_dado.rodar_dado()
    print(nuevo_valor)
    nuevo_valor = mi_dado.rodar_dado()
    print(nuevo_valor)
    nuevo_valor = mi_dado.rodar_dado()
    print(nuevo_valor)
    nuevo_valor = mi_dado.rodar_dado()
    print(nuevo_valor)

    # Forma TRES para obtener valores
    print(mi_dado.rodar_dado())
    print(mi_dado.rodar_dado())
    print(mi_dado.rodar_dado())
    
