""" JUEGO DE NAVE ESPACIAL

    RECURSOS:
    =========
    https://www.flaticon.es/    PAra iconos e imagenes libres


    CONSIDERACIONES:
    ================
    1)  Esta primer versión es sin trabajar orientado a objetos
    2)  LA pantalla de acuerdo a la resolución por ejemplo en este programa
        que es 800 x 600 nos da un eje de coordenadas donde el origen es la 
        posicion de la esquina superior izquierda de la ventana.
        
        (0, 0)  +-----------------------+ (800, 0)
                |      (400, 300)       |
                |           +           |
                |                       |
        (0, 600)+-----------------------+ (800, 600)
    3)  No exceder los limites de la pantalla, la pantalla es de 800x600 y 
        las imagenes de la nave y los enemigos son de 64x64, así la minima
        posición del lado izquierdo es 0, del lado derecho es 800-64 = 736,
        de la posicion superior es 0, de la posición inferior es 600-64 = 536
        lo anterior para desplegar las imagenes ya sea del enemigo o del heroe

    DESARROLLO DEL PROGRAMA:
    ========================

    P1 PARTE 1
    ----------
    Se inicializa pygame, se declara el tamaño de la pantalla, se
    ejecuta un ciclo while infinito donde dentro se verifican los
    eventos de la pantalla

    P2 PARTE 2
    -----------
    Personalizar la pantalla, cambiar el nombre de la ventana, cambiar
    el icono y el color de fondo (descargar icono a 32 bits)

    P3 PARTE 3
    ----------
    Agregar al protagonista (la nave, la descargamos a 64 bits)
    Se debe respetar en todo momento la posicion de la imagen y no exceder
    los limites de la misma, la pantalla es de 800x600 la imagen de la nave
    es de 64x64

    P4 PARTE 4
    ----------
    Controlar el movimiento de nuestra nave mediante el teclado usando las
    flechas izq., der. se tomara el control mediante los siguientes eventos

    if evento.type == pygame.KEYDOWN:   Detecta que se oprimio una tecla
    if evento.key == pygame.K_LEFT:     Si tecla es la flecha izq
    if evento.key == pygame.K_RIGHT:    Si tecla es la flecha der.
    if evento.type == pygame.KEYUP:     Detecta justo cuando se suelta la tecla

    También delimita los bordes de la pantalla para que la nave no rebase

    P5 PARTE 5
    ----------
    Creación de los enemigos (64 bits) en posiciones aleatorias de la pantalla
    respetando la resolución y el tamaño de la imagen para no exceder los 
    limites de la pantalla la pantalla es de 800x600 y la imagen del enemigo 
    es de 64x64.

    P6 PARTE 6
    ----------
    Generar el movimiento de los enemigos. El movimiento es automatico, se 
    debe desplazar de izquierda a derecha y de derecha a izquierda, pero 
    cuando toque uno de los bordes debera bajar 50 pixeles.

    P7 PARTE 7
    ----------
    Agrega el fondo de la pantalla, se reemplaza el color solido por una
    imagen de fondo, no siempre las imagenes encontradas se ajustan a nuestra
    pantalla, para corregir esto se puede usar un editor de imagenes para 
    ajustar el tamaño de la imagen a la ventana en nuestro caso 800x600

    P8 PARTE 8
    ----------
    Disparar las balas

"""


import pygame
import random

# P1 Inicializamos PyGame
pygame.init()
pantalla = pygame.display.set_mode((800, 600))  # P1 Inicializamos la pantalla

# P2 Titulo de la pantalla
pygame.display.set_caption("Invasión espacial")

# P2 para mostrar el icono en la ventana
ruta_icono = '/home/javier/Documentos/Programas/Python/GameFede/alienicono.png'
icono = pygame.image.load(ruta_icono)
pygame.display.set_icon(icono)


# P7 definicion de la imagen de fondo para nuesra ventana
ruta_fondo = '/home/javier/Documentos/Programas/Python/GameFede/Fondo.jpg'
fondo = pygame.image.load(ruta_fondo)



