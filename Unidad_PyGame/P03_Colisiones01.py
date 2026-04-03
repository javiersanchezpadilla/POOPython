""" MANEJO DE COLISIONES.

    En Pygame, las colisiones no se manejan preguntando "¿toco al enemigo?" 
    en cada objeto, sino preguntando al Grupo de Sprites si hay algún choque.

    1. La lógica de colisión (La "magia" de Pygame)
    -----------------------------------------------
    Vamos a usar pygame.sprite.spritecollide. Esta función revisa automáticamente 
    si un objeto (el protagonista) ha entrado en contacto con cualquier objeto 
    de una lista o grupo (los enemigos).

    2. Organización: ¡El concepto de "Grupos" para colisiones!
    Para que esto funcione bien, es mejor tener grupos separados. Así, el jugador 
    no choca contra sí mismo, solo contra lo que tú decidas.
    Esto quiere decir que debemos agregar un grupo solo para los enemigos

    Por qué esta es la mejor forma de aprender POO:
    -----------------------------------------------
    1)  Manejo de estados: Al pasar True en spritecollide, Pygame invoca 
        internamente el método kill() del sprite. ¡Es la misma gestión 
        automática de memoria que vimos hace un momento!
    2)  Escalabilidad: Si mañana quieres 50 enemigos, solo los agregas al 
        grupo_enemigos y la misma línea de código de colisión seguirá 
        funcionando sin que tengas que cambiar nada. Eso es código profesional.
    3)  Encapsulamiento: No escribimos coordenadas ni medimos distancias; le 
        delegamos esa tarea 'laboriosa' a Pygame.

"""
import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, color, x, y, velocidad=5): 
        super().__init__()
        # Creamos la "superficie" (el dibujo)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
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

        # Creamos la instancia del jugador y del enemigo
        self.protagonista = Jugador((0, 255, 0), 400, 300, 5)
        self.enemigo = Enemigo((255, 0, 0), 500, 200, 3)
        
        # Lo metemos en un grupo para actualizarlo y dibujarlo fácilmente
        # lo asociamos al grupo especial pygame.sprite.Group()
        # este grupo permite que deforma automatica se ejecuten los
        # métodos update() de todos las clases involucradas o socias del grupo
        # GRUPO PARA TODOS (GRUPO PARA DIBUJAR) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.todos_los_sprites = pygame.sprite.Group()

        # GRUPO SOLO PARA ENEMIGOS (PARA DETECTAR COLSICIONES)<<<<<<<<<<<<<<<<<<<
        # pygame.Sprite.Gruoup permite crear grupos que son tuplas para control
        #                     ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
        self.grupo_enemigos = pygame.sprite.Group()

        # Ahora ingresamos al protagonista y al enemigo dentro del grupo
        self.todos_los_sprites.add(self.protagonista)
        self.todos_los_sprites.add(self.enemigo)   
        
        # AGREGAMOS AL ENEMIGO AL GRUPO DE LOS ENEMIGOS. 
        self.grupo_enemigos.add(self.enemigo)

        self.corriendo = True

    def ejecutar(self):
        while self.corriendo:
            # 1. Eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.corriendo = False

            # 2. Actualización (Llama al método update de cada objeto en el grupo)
            self.todos_los_sprites.update()

            # NUEVA LÓGICA DE COLISIÓN
            # ¿El protagonista chocó con alguien del grupo de enemigos?
            # True significa: "Si hay choque, elimina al enemigo"
            # cuando detecta colisión entre el protagonista contra los elementos del 
            # grupo de enemigos, automaticamente destruye ese elemento de la lista y 
            # a partir de ese momento ya no lo muestra
            #                       sprotecollida      ⬇️⬇️⬇️⬇️⬇️⬇️       ⬇️⬇️⬇️⬇️⬇️⬇️  ⬇️⬇️ 
            choques = pygame.sprite.spritecollide(self.protagonista, self.grupo_enemigos, True)
           
            if choques:
                print("¡CHOQUE! Has eliminado a un enemigo.")

            # 3. Dibujo
            self.ventana.fill((64, 22, 151)) # Fondo
            self.todos_los_sprites.draw(self.ventana) # Dibuja todos los objetos
            pygame.display.flip()
            
            self.reloj.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = MiJuego()
    game.ejecutar()
