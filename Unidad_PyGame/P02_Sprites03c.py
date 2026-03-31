""" Reto para los alumnos (15 minutos):
    -----------------------------------

    3)  Segundo Jugador: Crear una segunda instancia llamada enemigo de color 
        rojo en una posición diferente y añadirla al mismo grupo de sprites.

    El problema actual es que ambos objetos son instancias de la misma clase 
    Jugador y comparten el mismo método update(). Cuando presionas una tecla, 
    ambos escuchan la misma orden y se mueven al mismo tiempo.

    Para controlarlos de forma independiente, podemos haerlo de dos formas 
    distintas:

    ***********************************************
    ** EN ESTE CÓDIGO SE USARA LA OPCIÓN 'A'    ***
    ** (y en el siguiente programa la opción B)  **
    ***********************************************
    
    Opción A: Pasar los controles por el constructor (Inyección de Dependencias)
    Esta es la más sencilla si quieres seguir usando una sola clase. Le dices 
    a cada instancia qué teclas debe obedecer.

    Modifica el __init__: Recibe un diccionario o una lista con las teclas.
    Modifica el update: Usa esas variables en lugar de pygame.K_LEFT, etc.

    Ejemplo de cómo quedaría el cambio:

        class Jugador(pygame.sprite.Sprite):
                                            vvvvvvvvv
            def __init__(self, color, x, y, controles, velocidad=5):
                super().__init__()
                # ... (resto del código igual) ...
                self.controles = controles # Guardamos el diccionario de teclas

            def update(self):
                teclas = pygame.key.get_pressed()
                
                # Ahora usamos self.controles['izquierda'], etc.
                if teclas[self.controles['izq']] and self.rect.x > 0:
                    self.rect.x -= self.velocidad
                if teclas[self.controles['der']] and self.rect.x < (800-50):
                    self.rect.x += self.velocidad
                # ... repetir para arriba y abajo ...

    Opción B: Uso de Herencia (Más elegante para un juego)
    Puedes crear una clase base y luego dos clases hijas. Una para el jugador 
    humano y otra para un 'Enemigo' que se mueva solo (IA simple) o con otras 
    teclas.

            class Enemigo(Jugador): # Hereda todo de Jugador
                def update(self):
                    # Aquí el enemigo se mueve solo de izquierda a derecha automáticamente
                    self.rect.x += self.velocidad
                    if self.rect.right > 800 or self.rect.left < 0:
                        self.velocidad *= -1 # Rebota en las paredes
    
    VAMOS A UTILIZAR LA PRIMER OPCION 'A': En este código se desarrollará la opción A
                
"""
import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, color, x, y, controles, velocidad=5):   # <-- punto 1
        super().__init__()
        # Creamos la "superficie" (el dibujo)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        
        # El "rect" es el rectángulo que envuelve a la imagen
        # Controla colisiones y posición
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = velocidad
        self.controles = controles                  # <-- punto 3

    def update(self):
        # Lógica de control por teclado
        teclas = pygame.key.get_pressed()
                                                    # <-- Punto 2
        if teclas[self.controles['izq']] and self.rect.x>0:
            self.rect.x -= self.velocidad
                                                    # <-- Punto 2
        if teclas[self.controles['der']] and self.rect.x <(800-50):
            self.rect.x += self.velocidad
                                                    # <-- Punto 2
        if teclas[self.controles['arr']] and self.rect.y>0:
            self.rect.y -= self.velocidad
                                                    # <-- Punto 2
        if teclas[self.controles['aba']] and self.rect.y<(600-50):
            self.rect.y += self.velocidad
            

class MiJuego:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((800, 600))
        self.reloj = pygame.time.Clock()

        # DEFINICION DE LOS CONTROLES PARA CADA JUGADOR
        # Definimos las teclas para el protagonista (Flechas)
        controles_p1 = { 'izq': pygame.K_LEFT, 'der': pygame.K_RIGHT, 
                         'arr': pygame.K_UP, 'aba': pygame.K_DOWN }
        
        # Definimos las teclas para el enemigo (WASD)
        controles_p2 = { 'izq': pygame.K_a, 'der': pygame.K_d, 
                         'arr': pygame.K_w, 'aba': pygame.K_s }
        
        # Creamos la instancia del jugador y del enemigo
        self.protagonista = Jugador((0, 255, 0), 400, 300, controles_p1, 5)
        self.enemigo = Jugador((255, 0, 0), 500, 200, controles_p2, 7)   # <-- Punto 3
        
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
