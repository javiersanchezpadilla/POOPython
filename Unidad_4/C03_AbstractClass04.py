""" CLASES ABSTRACTAS

    La Solución Esperada del problema anterior.
    -------------------------------------------
    La clase abstracta garantiza que el Polimorfismo funcione después en el 
    ciclo de monitoreo.

    ¿Qué pasaría si NO usáramos @abstractmethod?
    --------------------------------------------
    El programa fallaría mucho después, cuando el ciclo for intentara llamar a 
    enviar_alerta() y el método no existiera. Las clases abstractas nos avisan 
    del error antes de que el programa empiece a correr fuerte.

    ¿Puedo poner lógica real en la clase abstracta?
    -----------------------------------------------
    Respuesta: ¡Sí! El __init__ es un gran ejemplo. Todas las subclases heredan 
    self.nombre, ahorrando código.
"""
from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def leer_dato(self):
        """Debe devolver el valor actual del sensor"""
        pass

    @abstractmethod
    def enviar_alerta(self):
        """Debe imprimir un mensaje si el valor es peligroso"""
        pass


class SensorTemperatura(Sensor):
    def leer_dato(self):
        return 38  # Temperatura alta

    def enviar_alerta(self):
        print(f"ALERTA [{self.nombre}]: ¡Temperatura crítica detectada!")


class SensorPresion(Sensor):
    def leer_dato(self):
        return 120  # PSI

    def enviar_alerta(self):
        print(f"ALERTA [{self.nombre}]: Presión excedida en tubería.")

# --- POLIMORFISMO EN ACCIÓN ---
sensores = [
    SensorTemperatura("Caldera A"),
    SensorPresion("Tanque Gas")
]

print("--- Iniciando Monitoreo Industrial ---")
for s in sensores:
    valor = s.leer_dato()
    print(f"Leyendo {s.nombre}: {valor}")
    if valor > 35: # Umbral de ejemplo
        s.enviar_alerta()
