""" JUEGO DE NAVE ESPACIAL

    REQUERIMIENTOS:
    ===============
    pip install pygame                  Desde la consola ejecutar el comando
                                        para la instalación de la libreria 
                                            
    RECURSOS:
    =========
    https://www.1001freefonts.com/      Fuentes de texto
    https://www.flaticon.es/            Iconos e imagenes libres

    
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
    Disparar las balas, las consideraciones son: la bala debe salir desde 
    donde se encuentra la nave (no importa la posición), al disparar las 
    balas deben seguir su trayectoria o mantener su dirección de forma 
    independiente a la nave, es decir que cuando se dispara, sin importar
    que la nave siga moviendose la bala traza su propia ruta hasta el 
    destino (llegar al final de la pantalla o impactar una nave enemiga),
    la tecla que usaremos para el control del disparo será la barra 
    espaciadora (dentro del grupo de teclas presionadas).

    P9 PARTE 9
    ----------
    Control de las colisiones de las balas con las naves (detección de 
    colisiones), calculamos la distancia mínima de colisión
    Formula para calcular la distancia entre dos puntos
                     _______________________
        Distancia = V(x2-x1)**2 + (y2-y1)**2

    Vamos a requerir el modulo math.
    Tambien se agregará el control de puntaje de los enemigos destruidos

    P10 PARTE 10
    ------------
    Manejo de multiples enemigos simultaneamente, en la primer versión solo se
    manejo un solo enemigo, ahora vamos a manejar 8 enemigos simultaneamente
    mediante el uso de una lista (Esto reeemplaza P5 PARTE 5), sin embargo se 
    deja el cóidgo anterior comentado para que puedan seguir los pasos

    P11 PARTE 11
    ------------
    Dibujo de los textos en pantalla, el puntaje ahora vamos a mostrarlo en la
    pantalla del juego. Las fuentes se comportan de forma muy distinta a como 
    estamos acostumbrados, no es simplemente colocar el texto en una coordenada
    
    Los pasos a seguir son los siguientes:
        1.  Se crea un objeto donde se define el tipo de letra y tamaño
                fuente = pygame.font.Font('freesansbold.ttf', 32)

        2.  Se transforma el texto a una imagen y se le asigna un color
                texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))

        3.  La imagen anterior es ahora si mostrada en pantalla
                pantalla.blit(texto, (pos_x, pos_y))
        
    Para descargar y usar otros tipos de letras (otros fonts).
    ----------------------------------------------------------
        1.  Descargamos el font que nos guste (como recurso tienen disponible
            https://www.1001freefonts.com/) lo que se descarga es un archivo 
            comprimido (.zip)
        2.  El archivo .zip anterior lo descomprimimos dentro de la carpeta de
            nuestro proyecto por ejemplo fastest.ttf, la nueva definición del 
            tipo de letra al momento de crear el objeto para el font quedará:
                fuente = pygame.font.Font('fastest.ttf', 32)

    P12 PARTE 12
    ------------
    Agregar música y sonido a nuestro juego. Debemos descargar los archivos
    para los efectos de sonido (de preferencia .wav .ogg, los mp3 en ocasiones)
    dan problemas, estos archivos debemos ubicarlos dentro de nuestro proyecto,
    ademas es recomendable que en los audios de efectos sean de una duración 
    corta (muy corta)
    se requiere importar de la libreria pygame mixer

    Existen dos categorias para los sonidos
    ---------------------------------------
    1)  MÚSICA DE FONDO (para esta acción usamos music)
        1.1)  mixer.music.load('archivoAudio.mp3')  Carga el archivo de audio
        1.2)  mixer.music.set_volume(0.5)           Ajusta el volumen valor 
                                                    entre 0 y 1
        1.3)  mixer.music.play(-1)                  Ejecuta el archivo 
                                                    (-1) para que sea infinito
    
    2)  EFECTOS DE SONIDO (Disparos, explosiones, choques, usamos mixer).
        2.1)  sonido_colision = mixer.Sound('archivoAudio.mp3')
        2.2)  mixer.music.set_volume(1.0)
        2.3)  sonido_colision.play()

    P13 PARTE 13
    ------------
    Fin del juego, esto sucede cuando los enemigos logran llegar a impactar a 
    la nave del protagonista (colisión), para mas sencillo tomaremos en cuenta una
    distantancia alcanzada, si cumple esta condición cambiaremos la coordenada a 
    un valor fuera de la pantalla para desaparecer visualmente a todos de la pantalla
    y mostar el texto de JUEGO TERMINADO

"""


