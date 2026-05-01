""" PATRONES DE DISEÑO (FACTORY METHOD)

   El Factory Method es el 'estándar de oro' para crear objetos sin amarrarse 
   a clases concretas, y el Observer es el corazón de cualquier sistema que 
   reaccione a eventos (como una interfaz de usuario o una red social). 

   1. Factory Method (Patrón Creacional)
   -------------------------------------
    Problema: Tienes una aplicación que debe crear diferentes tipos de objetos, 
    pero no sabes cuál necesitarás hasta que el programa esté corriendo (tiempo 
    de ejecución). Si usas if/else gigantes para crear objetos, tu código será 
    difícil de mantener.

    Solución: Delegar la creación de los objetos a un método especializado 
    (la 'fábrica'). De esta forma, el código principal no sabe cómo se crea el 
    objeto, solo sabe qué interfaz tiene.

    Ejemplo generados de enemigos en el juego
"""
from abc import ABC, abstractmethod

# Producto Abstracto
class Enemigo(ABC):
    @abstractmethod
    def atacar(self):
        pass

# Productos Concretos
class Soldado(Enemigo):
    def atacar(self): 
        return "Disparo de fusil"

class Arquero(Enemigo):
    def atacar(self): 
        return "Flechazo certero"

# LA FÁBRICA
class FabricaEnemigos:
    @staticmethod
    def crear_enemigo(tipo):
        if tipo == "soldado":
            return Soldado()
        elif tipo == "arquero":
            return Arquero()
        raise ValueError("Tipo de enemigo no reconocido")


# Uso en el código principal (Desacoplado)
tipo = "soldado" # Esto podría venir de un archivo de nivel o input
enemigo = FabricaEnemigos.crear_enemigo(tipo)
print(f"El enemigo aparece y lanza un: {enemigo.atacar()}")
