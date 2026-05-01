""" CLASES ABSTRACTAS.

    Ejercicio de 'Detección y Reparación'. 
    Estos ejercicios son muy efectivos porque simulan lo que sucede cuando un 
    ingeniero integra código de otros compañeros.

    El Reto: El Sistema de Sensores de Fábrica
    ------------------------------------------
    Imagina que eres el Arquitecto de Software de una planta industrial. Has 
    diseñado una clase abstracta para que todos los sensores sigan la misma 
    norma, pero un desarrollador junior te ha enviado un código que no 
    funciona.

    1. El Código 'Roto' (Para revisar y corregir)
    Ejecutar el código. Python lanzará un error inmediatamente.

    2. La Misión del Alumno
    El alumno debe:
    1)  Identificar por qué Python no deja crear el objeto sensor_sala_1.
    2)  Reparar la clase SensorTemperatura añadiendo el método faltante.
    3)  crear una nueva clase SensorPresion que cumpla con el contrato de la 
        clase Sensor.

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

# --- EL ERROR ESTÁ AQUÍ ---
class SensorTemperatura(Sensor):
    def leer_dato(self):
        return 25  # Simula 25 grados

    # El programador OLVIDÓ implementar 'enviar_alerta'


# Intento de uso
# La solución se encuentra en la siguiente vesión del código
sensor_sala_1 = SensorTemperatura("Termómetro Central")
print(f"Temperatura: {sensor_sala_1.leer_dato()}")
