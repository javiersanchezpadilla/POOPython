""" Conceptos de POO aplicados aquí:

    1)  Herencia: Jugador hereda de Sprite, ganando métodos para ser dibujado 
        automáticamente.
    2)  Abstracción: La clase MiJuego no sabe cómo se mueve el jugador; solo 
        le dice update(). El "cómo" está oculto dentro de la clase Jugador.
    3)  Agregación: El grupo todos_los_sprites contiene objetos Jugador. Si 
        borramos el grupo, el objeto jugador podría seguir existiendo en otra 
        variable.

    Reto para los alumnos (15 minutos):
    -----------------------------------
    Realizar 3 modificaciones para ver si entendieron la estructura:

    1)  Cambio de Velocidad: Añadir un parámetro extra al constructor del Jugador 
        para que unos sean más rápidos que otros.
    2)  Límites de Pantalla: En el método update, añadir un if para que el jugador
        no pueda salirse de los bordes de la ventana (800x600).
    3)  Segundo Jugador: Crear una segunda instancia llamada enemigo de color rojo 
        en una posición diferente y añadirla al mismo grupo de sprites.

    (Resultado en la siguiente versión del código)

    =================================================================
    ==  POR QUE PARECE COMPOSICIÓN Y SE MENCIONA COMO AGREGACIÓN.  ==
    =================================================================

    Observar la siguiente linea

        class MiJuego:
            def __init__(self):
                pygame.init()
                self.ventana = pygame.display.set_mode((800, 600))
                self.reloj = pygame.time.Clock()

                self.protagonista = Jugador((0, 255, 0), 400, 300)  <<<<<<<<<*******
                
    La línea de código está dentro del constructor, lo cual suele oler a composición, 
    pero por qué en la arquitectura de videojuegos (y en este código específico) lo 
    consideramos Agregación.
    La diferencia no está solo en dónde se escribe la línea, sino en la dependencia 
    de vida y el origen de los datos.

    1. ¿Por qué parece Composición?
    Es comprensible la confusión porque estamos instanciando al Jugador dentro de 
    __init__. En una Composición pura, si la clase Juego muere, el Jugador muere con 
    ella y no tiene sentido fuera de él.

    2. Por qué lo marcamos como Agregación (El argumento técnico)
    En el desarrollo con Pygame, solemos considerar esta relación como Agregación por 
    tres razones fundamentales:

    1)  Independencia de Definición: La clase Jugador existe totalmente fuera de 
        Juego. Podrías usar esa misma clase Jugador en un 'Editor de Niveles' o en 
        un 'Menú de Selección de Personajes' sin cambiar ni una línea de su código.
    2)  Parámetros Externos: Nota que los datos (color, posición) podrían venir de 
        un archivo externo, una base de datos o un servidor. La clase Juego solo es 
        el 'lugar de reunión' temporal.
    3)  El contenedor Group: La línea self.todos_los_sprites.add(self.protagonista) 
        es la clave. El 'dueño' real del objeto durante la ejecución es el Grupo de 
        Sprites. Si borras la variable self.protagonista, el objeto sigue vivo dentro 
        del grupo. Eso rompe la regla de la composición donde el objeto padre es el 
        único dueño (Realmente esta es la clave de todo esto).

    Cómo convertirlo en 'Agregación Pura' (Para que no tengan duda alguna)
    La forma más 'limpia' de Agregación (donde el objeto se crea totalmente fuera), 
    el código se vería así:

        # 1. Creamos al jugador fuera (en el main)
        heroe = Jugador((0, 255, 0), 400, 300)

        # 2. Se lo PASAMOS al juego (Inyección de dependencias)
        class MiJuego:
            def __init__(self, objeto_jugador):
                self.protagonista = objeto_jugador      # <<<<<----- AGREGACIÓN PURA
                self.todos_los_sprites = pygame.sprite.Group()
                self.todos_los_sprites.add(self.protagonista)

        # Uso:
        game = MiJuego(heroe)

    CONCEPTOS ADICIONALES:
    ======================

        pygame.sprite.Sprite

    Esta es una de las piezas más importantes de Pygame. pygame.sprite.Sprite 
    es una Clase Base Abstracta (o una plantilla) diseñada para ser heredada.
    Por sí sola, no hace mucho, pero cuando tu clase Jugador hereda de ella, 
    'mágicamente' adquiere la capacidad de integrarse con los grupos 
    inteligentes que mencionamos antes.

    Aquí tienes las 3 funciones principales que cumple:

    1. Establece un "Contrato" de Atributos
    Para que Pygame sepa cómo dibujar un objeto automáticamente, el objeto debe 
    tener dos atributos con nombres específicos. Sprite obliga a que existan:
        *)  self.image: La apariencia visual (el 'papel').
        *)  self.rect: La ubicación y dimensiones (el 'marco').

    Si heredas de Sprite pero no defines estos dos, Pygame lanzará un error al 
    intentar dibujar. Es una excelente forma de enseñar polimorfismo a tus alumnos: 
    todos los sprites se ven distintos, pero todos se dibujan igual porque todos 
    tienen image y rect.

    2. Gestión de 'Pertenencia' (Grupos)
    Un objeto que hereda de Sprite sabe en qué grupos está metido.
        *)  Tiene métodos internos como self.kill(). Si llamas a jugador.kill(), 
            el objeto se elimina automáticamente de todos los grupos donde estaba 
            (balas, enemigos, colisiones).
        *)  Esto facilita mucho la limpieza de memoria; no tienes que buscar en 
            cada lista para borrar un objeto destruido.

    3. Comunicación con el Método update()
    Sprite reserva un nombre de método especial: update().
        *)  Cuando tú escribes def update(self): dentro de tu clase Jugador, 
            estás haciendo sobreescritura de métodos (Overriding).
        *)  Esto permite que el Group pueda llamar a todos_los_sprites.update() 
            y cada objeto ejecute su propia lógica particular.

    Resumen para la clase:
    ----------------------
    Imaginen que pygame.sprite.Sprite es un Uniforme. Al ponérselo (heredar), tus 
    objetos ya pueden entrar al cuartel (Group). Sin el uniforme, el grupo no los 
    reconoce y no les puede dar órdenes de moverse o dibujarse.

    Un detalle técnico vital:
    -------------------------
    Para que Sprite funcione, siempre debemos llamar al constructor de la clase 
    padre en el __init__ de nuestra clase:

        class Jugador(pygame.sprite.Sprite):
            def __init__(self):
                # ¡ESTA LÍNEA ES OBLIGATORIA! 
                # Activa todas las funciones internas de Sprite
                super().__init__()          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                
                self.image = pygame.Surface((50, 50))
                self.rect = self.image.get_rect()
        


    LLAMANDO A LAS FUNCIONES ESPECIALES DISPONIBLES GRACIAS A pygame.sprite.Sprite
    ==============================================================================

        self.protagonista = Jugador((0, 255, 0), 400, 300)
        self.todos_los_sprites = pygame.sprite.Group()
        self.todos_los_sprites.add(self.protagonista)
    
    Funciona como una lista porque 'guarda' objetos. Sin embargo, técnicamente 
    un pygame.sprite.Group() es más parecido a un Conjunto (Set) o una 
    Colección Inteligente.

    **) Diferencia clave: En una lista normal de Python, si agregas al 
        protagonista dos veces, tendrás dos copias en la lista. En un Group, 
        si intentas agregar al mismo objeto dos veces, Pygame se da cuenta y 
        lo mantiene solo una vez. Esto evita errores de duplicidad en el juego.

    2. ¿Por qué usamos un Group en lugar de una lista [] normal?
    Esta es la parte "mágica" de la POO en Pygame. El Group no solo guarda los 
    objetos, sino que tiene superpoderes (métodos automáticos):

    **) self.todos_los_sprites.update(): En lugar de que tú hagas un ciclo for 
        para mover a cada enemigo, bala y jugador, esta sola línea le grita a 
        todos los objetos del grupo: '¡Oigan, todos ejecuten su propio método 
        update() ahora!'.
    **) self.todos_los_sprites.draw(ventana): Esta línea le dice a cada objeto: 
        'Toma tu atributo self.image, mira tu posición en self.rect y dibújate 
        en la ventana'.

    3. La analogía para la clase
    Imaginen que self.todos_los_sprites es un Pelotón de soldados. Cuando el 
    General (la clase Juego) grita '¡Marchen!', no tiene que decírselo a cada 
    soldado uno por uno. Solo le da la orden al Pelotón (.update()), y cada 
    soldado sabe cómo mover sus propias piernas."

    Un detalle importante sobre self.todos_los_sprites.add(self.protagonista)
    Cuando usas esta línea, estás haciendo Agregación. El objeto self.protagonista 
    existe por su cuenta, y simplemente le estás diciendo al grupo: 'Ten, te 
    comparto la referencia de este jugador para que lo cuides y lo dibujes'.

    RESUMEN:
    **) Group(): Es el contenedor (el pelotón).
    **) .add(): Es la acción de reclutar un objeto al contenedor.
    **) .update(): Hace que todos los miembros del grupo ejecuten su lógica 
        interna de movimiento.
    **) .draw(): Hace que todos aparezcan en pantalla.
    
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
            

class MiJuego:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((800, 600))
        self.reloj = pygame.time.Clock()
        
        # --- AGREGACIÓN --- (Ver explicación de porque es agregación) 
        # y aunque está dentro del constructor y parece composición, no lo es
        # Creamos la instancia del jugador
        self.protagonista = Jugador((0, 255, 0), 400, 300)
        
        # Lo metemos en un grupo para actualizarlo y dibujarlo fácilmente
        self.todos_los_sprites = pygame.sprite.Group()
        self.todos_los_sprites.add(self.protagonista)
        
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
            self.ventana.fill((30, 30, 30)) # Fondo
            self.todos_los_sprites.draw(self.ventana) # Dibuja todos los objetos
            pygame.display.flip()
            
            self.reloj.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = MiJuego()
    game.ejecutar()