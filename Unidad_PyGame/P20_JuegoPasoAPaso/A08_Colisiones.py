""" MANEJO DE COLISIONES.

    El objetivo es que cuando la bala impacte al enemigo este sea destruido
    DISTANCIA ENTRE DOS PUNTOS
        ____________________________
    D = / (X2 - X1)**2 + (Y2 - Y1)**2

    Requerimos del modulo math
"""
import pygame
import random

# 1) importamos el modulo MATH ///////////////////////////////////////////////
import math

# Inicializar
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

# Titulo de la ventana y cambio de icono de la ventana
pygame.display.set_caption('Invasion Extraterrestre')
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)


# VARIABLES PARA CARGAR LAS IMAGENES Y DECLARACION
# DE LAS VARIABLES PARA CADA MIEMBRO DEL JUEGO
# **************************************************


# Definicion de la variable para cargar el fondo
fondo = pygame.image.load('Fondo.jpg')


# Definimos la imagen del jugador y posicion inicial
img_jugador = pygame.image.load('nave02.png')
jugador_x = 368     # 800/2=400  400-(64/2)=368
jugador_y = 536     # 600-64 = 536
jugador_x_cambio = 0  # factor de cambio


# Definimos las variables para control de los enemigos
img_malote = pygame.image.load('ovni.png')
malote_x = random.randint(0, 736)   # ancho de pantalla - tamaño ovni
malote_y = random.randint(50, 200)
malote_x_cambio = 0.8   # Factor de cambio en X
malote_y_cambio = 50    # Factor de cambio en Y para una vuelta completa


# Definimos las variables para control de los disparos (la bala)
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500            # posicion inicial de la bala en Y
bala_x_cambio = 0       # Factor de cambio en X
bala_y_cambio = 1       # Velocidad de la bala
bala_visible = False    # Para ver o no la bala (se ve solo en el disparo)

# *******************************
# DEFINICIO DE LAS FUNCIONES ****
# *******************************

# Agregar parametros a la funcion para el movimiento dinamico
def jugador(posNave_X, posNave_Y):
    pantalla.blit(img_jugador, (posNave_X, posNave_Y))


# Funcion para los enemigos
def enemigo(posMalote_X, posMalote_Y):
    pantalla.blit(img_malote, (posMalote_X, posMalote_Y))


# Funcion para disparo de la bala
def disparar_bala(posBala_X, posBala_Y):
    global bala_visible
    bala_visible = True                 # 16 y 10 tiene que ver con el tamaño de la nave
    pantalla.blit(img_bala, (posBala_X + 16, posBala_Y + 10))


# 4) VARIABLE PARA CONTROL DEL PUNTAJE //////////////////////////////////////////////////
# control de los puntos acumulados por cada enemigo destruido
puntaje = 0


# 2) CREACION DE LA funcion para Detectar colisiones ////////////////////////////////////
def hay_colision (x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False


# *************************
# * LOOP DEL JUEGO ********
# *************************

se_ejecuta = True
while se_ejecuta:

    # Cargamos la imagen de fondo
    pantalla.blit(fondo, (0,0))
   
    # Iterar los eventos del juego
    for evento in pygame.event.get():
        # Evento para SALIR del juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # CONTROL DE EVENTOS DEL TECLADO ***********
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.6     # Factor de cambio en X avance a la izquierda
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.6      # Factor de cambio en X avance a la derecha

            # Evento del disparo de la bala tecla BARRA ESPACIADORA
            if evento.key == pygame.K_SPACE:
                if not bala_visible:  
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)     

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.0

    # ******************************************
    # MANIPULACION DEL MOVIMIENTO DE LOS OBJETOS
    # ******************************************

    # Modificar la ubicacion del jugador
    jugador_x += jugador_x_cambio

    # Mantener los limites de la nave dentro de la pantalla
    if jugador_x <= 0:      # 0 es el origen por lo que no importa el tamaño
        jugador_x = 0       # de la imagen de la nave
    elif jugador_x >= 736:  # 800 - 64 pixeles de la nave = 736
        jugador_x = 736

    # Creamos las condiciones para los enemigos
    malote_x += malote_x_cambio

    # Mantener los limites de las naves enemigas
    if malote_x <= 0:               # 0 es el origen por lo que no importa el tamaño
        malote_x_cambio = 0.6       # Factor de cambio en X avance a la derecha
        malote_y += malote_y_cambio
    elif malote_x >= 768:           # 800 - 32 pixeles de la nave = 768
        malote_x_cambio = -0.6      # Factor de cambio en X avance a la izquierda
        malote_y += malote_y_cambio

    # Movimiento de la bala
    if bala_y <= -64:       # 64 pixeles mide la bala
        bala_y = 500        # Regresamos la altura inicial de la bala
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # 3) VERIFICACION DE LA COLISION /////////////////////////////////////////////////////
    # verificamos si existe colision entre el enemigo y la bala
    colision = hay_colision(malote_x, malote_y, bala_x, bala_y)
    # 4) Que se hace una vez detectada la colision?
    if colision:
        bala_y = 500                        # Inicializamos la posicion de la bala
        bala_visible = False                # ocultamos la bala
        puntaje += 1                        # Aumentamos el puntaje
        print(puntaje)                      # solo por probar en la pantalla
        malote_x = random.randint(0, 736)   # reiniciamos otro ovni nuevo tanto en X
        malote_y = random.randint(50, 200)  # como en la posicion Y


    # Funcion para cargar nuestra nave o heroe
    jugador(jugador_x, jugador_y)

    # Funcion para cargar a los enemigos
    enemigo(malote_x, malote_y)

    # Actualizar la pantalla grafica
    pygame.display.update()
    