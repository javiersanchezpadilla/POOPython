""" Agregación de Sprites

    Aquí es donde entra el concepto de Agregación que vimos antes. 
    No queremos que la clase Juego sepa cómo moverse; queremos una 
    clase Jugador independiente.

    Pygame tiene una clase especial para esto llamada pygame.sprite.Sprite.

    Por qué este enfoque es mejor para tus clases:
    ----------------------------------------------

    1)  Encapsulamiento: Cada objeto (Jugador, Enemigo) sabe cómo dibujarse 
        y moverse solo. Si algo falla en el movimiento, solo revisas la clase 
        Jugador.
    2)  Escalabilidad: Si quieres 100 enemigos, solo creas 100 instancias de 
        la clase Enemigo. No necesitas 100 variables diferentes.
    3)  Herencia: Más adelante, puedes crear una clase base Entidad y que 
        Jugador y Enemigo hereden de ella (compartiendo salud, posición, etc.).

    Tarea para la clase:
    --------------------
    
    1)  Copien el esqueleto básico.
    2)  Creen una clase Cuadrado que herede de pygame.sprite.Sprite.
    3)  Usen Agregación para añadir una instancia de Cuadrado a la clase Juego.
"""

import pygame


# class Jugador(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((50, 50))
#         self.image.fill((0, 255, 0)) # Un cuadrado verde
#         self.rect = self.image.get_rect()
#         self.rect.center = (400, 300)

#     def update(self):
#         # Lógica de movimiento con flechas
#         teclas = pygame.key.get_pressed()
#         if teclas[pygame.K_LEFT]:
#             self.rect.x -= 5
#         if teclas[pygame.K_RIGHT]:
#             self.rect.x += 5

class Jugador(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        # Creamos la "superficie" (el dibujo)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        
        # El "rect" es el rectángulo que envuelve a la imagen
        # Controla colisiones y posición
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = 5

    def update(self):
        # Lógica de control por teclado
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.rect.y += self.velocidad
            