import pygame                   # P1 Para el uso de Pygame
import random                   # P5 para la creación de nuestros enemigos
import math                     # P9 Control de las colisiones
from pygame import mixer        # P12 Para el manejo del audio (sonidos)


# P1 Inicializamos PyGame
pygame.init()
pantalla = pygame.display.set_mode((800, 600))  # P1 Inicializamos la pantalla

# P2 Titulo de la pantalla
pygame.display.set_caption("Invasión espacial")

# P2 para mostrar el icono en la ventana
ruta_icono = '/home/javier/Documentos/Programas/Python/GameFede/alienicono.png'
icono = pygame.image.load(ruta_icono)
pygame.display.set_icon(icono)


# P12 Agregar la música de fondo
# -------------------------------
ruta_musica_fondo = '/home/javier/Documentos/Programas/Python/GameFede/MusicaFondo.mp3'
ruta_disparo = '/home/javier/Documentos/Programas/Python/GameFede/disparo.mp3'
ruta_colision = '/home/javier/Documentos/Programas/Python/GameFede/Golpe.mp3'

# Cargamos el archivo de música de fondo
mixer.music.load(ruta_musica_fondo)
# Definimos el volumen de reproducción
mixer.music.set_volume(0.5)
# Ejecutamos la música de fondo, el argumento -1 es para que se repita una 
# vez que termine
mixer.music.play(-1)




# P7 definicion de la imagen de fondo para nuesra ventana
ruta_fondo = '/home/javier/Documentos/Programas/Python/GameFede/Fondo.jpg'
fondo = pygame.image.load(ruta_fondo)



# P3 Dibujamos al heroe protagonista y jugador
# ---------------------------------------------
ruta_jugador = '/home/javier/Documentos/Programas/Python/GameFede/cohete.png'
img_jugador = pygame.image.load(ruta_jugador)
# Ubicación de la nave principal, recordar que mi resolución es 800x600
jugador_x = 368     # 800(largo pantalla) - 64(ancho imagen) = 736 / 2 = 368
jugador_y = 536     # 600(alto pantalla) - 64(alto imagen) = 536
jugador_x_cambio = 0    # P4 para controlar el movimiento izq. o der.


# P5 Dibujamos al enemigo (como primer version solo se maneja un enemigo)
# ---------------------------------------------
# ruta_enemigo = '/home/javier/Documentos/Programas/Python/GameFede/enemigo.png'
# img_enemigo = pygame.image.load(ruta_enemigo)
# # Ubicación de la nave principal, recordar que mi resolución es 800x600
# enemigo_x = random.randint(0, 736) 
# enemigo_y = random.randint(50, 200)
# enemigo_x_cambio = 0.3      # P5 para controlar movimiento izq. o der.
# enemigo_y_cambio = 50       # P5 PAra controlar movimiento arriba abajo




# ********************************************
# P10 CReación de multiples enemigos
# ********************************************
ruta_enemigo = '/home/javier/Documentos/Programas/Python/GameFede/enemigo.png'
                            # Creamos listas vacias para cada enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8       # <-- Define la cantidad de enemigos a mostrar

# P10 Creamos cada uno de los enemigos y los agregamos a cada lista
#     despue de está acción tendremos ya creados todos lo enemigos
for _ in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load(ruta_enemigo))
    # Ubicación de la nave principal, recordar que mi resolución es 800x600
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)




