""" 
    Nombre del Módulo: Juego nave espacial
    Autor: Javier Sánchez Padilla
    Fecha: 08/04/2026
    Descripción: Este módulo contiene toda lógica integrada de la versión
    funcional, pero ahora orientada a objetos.

    REQUERIMIENTOS:
    ===============
    pip install pygame                  Desde la consola ejecutar el comando
                                        para la instalación de la libreria 
                                            
    RECURSOS:
    =========
    https://www.1001freefonts.com/      Fuentes de texto
    https://www.flaticon.es/            Iconos e imagenes libres
"""

import pygame                       
import random
import math
from pygame import mixer


class ActorJuego:
    """
    Representa una entidad dentro del juego.
    La entidad puede ser el protagonista, el enemigo, la bala podemos 
    observar que comparten los mismos atributos

    Atributos:
        ruta_imga:  Ruta donde se encuentra el archivo a cargar
        pos_x       Posición en el eje 'x' de la entidad
        pos_y       Posición en el eje 'y'
        factor_X    Desplazamiento en el eje 'x' para el personaje (velocidad)
        factor_Y    Desplazamiento en el eje 'y' para el personaje (velocidad)
    """

    def __init__(self, ruta_img, pos_x, pos_y, factor_x, factor_y):
        """Inicializa la entidad con sus parámetros básicos."""
        self.ruta_img = ruta_img
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.factor_x = factor_x
        self.factor_y = factor_y

    def muestra_img(self):
        """ Carga la imagen correspondiente al atributo """
        return pygame.image.load(self.ruta_img)


  
class Heroe(ActorJuego):
    """
    Representa al heroe del juego.

    Atributos de clase:
    VELOCIDAD_HEROE Es el desplazamiento (velocidad)
    ruta_heroe      Ruta donde se encuentra el archivo de la imagen
    """

    VELOCIDAD_HEROE_X = 0.3         # velocidad de desplazamiento (pixeles)
    ruta_heroe = '/home/javier/Documentos/Programas/Python/GameFede/cohete.png'

    def __init__(self, pos_x, pos_y):
        ActorJuego.__init__(self, Heroe.ruta_heroe, pos_x, pos_y, 0, 0)

    def mueve_img(self):
        """ Afecta el movimiento y deliminta los limites de la pantalla (0 a 800)
            el heroe solo puede moverse de forma horizontal"""
        self.pos_x += self.factor_x
                                # Verifica los limites horizontales de la pantalla
        if self.pos_x <= 0:     # limite izquierdo de la pantalla
            self.pos_x = 0
        elif self.pos_x >= 736:  # 800 (ancho pantalla) - 64 (ancho imagen) = 736
            self.pos_x = 736



class Enemigo(ActorJuego):
    """
    Representa al enemigo del juego.

    Atributos de clase:

    VELOCIDAD_ENEMIGO_X Es el desplazamiento (velocidad) en eje 'x'
    VELOCIDAD_ENEMIGO_Y Es el desplazamiento (velocidad) en eje 'y'
    ruta_enemigo        Ruta donde se encuentra el archivo de la imagen
    """

    VELOCIDAD_ENEMIGO_X = 0.5       # desplazamiento en pixeles en eje 'x'
    VELOCIDAD_ENEMIGO_Y = 50        # desplazamiento en pixeles en eje 'y'
    ruta_enemigo = '/home/javier/Documentos/Programas/Python/GameFede/enemigo.png'

    def __init__(self, pos_x, pos_y):
        ActorJuego.__init__(self, Enemigo.ruta_enemigo, pos_x, pos_y, 
                            Enemigo.VELOCIDAD_ENEMIGO_X, Enemigo.VELOCIDAD_ENEMIGO_Y)    

    def mueve_img(self):
        """ Afecta el movimiento y deliminta los limites de la pantalla (0 a 800)
            el enemigo puede moverse de forma horizontal y vertical, cada vez que
            llega a uno de los límites (bordes de la pantalla), baja un determinado
            valor en pixeles (VELOCIDAD_ENEMIGO_Y)"""
        self.pos_x += self.factor_x
        if self.pos_x <= 0 or self.pos_x >= 736:
            self.factor_x *= (-1)       # Invierte el sentido de movimiento
            self.pos_y += self.factor_y