# P3 Dibujamos al heroe protagonista y jugador
# ---------------------------------------------
ruta_heroe = '/home/javier/Documentos/Programas/Python/GameFede/cohete.png'
img_jugador = pygame.image.load(ruta_heroe)
# Ubicación de la nave principal, recordar que mi resolución es 800x600
jugador_x = 368     # 800(largo pantalla) - 64(ancho imagen) = 736 / 2 = 368
jugador_y = 536     # 600(alto pantalla) - 64(alto imagen) = 536
jugador_x_cambio = 0    # P4 para controlar el movimiento izq. o der.


# P5 Dibujamos al enemigo
# ---------------------------------------------
ruta_enemigo = '/home/javier/Documentos/Programas/Python/GameFede/enemigo.png'
img_enemigo = pygame.image.load(ruta_enemigo)
# Ubicación de la nave principal, recordar que mi resolución es 800x600
enemigo_x = random.randint(0, 736) 
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.3      # P5 para controlar movimiento izq. o der.
enemigo_y_cambio = 50       # P5 PAra controlar movimiento arriba abajo


# P8 Dibujamos la bala
# ---------------------------------------------
ruta_bala = '/home/javier/Documentos/Programas/Python/GameFede/bala.png'
img_bala = pygame.image.load(ruta_bala)
# Ubicación de la bala
bala_x = 0
bala_y = 500
bala_x_cambio = 0       # P5 para controlar movimiento izq. o der.
bala_y_cambio = 1       # P5 PAra controlar movimiento arriba abajo
bala_visible = False




# P3 funcion para dibujar al protagonista en la posición actual
def jugador(pos_x, pos_y):
    pantalla.blit(img_jugador, (pos_x, pos_y))


# P5 funcion para dibujar al enemigo
def enemigo(pos_x, pos_y):
    pantalla.blit(img_enemigo, (pos_x, pos_y))



se_ejecuta = True
while se_ejecuta:                       # P1 Loop del juego

    # P2 Determinamos el color de fondo de la pantalla
    #    primero dibujamos la pantalla antes que todo para que los personajes 
    #    se dibujen arriba de la pantalla, de lo contrario si dibujamos un 
    #    personaje antes, al dibujar la pantalla borraria los personajes
    #pantalla.fill((205, 144, 228))

    # P7 lanzamos la imagen de fondo para la pantalla, ya no es necesario
    #    cargar la pantalla anterior
    pantalla.blit(fondo, (0, 0))


    for evento in pygame.event.get():   # P1 Control de los eventos
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # P4 si el evento es una tecla presionada
        if evento.type == pygame.KEYDOWN:   
            # print('Una tecla fue presionada')

            if evento.key == pygame.K_LEFT:     # P4 se oprimio la flecha izq
                # print('Flecha izquierda presionada')
                jugador_x_cambio = -0.3         # P4 se mueve a la izquierda 

            if evento.key == pygame.K_RIGHT:    # P4 se oprimio la flecha der
                # print('Flecha derecha presionada')
                jugador_x_cambio = 0.3          # P4 se mueve a la derecha

        # P4 si el evento es una tecla liberada (al momento de soltarla)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print('La tecla fue soltada')
                jugador_x_cambio = 0            # P4 Deja de moverse


    # P4 afectamos las coordenadas de la posicion de la nave para que al
    #    momento de dibujarla se desplace a la nueva posición
    jugador_x += jugador_x_cambio

    # P4 restringe la posición de la nave a los limites de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:  # 800 (ancho pantalla) - 64 (ancho imagen) = 736
        jugador_x = 736


    # P5 afectamos las coordenadas de la posicion del enemigo
    #    momento de dibujarla se desplace a la nueva posición
    enemigo_x += enemigo_x_cambio

    # P5 restringe la posición de la nave a los limites de la pantalla
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:  # 800 (ancho pantalla) - 64 (ancho imagen) = 736
        enemigo_x_cambio = -0.3
        enemigo_y += enemigo_y_cambio


    # P3 llamamos a la función para mostrar la posición del jugador
    # jugador_x += 0.1 # como demostración
    jugador(jugador_x, jugador_y)

    # P5 Llamamos a la funcion para mostrar la posicion del enemigo
    enemigo(enemigo_x, enemigo_y)

    # P2 para mostrar el color debemos actualizar la pantalla
    pygame.display.update()

