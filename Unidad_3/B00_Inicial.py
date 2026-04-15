"""  HERENCIA.

    La Herencia es el 'superpoder' de la Programación Orientada a Objetos. 
    Es fundamental entender que no se trata solo de copiar código, sino de 
    crear una jerarquía lógica.

    1. El Concepto: ¿Qué es la Herencia?
    -------------------------------------
    Es un mecanismo que permite que una clase nueva (llamada Clase Hija o 
    Subclase) adquiera las propiedades y métodos de una clase existente 
    (Clase Padre, Superclase o Clase Base).

    Relación 'Es un': La prueba de fuego para saber si la herencia es correcta 
    es preguntarse: ¿El objeto B es un objeto A?
    1)  ¿Un Jugador es un Sprite? Sí.
    2)  ¿Un Enemigo es un Sprite? Sí.

    2. Términos Clave que debes dominar
    -----------------------------------
    **) super(): Es la función que nos permite invocar métodos de la clase 
        padre. 
        Lo usamos casi siempre en el __init__ para que la clase hija 'herede' 
        la inicialización del padre.
    **) Sobrescritura (Overwriting): Es cuando la clase hija extiende la 
        funcionalidad de un método del padre para que haga algo adicional en 
        conjunto con el mismo método del padre o la super clase.
    **) Overriding(Anulación): Es cuando la clase hija redefine un método 
        del padre para que haga algo distinto.
    **) Extensibilidad: La capacidad de la clase hija de tener sus propios 
        métodos y atributos que el padre no tiene.

    3. Un punto de reflexión:
    ----------------------
    A veces solemos confundir Herencia con Composición.

    1)  Herencia: Una Nave ES UN Sprite.        (ES UN Denota herencia)
    2)  Composición: Una Nave TIENE UN Motor.   (TIENE UN Denota composición)

    Puntos clave del código:
    ------------------------
    1)  Reutilización: Nota que Heroe e Invasor no tienen la línea de 
        pygame.image.load. La heredaron de Nave. Si cambias la forma de cargar 
        imágenes en el padre, ambos se actualizan.
    2)  El uso de super(): Es como decir: 'Oye, antes de hacer mis cosas de 
        Invasor, por favor ejecuta lo que dice mi padre Nave para configurar la 
        imagen y la posición'.
    3)  Diferenciación: Aunque ambos son 'Naves', uno tiene update de teclado 
        y el otro update automático. Eso es el corazón de la POO.
"""

import pygame

class Nave(pygame.sprite.Sprite):
    """ Clase Base que define las propiedades de cualquier nave.
        1. La Clase Padre: Nave
        Todos los objetos voladores en nuestro juego tienen una imagen, una 
        posición y una salud. No queremos escribir esto tres veces.
    """
    
    def __init__(self, x, y, archivo_img):
        super().__init__()
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.salud = 100

    def recibir_daño(self, cantidad):
        """Método común para todas las naves."""
        self.salud -= cantidad
        print(f"Salud restante: {self.salud}")


class Heroe(Nave):
    """ Nave controlada por el usuario.
        2. Clase Hija 1: Heroe (Especialización por Control)
        Esta clase hereda la imagen y salud, pero extiende el comportamiento 
        añadiendo movimiento por teclado.
    """
    
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5


class Invasor(Nave):
    """ Nave enemiga con movimiento automático.
        3. Clase Hija 2: Invasor (Especialización por IA)
        Esta clase también hereda todo de Nave, pero sobrescribe el 
        comportamiento para moverse solo y quizás tenga un atributo extra como 
        'puntos al morir'."""
    
    def __init__(self, x, y, archivo_img, puntos):
        # Primero llamamos al constructor del padre
        super().__init__(x, y, archivo_img)
        # Luego añadimos lo propio de esta clase
        self.valor_puntos = puntos

    def update(self):
        # Se mueve hacia abajo automáticamente
        self.rect.y += 2

    