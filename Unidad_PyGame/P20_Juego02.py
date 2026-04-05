""" JUEGO DE NAVE ESPACIAL

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

    def __init__(self, ruta_img, pos_x, pos_y, factor_x, factor_y):
        self.ruta_img = ruta_img
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.factor_x = factor_x
        self.factor_y = factor_y

    def muestra_img(self):
        return pygame.image.load(self.ruta_img)


  
class Heroe(ActorJuego):

    VELOCIDAD_HEROE_X = 0.3         # velocidad de desplazamiento (pixeles)
    ruta_heroe = '/home/javier/Documentos/Programas/Python/GameFede/cohete.png'

    def __init__(self, pos_x, pos_y):
        ActorJuego.__init__(self, Heroe.ruta_heroe, pos_x, pos_y, 0, 0)

    def mueve_img(self):
        self.pos_x += self.factor_x
                                # Verifica los limites horizontales de la pantalla
        if self.pos_x <= 0:     # limite izquierdo de la pantalla
            self.pos_x = 0
        elif self.pos_x >= 736:  # 800 (ancho pantalla) - 64 (ancho imagen) = 736
            self.pos_x = 736



class Enemigo(ActorJuego):

    VELOCIDAD_ENEMIGO_X = 0.5       # desplazamiento en pixeles en eje 'x'
    VELOCIDAD_ENEMIGO_Y = 50        # desplazamiento en pixeles en eje 'y'
    ruta_enemigo = '/home/javier/Documentos/Programas/Python/GameFede/enemigo.png'

    def __init__(self, pos_x, pos_y):
        ActorJuego.__init__(self, Enemigo.ruta_enemigo, pos_x, pos_y, 
                            Enemigo.VELOCIDAD_ENEMIGO_X, Enemigo.VELOCIDAD_ENEMIGO_Y)    

    def mueve_img(self):
        self.pos_x += self.factor_x
        if self.pos_x <= 0 or self.pos_x >= 736:
            self.factor_x *= (-1)       # Invierte el sentido de movimiento
            self.pos_y += self.factor_y



class Bala(ActorJuego):

    VELOCIDAD_BALA_Y = 3
    ruta_bala = '/home/javier/Documentos/Programas/Python/GameFede/bala.png'

    def __init__(self, pos_x, pos_y):
        ActorJuego.__init__(self, Bala.ruta_bala, pos_x, pos_y, 0, Bala.VELOCIDAD_BALA_Y)
        self.bala_visible = False


    def mueve_img(self):
        if self.bala_visible:
            self.pos_y -= self.factor_y
            if self.pos_y <= -64:           # la bala debe salir de la pantalla
                self.bala_visible = False   # Ya no será visible

    def hay_colision(self, enemigo_x, enemigo_y):
        """ Permite calcular la distncia entre dos puntos
                            _______________________
                Distancia = V(x2-x1)**2 + (y2-y1)**2

            argumentos de la formula:
            x1, y1  Valores de las coordenadas de la bala (self)
            x2, y2  Valores de las coordenadas del enemigo (other)

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
        self.inicia_ventana()
        self.inicia_enemigos()
        # self.inicia_balas()
        self.inicia_sonidos()
        
        self.partida()


    def inicia_graficos(self):
        pygame.init()
        return pygame.display.set_mode((800, 600))

    def inicia_ventana(self):
        pygame.display.set_caption("Invasión espacial")     # Titulo ventana
        icono = pygame.image.load(Juego.ruta_icono)         # Muestra icono
        pygame.display.set_icon(icono)

    def inicia_sonidos(self):
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
                if self.enemigo[ene].pos_y > 300:
                    self.enemigo[ene].pos_y = 1000  # lo situa fuera de la pantalla
                    self.mostrar_texto('JUEGO TERMINADO', 60, 200, 40, 'amarillo')
                    break

    def partida(self):
        fondo = pygame.image.load(Juego.ruta_fondo)

        while self.en_ejecucion:  
            self.pantalla.blit(fondo, (0, 0))
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.en_ejecucion = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.heroe.factor_x = self.heroe.VELOCIDAD_HEROE_X * (-1)
                    if evento.key == pygame.K_RIGHT:
                        self.heroe.factor_x = self.heroe.VELOCIDAD_HEROE_X
                    if evento.key == pygame.K_SPACE:
                        if not self.bala.bala_visible:
                            self.bala.bala_visible = True
                            self.bala.pos_x = self.heroe.pos_x + 16
                            self.bala.pos_y = self.heroe.pos_y + 10
                            sonido_bala = mixer.Sound(Juego.ruta_disparo)
                            sonido_bala.play()


                if evento.type == pygame.KEYUP:
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
