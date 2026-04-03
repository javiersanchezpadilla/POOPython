""" CARGAR IMAGENES DENTRO DE LOS RECTANGULOS.

    Cambiar los cuadros de colores por imágenes reales (sprites) es el 
    momento en el que el proyecto deja de parecer un 'ejercicio de clase' 
    y empieza a verse como un videojuego de verdad.

    En la Programación Orientada a Objetos, esto es muy sencillo porque 
    solo tenemos que modificar el atributo self.image de nuestra clase.

    1. Preparación: Cargar la imagen
    --------------------------------
    Para que el juego no se vuelva lento, Pygame recomienda cargar la imagen 
    una sola vez y convertirla al formato interno de la tarjeta de vídeo usando 
    .convert_alpha().

    Instrucción clave:
    ------------------

                self.image = pygame.image.load("nave.png").convert_alpha()

    2. Modificando la clase Jugador
    -------------------------------
    Vamos a actualizar el constructor para que, en lugar de crear un Surface 
    vacío de color, cargue un archivo.

    3. El "Secreto" del Rect con imágenes reales
    --------------------------------------------
    Aquí es donde se vr el poder de la POO. Al usar self.image.get_rect(), 
    Pygame mide los píxeles de la imagen (por ejemplo, una nave de 60x60) y 
    crea el "marco" exacto.

    ¿Qué pasa con la colisión?
    --------------------------
    Lo mejor es que la línea de colisión (spritecollide) sigue funcionando 
    exactamente igual. No importa si el objeto es un cuadro verde o un 
    dragón hiperrealista; Pygame seguirá usando el rect para detectar el 
    choque.
"""

import pygame

class Jugador(pygame.sprite.Sprite):
    # 1. ya no vamos a usar el color, ahora carharmos la imagen
    #                  vvvvvvvvvvv
    def __init__(self, ruta_imagen, x, y, velocidad=5):
        super().__init__()

        # 2. Cargamos la imagen real
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(color)
        self.image = pygame.image.load(ruta_imagen).convert_alpha()
        
        # 3. Opcional: Escalar la imagen si es muy grande
        self.image = pygame.transform.scale(self.image, (40, 60))
        
        # 4. El rect se ajusta automáticamente al tamaño de la imagen cargada
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = velocidad

    def update(self):
        # Lógica de control por teclado
        teclas = pygame.key.get_pressed()
                                        
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and self.rect.x>0:
            self.rect.x -= self.velocidad
                                              
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and self.rect.x <(800-50):
            self.rect.x += self.velocidad
                                             
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and self.rect.y>0:
            self.rect.y -= self.velocidad
               
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and self.rect.y<(600-50):
            self.rect.y += self.velocidad
            
            
class Enemigo(Jugador):
    
    def __init__(self, color, x, y, velocidad=3):
        # Llamamos al constructor de Jugador para que configure el color 
        # y posición
        super().__init__(color, x, y, velocidad)
        self.direccion = 1 # 1 para derecha, -1 para izquierda

    def update(self):
        # IA Básica: Se mueve de lado a lado y rebota en las paredes
        self.rect.x += self.velocidad * self.direccion

        # Si toca el borde derecho (800) o el izquierdo (0)
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.direccion *= -1 # Cambia el sentido del movimiento


class MiJuego:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((800, 600))
        self.reloj = pygame.time.Clock()

        # 5. Creamos la instancia del jugador y del enemigo
        ruta_imgs = '/home/javier/Documentos/Programas/Python/POOPython/'\
                      'Unidad_PyGame/PNGs/'
        # ya no vamos a usar el color  xxxxxxxxx
        # 6. self.protagonista = Jugador((0, 255, 0), 400, 300, 5) 
        self.protagonista = Jugador(ruta_imgs+'Nave01.png', 400, 300, 5)
        self.enemigo = Enemigo(ruta_imgs+'Alien01.png', 500, 200, 3) 
        
        self.todos_los_sprites = pygame.sprite.Group()
        self.grupo_enemigos = pygame.sprite.Group()

        # Ahora ingresamos al protagonista y al enemigo dentro del grupo
        self.todos_los_sprites.add(self.protagonista)
        self.todos_los_sprites.add(self.enemigo) 
        
        # Agregamos al enemigo al grupo de los enemigos. 
        self.grupo_enemigos.add(self.enemigo)
        self.corriendo = True

    def ejecutar(self):
        while self.corriendo:
            # 1. Eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.corriendo = False

            self.todos_los_sprites.update()

            choques = pygame.sprite.spritecollide(self.protagonista, self.grupo_enemigos, True)
           
            if choques:
                print("¡CHOQUE! Has eliminado a un enemigo.")

            # Dibujo
            self.ventana.fill((64, 22, 151)) # Fondo
            self.todos_los_sprites.draw(self.ventana) # Dibuja todos los objetos
            pygame.display.flip()
            self.reloj.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = MiJuego()
    game.ejecutar()