# P8 Dibujamos la bala
# ---------------------------------------------
ruta_bala = '/home/javier/Documentos/Programas/Python/GameFede/bala.png'
img_bala = pygame.image.load(ruta_bala)
# Ubicación de la bala
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False


# P9 Variable para control del puntaje (inicia con cero)
puntaje = 0

# P11 DEfinimos una variable para definir la fuente a usar
#                            font libre     tamaño
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10        # Coordenada en 'x' para ubicar el texto
texto_y = 10        # Coordenada en 'y' para ubicar el texto


# P11 Definimos una función para el dibujo de las letras
def mostrar_puntaje(pos_x, pos_y):
    """ Permite representar un texto en la pantalla
        1.  Se crea un objeto donde se define el tipo de letra y tamaño
            (se creo arriba y se llama fuente)
        2.  Se transforma el texto a una imagen y se le asigna un color
        3.  La imagen anterior es ahora si mostrada en pantalla
    """
    # Aquí cumplimos el segundo punto donde el texto lo convertimos en imagen
    # y le asignamos un color, en este caso el color blanco
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    # Como ya contamos con el texto convertido en imagen podemos mostrarlo
    # directamente en la pantalla
    pantalla.blit(texto, (pos_x, pos_y))


# P13 Funcion para mostrar el fin del juego
# definimos el tipo de letra 
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

# P13 creamos la función para mostrar el texto de juego terminal
def texto_juego_terminado():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))






# P3 funcion para dibujar al protagonista en la posición actual
def jugador(pos_x, pos_y):
    pantalla.blit(img_jugador, (pos_x, pos_y))


# P5 funcion para dibujar al enemigo (uno solo)
# def enemigo(pos_x, pos_y):
#     pantalla.blit(img_enemigo, (pos_x, pos_y))

# P10 Para dibujar a LOS enemigos, se modifa la función usada
# en el paso 5, ahora como es una lista cambia la lógica de operación
def enemigo(pos_x, pos_y, que_enemigo):
    pantalla.blit(img_enemigo[que_enemigo], (pos_x, pos_y))




# P8 funcion para dibujar la bala disparada
def disparar_bala(pos_x, pos_y):
    """ Como las coordenadas corresponden a la nave, debemos corregir
        para que el efecto de disparo sea de la punta de la nave en el
        centro """
    global bala_visible
    bala_visible = True
    # Aqui hacemos la corrección de los valores para la posición del disparo
    pantalla.blit(img_bala, (pos_x + 16, pos_y + 10))


# P9 Detectar colisión
def hay_colision(x1, y1, x2, y2):
    """ Permite calcular la distncia entre dos puntos mediante la formula
                     _______________________
        Distancia = V(x2-x1)**2 + (y2-y1)**2
    argumentos:
    x1, y1  Valores de las coordenadas del primer punto de referencia
    x2, y2  Valores de las coordenadas del segundo punto

    Retorno:
    True    Si el valor de la distancia se considera en colisión
    False   Si no cumple la condicion establecida como colisión
    """
    distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    if distancia < 27:
        return True
    else:
        return False



