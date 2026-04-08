""" CARGAR EL FONDO DEL JUEGO.

    En este tema se agregará el fondo del juego, la idea es cargar una imagen 
    que se mantenga al fondo del juego.
    Podemos buscar imagenes en freepik.com, una vez descargada es necesario 
    redimensionarla.
    Recordemos que nuestra ventana es de 800x600, por lo que la imagen debe ser 
    de 800x600.

    MUY IMPORTANTE!!! como ahora se carga la imagen de fondo en cada iteracion 
    la ejecucion del juego se  vuelve mas lenta por lo que vamos aumentar la 
    velocidad de 0.3 a 0.6
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

# 1) DEfinimos la variable para cargar el fondo ////////////////////////////////
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

malote_x_cambio = 0.8   # <--- Se aumento la velocidad para compensar 
malote_y_cambio = 50    # Factor de cambio en Y para una vuelta completa

# Agregar parametros a la funcion para el movimiento dinamico
def jugador(posNave_X, posNave_Y):
    pantalla.blit(img_jugador, (posNave_X, posNave_Y))


# Funcion para los enemigos
def enemigo(posMalote_X, posMalote_Y):
    pantalla.blit(img_malote, (posMalote_X, posMalote_Y))


# * LOOP DEL JUEGO ********
se_ejecuta = True
while se_ejecuta:

    # 2) Ahora en lugar de cargar la imagen de color cargamos la imagen ////////////////////////////
    # pantalla.fill((205, 144, 228))   Esta linea ya no se va a ocupar
    pantalla.blit(fondo, (0,0))
   
    # Iterar los eventos del juego
    for evento in pygame.event.get():
        # Evento para SALIR del juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.6     # <--- Se aumento la velocidad para compensar //////////////////
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.6      # <--- Se aumento la velocidad para compensar //////////////////

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

    # Creamos las condiciones para los enemigos
    malote_x += malote_x_cambio

    # Mantener los limites de las naves enemigas
    if malote_x <= 0:               # 0 es el origen por lo que no importa el tamaño
        malote_x_cambio = 0.6       # <--- Se aumento la velocidad para compensar  //////////////
        malote_y += malote_y_cambio
    elif malote_x >= 768:           # 800 - 32 pixeles de la nave = 768
        malote_x_cambio = -0.6      # <--- Se aumento la velocidad para compensar ///////////////
        malote_y += malote_y_cambio



    # Funcion para cargar nuestra nave o heroe
    jugador(jugador_x, jugador_y)

    # Funcion para cargar a los enemigos
    enemigo(malote_x, malote_y)

    # Actualizar la pantalla grafica
    pygame.display.update()
    