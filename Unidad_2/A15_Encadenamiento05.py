""" El "Configurador" de Autos (Refactorización)

    El Objetivo
    -----------
    Se deben modificar los métodos de la clase Automovil para que sea posible 
    configurar un coche completo en una sola sentencia de código.

    Código Base
    -----------
    Nota que los métodos actuales no devuelven nada (devuelven None por defecto), 
    por lo que el encadenamiento fallará inicialmente.
    
    Solución en la siguiente version del código
"""
class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Blanco"
        self.combustible = 50
        self.encendido = False

    def pintar(self, nuevo_color):
        self.color = nuevo_color
        print(f"Pintando de {self.color}...")
        # ¿Qué falta aquí para encadenar?

    def cargar_gasolina(self, cantidad):
        self.combustible += cantidad
        print(f"Cargando {cantidad}L...")
        # ¿Qué falta aquí para encadenar?

    def arrancar(self):
        self.encendido = True
        print("Motor en marcha.")
        # ¿Qué falta aquí para encadenar?