# P1 Loop del juego
se_ejecuta = True
while se_ejecuta:  

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

        # *****************************************
        # P4 si el evento es una tecla presionada
        # *****************************************
        if evento.type == pygame.KEYDOWN:   
            # print('Una tecla fue presionada')

            if evento.key == pygame.K_LEFT:     # P4 se oprimio la flecha izq
                # print('Flecha izquierda presionada')
                jugador_x_cambio = -0.3         # P4 se mueve a la izquierda 

            if evento.key == pygame.K_RIGHT:    # P4 se oprimio la flecha der
                # print('Flecha derecha presionada')
                jugador_x_cambio = 0.3          # P4 se mueve a la derecha

            # P8 Este es el evento que controla el disparo de la bala 
            if evento.key == pygame.K_SPACE:    # P8 Disparo con barra espaciadora

                                                # P12 Sonido del disparo
                sonido_bala = mixer.Sound(ruta_disparo)
                sonido_bala.play()

                if not bala_visible:            # P8 solo si la bala no es visible
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

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
    # enemigo_x += enemigo_x_cambio

    # P5 restringe la posición de la nave a los limites de la pantalla
    # Está es la versión para un solo enemigo
    # if enemigo_x <= 0:
    #     enemigo_x_cambio = 0.3
    #     enemigo_y += enemigo_y_cambio
    # elif enemigo_x >= 736:  # 800 (ancho pantalla) - 64 (ancho imagen) = 736
    #     enemigo_x_cambio = -0.3
    #     enemigo_y += enemigo_y_cambio


    # ************************************************************************
    # P10 Ahora como son mas enemigos reemplazamos la versión anterior P5
    #     Cambiamos tambien el manejo de las colisiones para tener control de 
    #     cada enemigo
    for ene in range(cantidad_enemigos):

        # ---------------------------------------
        # P13 Evaluación del fin del juego
        if enemigo_y[ene] > 500:                # Si llego hasta abajo termina
            for k in range(cantidad_enemigos):  # cicla con todos los enemigos
                enemigo_y[k] = 1000             # le asigna una coordenada fuera

            texto_juego_terminado()             # Muestra en pantalla GAME OVER
            break                               # rompe el ciclo
        # P13 fin de la evaluación de fin del juego
        # -----------------------------------------

        # Afectamos los valores de cada enemigo
        enemigo_x[ene] += enemigo_x_cambio[ene]

        # Control de los limites de la pantalla para el enemigo
        if enemigo_x[ene] <= 0:
            enemigo_x_cambio[ene] = 0.3
            enemigo_y[ene] += enemigo_y_cambio[ene]
        elif enemigo_x[ene] >= 736:  # 800 - 64 = 736
            enemigo_x_cambio[ene] = -0.3
            enemigo_y[ene] += enemigo_y_cambio[ene]

        # Verificamos las colisiones para cada enemigo dentro de la lista
        # En caso de haber, oculta la bala y crea una nueva coordenada para 
        # el enemigo para que aparezca de nuevo en escena
        colision = hay_colision(enemigo_x[ene], enemigo_y[ene], bala_x, bala_y)
        if colision:
            # P12 Sonido de la colisión 
            sonido_colision = mixer.Sound(ruta_colision)
            mixer.music.set_volume(1.0)
            sonido_colision.play()

            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[ene] = random.randint(0, 736) 
            enemigo_y[ene] = random.randint(50, 200)

        # dibuja al enemigo
        enemigo(enemigo_x[ene], enemigo_y[ene], ene)
    # P10 Aquí termina toda la parte 10 
    # *********************************


    # P8 Controlamos la trayectoria de la bala para que en cada ciclo se vea
    #    PRimero controlamos la visibilidad de la bala en la pantalla
    if bala_y <= -64:   # bala mide 64 bits debe salir totalmente de pantalla
        bala_y = 500    # restablecemos posición original de la bala (origen)
        bala_visible = False    # Anulamos la visibilidad


    # P8 Si la bala es visible entonces llama la función para mostrar la bala
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    # P9 Detecta colisión entre la bala y la nave evemiga y aumenta puntaje
    # colision = hay_colision(enemigo_x, enemigo_y, bala_x, bala_y)
    # if colision:
    #     bala_y = 500
    #     bala_visible = False
    #     puntaje += 1
    #     enemigo_x = random.randint(0, 736) 
    #     enemigo_y = random.randint(50, 200)


    # P3 llamamos a la función para mostrar la posición del jugador
    # jugador_x += 0.1 # como demostración
    jugador(jugador_x, jugador_y)

    # P5 Llamamos a la funcion para mostrar la posicion del enemigo
    # enemigo(enemigo_x, enemigo_y)

    # P11 Llamamos a la funcion encargada de mostrar el texto en pantalla
    mostrar_puntaje(texto_x, texto_y)

    # P2 para mostrar el color debemos actualizar la pantalla
    pygame.display.update()