class Bala(ActorJuego):
    """
    Representa el disparo (bala) en el juego.

    Atributos de clase:
    VELOCIDAD_BALA_Y    Desplazamiento (velocidad) de la bala
    ruta_bala           Ruta donde se encuentra el archivo de la imagen
    """

    VELOCIDAD_BALA_Y = 3
    ruta_bala = '/home/javier/Documentos/Programas/Python/GameFede/bala.png'

    def __init__(self, pos_x, pos_y):
        ActorJuego.__init__(self, Bala.ruta_bala, pos_x, pos_y, 0, Bala.VELOCIDAD_BALA_Y)
        self.bala_visible = False


    def mueve_img(self):
        """ Afecta el movimiento y deliminta los limites de la pantalla (0 a 600)
            la bala se debe mover desde donde es creada (disparada desde la 
            posición de la nave) y seguir una trayectoria vertical hasta salir
            totalmente de la pantalla.
        """
        if self.bala_visible:
            self.pos_y -= self.factor_y
            if self.pos_y <= -64:           # la bala debe salir de la pantalla
                self.bala_visible = False   # Ya no será visible

    def hay_colision(self, enemigo_x, enemigo_y):
        """ Permite calcular la distancia entre dos puntos
                         _______________________
            Distancia = V(x2-x1)**2 + (y2-y1)**2
                    x1, y1  Valores de las coordenadas de la bala (self)
                    x2, y2  Valores de las coordenadas del enemigo (other)

            Args:
            enemigo_x   Coordenada en 'x' del enemigo
            enemigo_y   Coordenada en 'y' del enemigo

            Retorno:
            True    Si el valor de la distancia se considera en colisión
            False   Si no cumple la condicion establecida como colisión
        """
        distancia = math.sqrt(math.pow((self.pos_x - enemigo_x), 2) +\
                              math.pow((self.pos_y - enemigo_y), 2))
        if distancia < 27:
            return True
        else:
            return False       



