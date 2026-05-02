""" DISEÑO DE PATRONES ESTRUCTURALES (PROXY)

    Virtual Proxy (Carga Perezosa o Lazy Loading)
    ---------------------------------------------
    Este es un concepto clave en ingeniería: no gastes recursos si no los vas 
    a usar. Imagina un videojuego con texturas muy pesadas (4K). No las 
    cargues todas al iniciar el juego, cárgalas solo cuando el jugador esté 
    cerca de verlas.

    Comparación para la clase: Adapter vs Proxy
    -------------------------------------------
    Podemos preguntarnos, ¿No son lo mismo?. La respuesta es no

    **) Adapter: Cambia la forma de la interfaz para que dos cosas encajen 
        (traductor).
    **) Proxy: Mantiene la misma forma de la interfaz, pero añade control, 
        seguridad o eficiencia (guardaespaldas).

"""
class ImagenPesada:
    def __init__(self, nombre_archivo):
        self.nombre = nombre_archivo
        self._cargar_de_disco()

    def _cargar_de_disco(self):
        print(f"Cargando {self.nombre} (esto tarda 5 segundos y usa 1GB de RAM)...")

    def mostrar(self):
        print(f"Mostrando {self.nombre} en pantalla.")

class ProxyImagen:
    def __init__(self, nombre_archivo):
        self.nombre = nombre_archivo
        self._imagen_real = None # El objeto real aún no existe

    def mostrar(self):
        # El objeto real SOLO se crea la primera vez que se necesita mostrar
        if self._imagen_real is None:
            self._imagen_real = ImagenPesada(self.nombre)
        self._imagen_real.mostrar()

# --- USO ---
# Aquí NO se gasta memoria todavía
mi_imagen = ProxyImagen("fondo_bosque_4K.png") 

print("El juego ha iniciado, pero el jugador está en el menú...")
# Solo cuando el jugador entra al bosque, se carga la imagen
print("\nJugador entra al bosque:")
mi_imagen.mostrar()
