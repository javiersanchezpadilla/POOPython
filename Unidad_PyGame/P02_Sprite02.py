""" Uniendo ambas clases 

    La Clase Jugador (Encapsulamiento de movimiento)
    ------------------------------------------------
    En esta clase, el estado (posición y color) y el comportamiento (moverse) 
    están juntos. Fíjate cómo usamos self.rect para controlar la posición, 
    que es un objeto de Pygame muy potente.
"""

import pygame

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
            
