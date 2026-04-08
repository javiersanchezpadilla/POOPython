""" MOVIMIENTO DE LA NAVE.

    Aqui vamos a hacer uso ya de las flechas para representar el movimiento
    del personaje (nave) ya en la pantalla
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

# 1) Agregamos una variable para controlar el factor de cambio ///////////////////////
#    para el movimiento de la imagen 
#     0.0   = no se mueve 
#    -0.3   = se mueve a la izquierda 
#     0.3   = se mueve a la derecha
jugador_x_cambio = 0


# Agregar parametros a la funcion para el movimiento dinamico
def jugador(posNave_X, posNave_Y):
    pantalla.blit(img_jugador, (posNave_X, posNave_Y))


# * LOOP DEL JUEGO ********
se_ejecuta = True
while se_ejecuta:
    pantalla.fill((205, 144, 228))
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:

            # 2) Cuando el usuario oprime la flecha a la izquierda cambia el factor a -0.3 //////////////////
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            # 3) Cuando el usuario oprime la flecha a la derecha cambia el factor a 0.3 //////////////////////
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3

        # 4) Cuando el usuario suelta la tecla deja de moverse el factor = 0 ////////////////////////////////
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.0


    # 5) modificamos los valores de la variable aumentando el factor ///////////////////////////
    jugador_x += jugador_x_cambio
    jugador(jugador_x, jugador_y)

    
    pygame.display.update()