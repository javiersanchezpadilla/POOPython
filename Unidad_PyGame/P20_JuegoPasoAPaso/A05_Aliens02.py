""" MOVIMIENTO DEL ENEMIGO.

    Asignando movimiento a las naves enemigas, el movimiento no es asignado 
    por el usuario, así que lo debe asignar el código de izquierda a derecha
    y en cada vuelta completa la nave debe bajar
"""

import pygame
import random 

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
jugador_x_cambio=0  # factor de cambio


# Definimos las variables para control de los enemigos
img_malote = pygame.image.load('ovni.png')
malote_x = random.randint(0, 736)   # ancho de pantalla - tamaño ovni
malote_y = random.randint(50, 200)

malote_x_cambio = 0.3   # 1) Factor de cambio en X para las naves enemigas ///////////////////////////
malote_y_cambio = 50    # 2) Factor de cambio en Y para una vuelta completa ////////////////////////////

# Agregar parametros a la funcion para el movimiento dinamico
def jugador(posNave_X, posNave_Y):
    pantalla.blit(img_jugador, (posNave_X, posNave_Y))


# Funcion para los enemigos
def enemigo(posMalote_X, posMalote_Y):
    pantalla.blit(img_malote, (posMalote_X, posMalote_Y))


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

    # Mantener los limites de la nave dentro de la pantalla
    if jugador_x <= 0:      # 0 es el origen por lo que no importa el tamaño
        jugador_x = 0       # de la imagen de la nave
    elif jugador_x >= 736:  # 800 - 64 pixeles de la nave = 736
        jugador_x = 736

    # 3) CREAMOS LAS CONDICIONES PARA LOS ENEMIGOS //////////////////////////////////////////////
    malote_x += malote_x_cambio

    # 4) Controlamos los desplazamientos de las naves, en cada limite desplaza la /////////////////////////
    #    la nave hacia abajo para que tambien avance hacia abajo.
    # Mantener los limites de las naves enemigas
    if malote_x <= 0:               # 0 es el origen por lo que no importa el tamaño
        malote_x_cambio = 0.3       # de la imagen de la nave
        malote_y += malote_y_cambio
    elif malote_x >= 768:           # 800 - 32 pixeles de la nave = 768
        malote_x_cambio = -0.3
        malote_y += malote_y_cambio



    # Funcion para cargar nuestra nave o heroe
    jugador(jugador_x, jugador_y)

    # Funcion para cargar a los enemigos
    enemigo(malote_x, malote_y)

    # Actualizar la pantalla grafica
    pygame.display.update()
    