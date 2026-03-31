""" Reto para los alumnos (15 minutos):
    -----------------------------------
    Realizar 3 modificaciones para ver si entendieron la estructura:

    1)  Cambio de Velocidad: Añadir un parámetro extra al constructor del Jugador 
        para que unos sean más rápidos que otros.
    2)  Límites de Pantalla: En el método update, añadir un if para que el jugador
        no pueda salirse de los bordes de la ventana (800x600).
    3)  Segundo Jugador: Crear una segunda instancia llamada enemigo de color rojo 
        en una posición diferente y añadirla al mismo grupo de sprites.

    En esta versión no se desarrolla al 100% el punto 3, ya que ambos cuadros se 
    mueven con las mismas teclas, en el siguiente ejemplo los moveremos de forma
    independiente.
    Como ambos objetos son instancias de la misma clase 'Jugador' y comparten 
    el mismo método update(). Cuando presionas una tecla, ambos escuchan la misma 
    orden y se mueven al mismo tiempo.
"""
import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, color, x, y, velocidad=5):   # <-- punto 1
        super().__init__()
        # Creamos la "superficie" (el dibujo)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        
        # El "rect" es el rectángulo que envuelve a la imagen
        # Controla colisiones y posición
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = velocidad                  # <-- punto 1

    def update(self):
        # Lógica de control por teclado
        teclas = pygame.key.get_pressed()
                                                    # <-- Punto 2
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and self.rect.x>0:
            self.rect.x -= self.velocidad
                                                    # <-- Punto 2
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and self.rect.x <(800-50):
            self.rect.x += self.velocidad
                                                    # <-- Punto 2
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and self.rect.y>0:
            self.rect.y -= self.velocidad
                                                    # <-- Punto 2
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and self.rect.y<(600-50):
            self.rect.y += self.velocidad
            

class MiJuego:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((800, 600))
        self.reloj = pygame.time.Clock()

        # --- AGREGACIÓN --- (Ver explicación de porque es agregación) 
        # y aunque está dentro del constructor y parece composición, no lo es
        # Creamos la instancia del jugador
        self.protagonista = Jugador((0, 255, 0), 400, 300)
        self.enemigo = Jugador((255, 0, 0), 500, 200)
        
        # Lo metemos en un grupo para actualizarlo y dibujarlo fácilmente
        self.todos_los_sprites = pygame.sprite.Group()
        self.todos_los_sprites.add(self.protagonista)
        self.todos_los_sprites.add(self.enemigo)        # <-- Punto 3
        
        self.corriendo = True

    def ejecutar(self):
        while self.corriendo:
            # 1. Eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.corriendo = False

            # 2. Actualización (Llama al método update de cada objeto en el grupo)
            self.todos_los_sprites.update()

            # 3. Dibujo
            self.ventana.fill((64, 22, 151)) # Fondo
            self.todos_los_sprites.draw(self.ventana) # Dibuja todos los objetos
            pygame.display.flip()
            
            self.reloj.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = MiJuego()
    game.ejecutar()