class Juego:
    """
    Representa el juego controlando totalmente la operación del mismo.

    Atributos:
        en_ejecucion    True mientras este activo el juego
        heroe           Instancia del heroe (composición)
        enemigo         Instancias de los enemigos del juego (composición)
        bala            Instancia del disparo
        puntaje         Marcador de enemigos eliminados
        pantalla        Instancia de la ventana creada para el juego
    """

    TOTAL_ENEMIGOS = 8              # Numero máximo de enemigos en pantalla
    ruta_fondo = '/home/javier/Documentos/Programas/Python/GameFede/Fondo.jpg'
    ruta_icono = '/home/javier/Documentos/Programas/Python/GameFede/alienicono.png'
    ruta_musica_fondo = '/home/javier/Documentos/Programas/Python/GameFede/MusicaFondo.mp3'
    ruta_disparo = '/home/javier/Documentos/Programas/Python/GameFede/disparo.mp3'
    ruta_colision = '/home/javier/Documentos/Programas/Python/GameFede/Golpe.mp3'

    def __init__(self):
        self.en_ejecucion = True
        self.heroe = Heroe(400, 536)
        self.enemigo = []
        self.bala = Bala(0,0)
        self.puntaje = 0
        self.pantalla = self.inicia_graficos()

        self.inicia_ventana()       # crea la instancia de la ventana gráfica
        self.inicia_enemigos()      # Crear los enemigos
        self.inicia_sonidos()       # carga todos los sonidos
        self.partida()              # controla la partida


    def inicia_graficos(self):
        """ Inicializa PyGame y retorna una instancia que representa la 
            pantalla"""
        pygame.init()
        return pygame.display.set_mode((800, 600))

    def inicia_ventana(self):
        """ Asigna las propiedades de la pantalla, como el título de la
            pantalla y asigna y muestra el icono """
        pygame.display.set_caption("Invasión espacial")     # Titulo ventana
        icono = pygame.image.load(Juego.ruta_icono)         # Muestra icono
        pygame.display.set_icon(icono)

    def inicia_sonidos(self):
        """ Carga la música de fondo del juego y a ejecuta """
        mixer.music.load(Juego.ruta_musica_fondo)       # Cargamos musica fondo
        mixer.music.set_volume(0.5)                     # volumen de reproducc
        mixer.music.play(-1)                            # Ejecuta infitamente (-1)


    def inicia_enemigos(self):                              # crea a los enemigos
        for _ in range(Juego.TOTAL_ENEMIGOS):
            self.enemigo.append(Enemigo(random.randint(0, 736), random.randint(50, 200)))

    def mueve_enemigos(self):
        for ene in range(Juego.TOTAL_ENEMIGOS):
            self.enemigo[ene].mueve_img()

    def muestra_enemigos(self):
        for ene in range(Juego.TOTAL_ENEMIGOS):
            self.pantalla.blit(self.enemigo[ene].muestra_img(), (self.enemigo[ene].pos_x, self.enemigo[ene].pos_y))

    def determina_colisiones(self):
        for ene in range(Juego.TOTAL_ENEMIGOS):
            enemigo_destriudo = self.bala.hay_colision(self.enemigo[ene].pos_x, self.enemigo[ene].pos_y)
            if enemigo_destriudo:
                self.bala.bala_visible = False
                self.enemigo[ene].pos_x = random.randint(0, 736) 
                self.enemigo[ene].pos_y = random.randint(50, 200)
                self.puntaje += 1
                sonido_colision = mixer.Sound(Juego.ruta_colision)
                mixer.music.set_volume(1.0)
                sonido_colision.play()

    def mostrar_texto(self, f_string_texto, pos_x, pos_y, tamanio, color_texto):
        """ Permite representar un texto en la pantalla
            1.  Se crea un objeto donde se define el tipo de letra y tamaño
                (se creo arriba y se llama fuente)
            2.  Se transforma el texto a una imagen y se le asigna un color
            3.  La imagen anterior es ahora si mostrada en pantalla
        """
        color = {'azul':(0, 0, 255), 'blanco':(255, 255, 255), 'amarillo':(255, 255, 0),
                 'verde':(0, 255, 0), 'rojo':(255, 0, 0)}
        fuente = pygame.font.Font('freesansbold.ttf', tamanio)
        texto_cadena = fuente.render(f_string_texto, True, color[color_texto])
        self.pantalla.blit(texto_cadena, (pos_x, pos_y))

    def determina_fin_juego(self):
            for ene in range(Juego.TOTAL_ENEMIGOS):
                if self.enemigo[ene].pos_y > 500:
                    self.enemigo[ene].pos_y = 1000  # lo situa fuera de la pantalla
                    self.mostrar_texto('JUEGO TERMINADO', 60, 200, 40, 'amarillo')
                    break

    def partida(self):
        fondo = pygame.image.load(Juego.ruta_fondo)

        while self.en_ejecucion:  
            self.pantalla.blit(fondo, (0, 0))           # carga en imagen de fondo
            for evento in pygame.event.get():           # captura los eventos
                if evento.type == pygame.QUIT:          # evento cerrar
                    self.en_ejecucion = False
                if evento.type == pygame.KEYDOWN:       # evento TECLA PRESIONADA
                    if evento.key == pygame.K_LEFT:     # tecla flecha izquierda
                        self.heroe.factor_x = self.heroe.VELOCIDAD_HEROE_X * (-1)
                    if evento.key == pygame.K_RIGHT:    # tecla flecha derecha
                        self.heroe.factor_x = self.heroe.VELOCIDAD_HEROE_X
                    if evento.key == pygame.K_SPACE:    # tecla barra espaciadora
                        if not self.bala.bala_visible:
                            self.bala.bala_visible = True
                            self.bala.pos_x = self.heroe.pos_x + 16
                            self.bala.pos_y = self.heroe.pos_y + 10
                            sonido_bala = mixer.Sound(Juego.ruta_disparo)
                            sonido_bala.play()


                if evento.type == pygame.KEYUP:     # evento tecla LIBERADA
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        self.heroe.factor_x = 0
            

            # Mueve las coordenadas de la imagen del heroe
            self.heroe.mueve_img()
            # Muestra la imagen del heroe
            self.pantalla.blit(self.heroe.muestra_img(), (self.heroe.pos_x, self.heroe.pos_y))

            self.mueve_enemigos()
            self.muestra_enemigos()

            self.bala.mueve_img()
            if self.bala.bala_visible:
                self.pantalla.blit(self.bala.muestra_img(), (self.bala.pos_x, self.bala.pos_y))

            self.determina_colisiones()
            self.mostrar_texto(f'Puntaje {self.puntaje}', 1, 1, 32, 'amarillo')
            self.determina_fin_juego()
            pygame.display.update()



aa = Juego()
