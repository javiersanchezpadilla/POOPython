""" PERSONALIZACIÓN DE LA VENTANA DE TRABAJO.

    Aqui vamos a personalizar el icono de la ventana, el color de fondo de la 
    ventana y el icono de la ventana
"""

import pygame

# Inicializar
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

# 1) Titulo de la ventana //////////////////////////////////////////////////
pygame.display.set_caption('Invasion Extraterrestre')

# 2) Para buscar iconos podemos buscar en flaticon.com ////////////////////
#    la extension sera PNG y el tamaño 32 pixeles
#    En linux por el estilo del escritorio no se aprecia el icono
#    pero en windows si debe apreciarse
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)



# Loop del juego
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    # 3) como parte de los eventos debemos indicar el color de  //////
    #    fondo para que se redibuje la pantalla siempre
    pantalla.fill((205, 144, 228))
    # 4) ahora le damos la orden para que se actualice
    pygame.display.update()