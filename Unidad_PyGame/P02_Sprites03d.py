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
    ** EN ESTE CÓDIGO SE USARA LA OPCIÓN 'B'    ***
    ***********************************************
   
    Opción B: Uso de Herencia (Más elegante para un juego)
    Puedes crear una clase base y luego dos clases hijas. Una para el jugador 
    humano y otra para un 'Enemigo' que se mueva solo (IA simple) o con otras 
    teclas.

            class Enemigo(Jugador): # Hereda todo de Jugador
                def update(self):
                    # Aquí el enemigo se mueve solo de izquierda a derecha 
                    # automáticamente
                    self.rect.x += self.velocidad
                    if self.rect.right > 800 or self.rect.left < 0:
                        self.velocidad *= -1 # Rebota en las paredes


    Vamos a usar la Herencia para crear un 'Enemigo' que tenga su propia 
    inteligencia artificial (IA) básica.
    Lo mejor de la POO es que no tenemos que volver a escribir el código del 
    color, la posición o el dibujo. La clase Enemigo heredará todo eso de 
    Jugador y solo sobrescribirá (reemplazará) el método update para moverse 
    por su cuenta, sin necesidad de que alguien presione una tecla.

    1. Creación de la clase Enemigo (Especialización)
    -------------------------------------------------
    Aquí aplicamos el concepto de Polimorfismo: la clase Enemigo tiene un método 
    update con el mismo nombre que el de Jugador, pero hace algo completamente 
    distinto.

    ¿Por qué este cambio es importante de entender?
    -----------------------------------------------
    1)  Reutilización de Código: No definimos self.image ni self.rect en la clase 
        Enemigo. La herencia lo hizo por nosotros.
    2)  Autonomía de Objetos: Les demuestras que un objeto no es solo un contenedor 
        de datos, sino una entidad capaz de 'tomar decisiones' (en este caso, 
        rebotar en la pared).
    3)  Simplicidad del Ciclo Principal: El método ejecutar no cambió en absoluto. 
        No le importa si hay 1 o 100 enemigos, el comando 
        self.todos_los_sprites.update() sigue siendo el mismo.
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
        self.velocidad = velocidad

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

        # Creamos la instancia del jugador y del enemigo
        self.protagonista = Jugador((0, 255, 0), 400, 300, 5)   # <-- Punto 3
        self.enemigo = Enemigo((255, 0, 0), 500, 200, 3)        # <-- Punto 3
        
        # Lo metemos en un grupo para actualizarlo y dibujarlo fácilmente
        # lo asociamos al grupo especial pygame.sprite.Group()
        # este grupo permite que deforma automatica se ejecuten los
        # métodos update() de todos las clases involucradas o socias del grupo
        self.todos_los_sprites = pygame.sprite.Group()
        # Ahora ingresamos al protagonista y al enemigo dentro del grupo
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
            # AQUÍ ESTÁ EL TRUCO:
            # El grupo llama al update() del humano (que lee teclas)
            # Y al update() del enemigo (que tiene su propia IA)
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
