""" CREAR LA PANTALLA GRAFICA.

    Primer pantalla Grafica con PyGame
    Este codigo permite crear la pantalla de trabajo y permitir reptir el 
    ciclo infinito para Escuchar los eventos de teclado.
    No olvidar como primer paso la instalacion de la libreria  pygame
    
    $ pip install pygame
"""

import pygame

# 1) Inicializamos pyGame dentro del programa ////////////////////////////////
pygame.init()

# 2) Establecemos el tamaño de la pantalla  ///////////////////////////////////
#    en una tupla en este caso es de 800x600
#    Esta parte solo crea la pantalla y la cierra inmediatamente
pantalla = pygame.display.set_mode((800,600))


# 3) Creamos un ciclo infinito para detener que cierre la ventana  ////////////
#    Este es un LOOP INFINITO que captara los eventos
#    Quit es el evento de la "X" en la esquina sup derecha de la ventana

se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False