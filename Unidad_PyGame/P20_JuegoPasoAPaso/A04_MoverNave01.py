""" MOVER NAVE.

    Aqui vamos a Permitir mediant el uso de las flechas mover el personaje
    principal que es nuestra nave
    Vamos a aprender la dinamica del movimiento del personaje
    primero identificaremos cuando el usuario oprime la tecla ya sea izquierda 
    o derecha de igual manera identificaremos cuando el usuario suelta la 
    tecla izq. o derecha.
    Los resultados los podemos ver en la pantalla de la consola ya que se 
    cuenta con un print(), el objetivo solo en esender como se detecta el
    evento del movimiento.
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


# 1) Le vamos a agregar parametros a la funcion para que /////////////////////////////
#    el personaje se mueva dinamicamente
def jugador(posNave_X, posNave_Y):
    pantalla.blit(img_jugador, (posNave_X, posNave_Y))

# *******************************************
# ***     LOOP DEL JUEGO     ****************
# *******************************************
se_ejecuta = True
while se_ejecuta:
    pantalla.fill((205, 144, 228))

   # jugador_x+=0.1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # 3) Detectamos el evento de una tecla presionada //////////////////////////////
        if evento.type == pygame.KEYDOWN:
            print('Una tecla fue presionada')
            # identificacion de si es la flecha IZQUIERDA
            if evento.key == pygame.K_LEFT:
                print('Flecha izquerda presionada')
            # identificacion de si es la flecha DERECHA
            if evento.key == pygame.K_RIGHT:
                print('Flecha derecha presionada')

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                print('La tecla izquierda o derecha fue soltada')



    # 2) agregamos los argumentos a la llamada de la funcion ///////////////////////////
    jugador(jugador_x, jugador_y)

    
    pygame.display.update()