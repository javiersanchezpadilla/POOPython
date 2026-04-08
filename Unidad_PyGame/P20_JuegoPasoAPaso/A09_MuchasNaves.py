""" CREACIÓN DE MUCHAS NAVES.

    El objetivo es que no sea un solo enemigo, con la misma logica debemos 
    hacer que ahora se aplique a un numero mayor de enemigos,para resolverlo 
    ya que no estamos trabajando objetos, sera el crear una lista donde cada 
    elemento de la lista será un enemigo, por lo que donde se trabajara es 
    donde se declararon las variables para los enemigos
"""
import pygame
import random
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


# 1) AQUI COMIENZA TODO!!!!! Concertimos las variables en listas //////////////////////////////////
# Definimos las variables para control de los enemigos ////////////////////////////////////////////
# creacion de las listas (preparamos las variables para que sean listas) //////////////////////////
img_malote = []
malote_x = []
malote_y = []
malote_x_cambio = []
malote_y_cambio = []
cantidad_enemigos = 8   # nueva variable para los enemigos

# Generamos cada uno de los enemigos
for creaMalotes in range(cantidad_enemigos):
    img_malote.append(pygame.image.load('ovni.png'))
    malote_x.append(random.randint(0, 736))   # ancho de pantalla - tamaño ovni
    malote_y.append(random.randint(50, 200))
    malote_x_cambio.append(0.8)   # Factor de cambio en X
    malote_y_cambio.append(50)    # Factor de cambio en Y para una vuelta completa


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

# 3) MODIFICAMOS LA FUNCION PARA EL PARAMETRO DE REFERENCIA DEL INDICE DE LA LISTA ///////////////////////
# Funcion para los enemigos
def enemigo(posMalote_X, posMalote_Y, ene):
    pantalla.blit(img_malote[ene], (posMalote_X, posMalote_Y))


# Funcion para disparo de la bala
def disparar_bala(posBala_X, posBala_Y):
    global bala_visible
    bala_visible = True                 # 16 y 10 tiene que ver con el tamaño de la nave
    pantalla.blit(img_bala, (posBala_X + 16, posBala_Y + 10))


# control de los puntos acumulados por cada enemigo destruido
puntaje = 0


#  Funcion para la deteccion de las colisiones
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
    # 2) referenciamos a cada uno de los enemigos ////////////////////////////////////////////////////
    #    ademas las condiciones de los limites deben entrar en el FOR, por
    #    que deben alinearse tamnien y agregar el indicador de lista con su indice
    # Tambien hay que agregar dentro la verificacion de las colisicones dentro del FOR
    # por ultimo mover dentro del FOR la llamada de nuestro enemigo y modificarla
    for e in range(cantidad_enemigos):
        malote_x[e] += malote_x_cambio[e]

        # Mantener los limites de las naves enemigas POR CADA ENEMIGO /////////////////////////////////
        if malote_x[e] <= 0:             
            malote_x_cambio[e] = 0.6     
            malote_y[e] += malote_y_cambio[e]
        elif malote_x[e] >= 768:         
            malote_x_cambio[e] = -0.6    
            malote_y[e] += malote_y_cambio[e]

        # verificamos si existe colision entre el enemigo y la bala /////////////////////////////////////
        colision = hay_colision(malote_x[e], malote_y[e], bala_x, bala_y)

        if colision:                            # Si hay colision se debe:
            bala_y = 500                        # Inicializamos la posicion de la bala
            bala_visible = False                # ocultamos la bala
            puntaje += 1                        # Aumentamos el puntaje
            malote_x[e] = random.randint(0, 736)   # reiniciamos otro ovni nuevo tanto en X
            malote_y[e] = random.randint(50, 200)  # como en la posicion Y

        # Funcion para cargar a los enemigos,  ////////////////////////////////////////////////////////
        # AHORA DEBE MODIFICARSE PARA ACEPTAR UN NUEVO ARGUMENTO LLAMADO E
        enemigo(malote_x[e], malote_y[e], e)


    # Movimiento de la bala
    if bala_y <= -64:       # 64 pixeles mide la bala
        bala_y = 500        # Regresamos la altura inicial de la bala
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    # Funcion para cargar nuestra nave o heroe
    jugador(jugador_x, jugador_y)


    # Actualizar la pantalla grafica
    pygame.display.update()
    