""" CREACIÓN DEL ENTORNO DE TRABAJO

    Requerimientos:
    ---------------
    Desde la consola debemos instlar:

        pip install pygame  <-- Instalar la libreria PyGame

    vamos a estructurar el juego no como un montón de funciones sueltas, 
    sino como una Clase Maestra que controle todo.

    El Concepto: La Clase Juego
    --------------------------
    En lugar de tener un ciclo while infinito en medio de nuestro script, 
    crearemos una clase llamada Game. Esta clase será el "cerebro" que contiene:
        1)  Atributos: La ventana, el reloj (FPS), y el estado del juego.
        2)  Métodos: Inicializar, manejar eventos, actualizar lógica y dibujar.

    MANEJO DE LOS COLORES:
    ---------------------
    Para obtener los valores para los colores Rojo, Verde y Azul (RGB), podemos
    acceder a la página: 

        https://htmlcolorcodes.com/es/

    Los colores son RGB con una escala de 0 a 255
    Rojo  Verde    Azul
     0        0       0     Negro (Ausencia de color)
    255     255     255     Blanco (Adición de todos los colores)
    255       0       0     Rojo
      0     255       0     Verde
      0       0     255     Azul
    255     255       0     Amarillo
     64      22     151     Morado
     64     103     221     Tono de azul

    4 instrucciones "misteriosas" que siempre causan confusión al principio.
    -------------------------------------------------------------------------

    1. El Rect (El objeto más importante)
    En Pygame, no movemos "imágenes", movemos rectángulos.
        *)  Instrucción: self.rect = self.image.get_rect()
        *)  Explicación sencilla: Imagina que cada dibujo es una estampa. El rect 
            es el borde invisible de plástico que la rodea.
        *)  Para qué sirve: Si quieres saber si dos objetos chocaron, Pygame no 
            mira los píxeles, solo mira si sus "rectángulos" se enciman. Además, 
            nos permite usar propiedades mágicas como self.rect.center, 
            self.rect.top o self.rect.bottom.

    2. El Surface (El lienzo)
        *)  Instrucción: self.image = pygame.Surface((50, 50))
        *)  Explicación sencilla: Un Surface es simplemente un trozo de papel en 
            blanco donde puedes dibujar.
        *)  Dato clave: La ventana principal del juego también es un Surface. 
            Cuando 'dibujamos' al jugador, lo que hacemos en realidad es copiar 
            el papel pequeño (el jugador) sobre el papel grande (la ventana).

    3. El "Flip" o "Update" de pantalla
        *)  Instrucción: pygame.display.flip()
        *)  Explicación sencilla: Imagina un pizarrón con dos caras. Pygame 
            dibuja todo en la cara que no ves (atrás), para que no se vea el 
            proceso de dibujo parpadeando.
        *)  El truco: flip() le da la vuelta al pizarrón para mostrar el dibujo 
            terminado al jugador. Esto ocurre 60 veces por segundo. (es un buffer
            el cual cambia swapbuffer).

    4. El "Tick" del Reloj
        *)  Instrucción: self.reloj.tick(60)
        *)  Explicación sencilla: Sin esto, el juego correría a la velocidad 
            máxima de tu procesador. En una computadora potente el cuadro se 
            movería a la velocidad de la luz y en una vieja muy lento.
        *)  Función: Esta instrucción le dice a Python: "Espera lo necesario 
            para que este ciclo dure exactamente 1/60 de segundo". Así, el 
            juego corre igual en todas las máquinas.

    RECOMENDACIÓN:
    --------------
    Entender el sistema de coordenadas. En Pygame (y casi todos los motores de 
    juegos):
        *)  El punto (0,0) es la esquina superior izquierda.
        *)  Si sumas a la Y, el objeto baja.
        *)  Si restas a la Y, el objeto sube.
"""

import pygame
import sys

class Juego:
    def __init__(self):
        pygame.init()                           # 1. Inicialización de Pygame
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mi Primer Juego POO")
        self.reloj = pygame.time.Clock()
        self.ejecutando = True

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False

    def actualizar(self):
        # Aquí colocaremos la lógica del juego (movimientos, colisiones)
        pass

    def dibujar(self):
        self.pantalla.fill((64, 22, 151)) # RGB de 0 a 255 por color

        # Aquí se dibujarán los objetos

        pygame.display.flip()

    def ejecutar(self):
        while self.ejecutando:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(60) # Limitamos a 60 FPS
        
        pygame.quit()
        sys.exit()


# Punto de entrada
if __name__ == "__main__":  # Para poder hacer pruebas locales
    mi_juego = Juego()
    mi_juego.ejecutar()

