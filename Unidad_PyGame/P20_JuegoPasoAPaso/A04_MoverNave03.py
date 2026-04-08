""" MOVIMIENTO DE LA NAVE CON LIMITES DE LA PANTALLA.

    Se estableceran limites en la pantalla para la nave, en este momento si 
    dejamos oprimida cualquiera de las teclas, ya sea izquierda o derecha la 
    Nave continua, por lo que ahora se estableceran limites entre 0 y 800
"""

import pygame

# Inicializar
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

# Titulo de la ventana y cambio de icono de la ventana
pygame.display.set_caption('Invasion Extraterrestre')

icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Definimos la imagen del jugador y posicion inicial
img_jugador = pygame.image.load('nave02.png')
jugador_x = 368     # 800/2=400  400-(64/2)=368
jugador_y = 536     # 600-64 = 536

# Agregamos una variable para controlar el factor de cambio
jugador_x_cambio = 0


# Agregar parametros a la funcion para el movimiento dinamico
def jugador(posNave_X, posNave_Y):
    pantalla.blit(img_jugador, (posNave_X, posNave_Y))


# * LOOP DEL JUEGO ********
se_ejecuta = True
while se_ejecuta:
    pantalla.fill((205, 144, 228))
   
    # Iterar los eventos del juego
    for evento in pygame.event.get():
        # Evento para SALIR del juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.0

    # Modificar la ubicacion del jugador
    jugador_x += jugador_x_cambio

    # 1) mantener la nave dentro de los bordes de la pantalla //////////////////////////////////
    if jugador_x <= 0:      # 0 es el origen por lo que no importa el tamaño
        jugador_x = 0       # de la imagen de la nave
    elif jugador_x >= 736:  # 800 - 64 pixeles de la nave = 736
        jugador_x = 736

    jugador(jugador_x, jugador_y)

    # Actualizar la pantalla grafica
    pygame.display.update()
    