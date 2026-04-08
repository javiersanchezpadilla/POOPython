""" DIBUJO DE LA NAVE.

    Aqui vamos a incluir en el juego al heroe o personaje principal
    En esta caso será la nave que controlaremos
    Descargamos la nave en formato PNG en un tamaño de 64 bits
    no olvidar que nuestra pantalla es de 800x600, ademas el origen de
    las coordenadas se toman de la siguiente forma:

    Coordenada    Posicion
    (0, 0)      Esquina superior izquierda          0,0            800,0
    (800,0)     Esquina superior derecha
    (0, 600)    Esquina inferior izquierda
    (800, 600)  Esquina inferior derecha            0,600        800,600

        (0, 0)  +-----------------------+ (800, 0)
                |      (400, 300)       |
                |           +           |
                |                       |
        (0, 600)+-----------------------+ (800, 600)
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

# 1) Definimos la imagen del jugador y declaramos las /////////////////////////
#    coordenadas de despliegue en pantalla
img_jugador = pygame.image.load('nave02.png')
# 2) Coordenadas iniciales de la posicion de la nave ///////////////////////////
#    considerar el tamaño del icono 64 bits

# Para que aparezca a la mitad de la pantalla
jugador_x = 368     # 800/2=400  400-(64/2)=368
jugador_y = 536     # 600-64 = 536

# 3) Se declara la funcion para lanzar la imagen del jugador ///////////////////
def jugador():
    # Lanza la imgen a pantalla
    pantalla.blit(img_jugador, (jugador_x, jugador_y))


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # se movio el relleno de la pantalla 
    pantalla.fill((205, 144, 228))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    jugador()

    
    pygame.display.update()