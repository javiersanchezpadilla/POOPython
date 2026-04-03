""" ACTIVOS PARA DESCARGAR IMAGENES.

     Para no perder tiempo buscando imágenes que luego resultan ser demasiado 
     grandes, o tengan fondo negro que no queremos, o tienen formatos extraños.

     Guía de Activos:
     ---------------- 
    Preparando tus imágenes para Pygame, Para que los juegos pasen de 
    'cuadritos' a 'imágenes reales'.
     
    ¿Dónde conseguir imágenes gratis y seguras?
    -------------------------------------------
    Usa estos sitios que tienen recursos específicos para juegos:
    A)  itch.io: La mejor fuente. Busca 'Free 2D Assets'. Son archivos 
        diseñados para videojuegos (https://itch.io/game-assets/free).
    B)  Kenney.nl: Es el estándar de oro en la industria educativa. Todo es 
        gratuito y de muy alta calidad (https://kenney.nl/assets).
    C)  OpenGameArt.org: Imágenes de código abierto.2 
        (https://opengameart.org/). 
    
    Formatos recomendados 
    ---------------------
    1)  Formato: Siempre busca PNG.
    2)  Por qué: El PNG soporta transparencia. Esto significa que si tu nave 
        tiene forma de 'cruz', el espacio que sobra alrededor de la cruz será 
        invisible, en lugar de ser un cuadro blanco o negro molesto.
        
    Tamaño 
    ------
    1)  No descargues imágenes de 2000x2000 píxeles. Para un juego de 800x600,
        busca imágenes de entre 32x32 y 64x64 píxeles.Si la imagen es muy 
        grande: Recuerda que puedes usar 

            pygame.transform.scale(imagen, (ancho, alto)) 

        dentro de tu constructor para ajustarla al tamaño que necesites.
        
    Ubicación de la imagenes en el proyecto.
    ----------------------------------------
    1) Pon todas las imágenes en una carpeta llamada assets dentro del proyecto.
    2)  Tu código debe verse así para cargar el archivo:
    
            self.image = pygame.image.load("assets/nave.png").convert_alpha()
            
    ¿Cómo evaluar esto en clase? 
    (Rúbrica rápida)Si quieres evaluar que realmente entendieron cómo cargar imágenes:CriterioLogrado (3 pts)A mejorar (1 pt)TransparenciaEl personaje se ve limpio, sin cuadros blancos alrededor.El personaje tiene un fondo cuadrado que tapa el escenario.Gestión de memoriaUsó .convert_alpha() al cargar la imagen.Carga la imagen directamente en el draw (lento y causa lag).OrganizaciónLas imágenes están en una carpeta assets.Imágenes desperdigadas en cualquier carpeta o en la raíz.🚀 El "Reto Final" de integraciónComo ya saben hacer:Clases con POO.Herencia (Jugador y Enemigo).Colisiones.Cargar imágenes.El examen final de esta unidad podría ser: "Crea un juego donde el jugador (con imagen) deba esquivar 3 enemigos (con otra imagen) que se mueven a velocidades aleatorias. Si el jugador choca, debe aparecer un mensaje de 'Game Over' en consola y eliminar al enemigo."¿Te gustaría que te ayude a redactar este "Examen Final" completo incluyendo una sección de "Puntos Extra" para los alumnos que logren poner música o sonidos al chocar? (Es muy sencillo con pygame.mixer).

"""