""" CARGAR SONIDOS DENTRO DEL JUEGO (SOLO EFECTOS DE SONIDO RAPIDOS).

    En Pygame, el sonido y el texto se manejan como objetos, lo que encaja 
    perfectamente con el enfoque de POO que hemos estado trabajando.

    1. El Sonido (El objeto Sound)
    ------------------------------
    A)  Para efectos rápidos (disparos, explosiones, saltos), usamos 
    
            pygame.mixer.Sound. 
            
        Es muy ligero y se carga una sola vez en el __init__.

    B)  Para música de fondo larga, se usa 
    
            pygame.mixer.music.load()
        
        pero para efectos cortos de interacción, siempre usamos objetos Sound.
"""

import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, ruta_imagen, x, y, velocidad=5):
        super().__init__()

        self.image = pygame.image.load(ruta_imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        
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

        # ************************************
        # 1. Inicializamos el sistema de audio
        # *************************************
        pygame.mixer.init()
        # **********************************************
        # 2. Cargamos los efectos de sonido (Agregación)
        # **********************************************
        ruta_sonidos = '/home/javier/Documentos/Programas/Python/'\
                       'GraficPython/MIS_CLASES/Unidad_4/PNGs/Sonidos/'
        self.sonido_explosion = pygame.mixer.Sound(ruta_sonidos+'explosion.mp3')
        self.sonido_disparo = pygame.mixer.Sound(ruta_sonidos+'laser.mp3')

        # **************************************************
        # 3. Ajustamos el volumen de los efectos de sonido
        # **************************************************
        self.sonido_explosion.set_volume(0.5) # Volumen de 0 a 1
        self.sonido_disparo.set_volume(0.5)

        self.ventana = pygame.display.set_mode((800, 600))
        self.reloj = pygame.time.Clock()

        ruta_imgs = '/home/javier/Documentos/Programas/Python/POOPython/'\
                      'Unidad_PyGame/PNGs/'
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
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.corriendo = False

            self.todos_los_sprites.update()

            choques = pygame.sprite.spritecollide(self.protagonista, self.grupo_enemigos, True)
           
            if choques:
                print("¡CHOQUE! Has eliminado a un enemigo.")

                # *******************************
                # 4. Reproduce el sonido una vez
                # *******************************
                self.sonido_explosion.play()    

            # Dibujo
            self.ventana.fill((64, 22, 151)) # Fondo
            self.todos_los_sprites.draw(self.ventana) # Dibuja todos los objetos
            pygame.display.flip()
            self.reloj.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = MiJuego()
    game.ejecutar()


