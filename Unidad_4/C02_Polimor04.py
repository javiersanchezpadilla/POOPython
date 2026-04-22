""" POLIMORFISMO (Ejercicio: 'El Sistema de Movimiento Universal')

    En este ejercicio se integrará Herencia (para no repetir código) 
    y Polimorfismo (para manejar todo de forma uniforme).

    Vamos a diseñar una 'Invasión Espacial'. 
    El objetivo es entender que podemos tener una lista con 100 enemigos 
    distintos y moverlos a todos con una sola línea de código.

    EL EJERCICIO SOLO ES CONCEPTUAL PARA MOSTRAR LA FUNCIONALIDAD SE PUEDE
    REALIZAR, PERO DE MOMENTO SOLO ES CONCEPTUAL.

    Reto:
    -----
    Añadir un nuevo tipo de enemigo llamado JefeFinal que herede de Alienigena
    **) La condición: El JefeFinal debe moverse solo de izquierda a derecha 
        pero disparar (imprimir un mensaje en consola) cada vez que se mueve.
    **) La pregunta clave: ¿Tuvieron que cambiar el ciclo for principal para 
        que el jefe funcionara?

    Respuesta: No, porque el jefe también es un Alienigena y tiene el método 
    mover().

    ¿Por qué este ejercicio funciona?
    Les enseña a los estudiantes a desacoplar la lógica. El 'Motor de 
    Movimiento' no necesita saber cómo se mueve cada bicho; esa responsabilidad
    es de cada clase individual. Esto hace que el código sea modular y fácil 
    de expandir.

"""
import pygame

# 1. La Base (Herencia)
#    Primero definimos qué tienen en común todos los alienígenas.
class Alienigena(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def mover(self):
        """Método que será polimórfico"""
        pass

# 2. Las Variaciones (Polimorfismo)
#    Aquí es donde cada hijo define su propia "forma" de moverse.
class Marciano(Alienigena):
    def mover(self):
        # Movimiento horizontal simple
        self.rect.x += 2

class Kamikaze(Alienigena):
    def mover(self):
        # Movimiento diagonal rápido hacia abajo
        self.rect.x += 3
        self.rect.y += 3

class Bobo(Alienigena):
    def mover(self):
        # Movimiento errático (zigzag)
        import random
        self.rect.x += random.choice([-5, 5])

# 3. La ejecución polimórfica (El Motor del Juego)
#    Aquí es donde se demuestra el poder del concepto. 
#    No importa qué tipo de alienígena sea, todos responden al comando 
#    .mover().
# Creamos una lista mixta (un ejército polimórfico)
ejercito = [
    Marciano(100, 50, (0, 255, 0)),
    Kamikaze(200, 50, (255, 0, 0)),
    Bobo(300, 50, (0, 0, 255))
]

# En el ciclo principal de Pygame:
running = True
while running:
    for alien in ejercito:
        # AQUÍ ESTÁ EL POLIMORFISMO:
        # 'alien' puede ser Marciano, Kamikaze o Bobo.
        # No nos importa cuál sea, solo sabemos que todos tienen .mover()
        alien.mover()



