""" MANEJO DE EXCEPCIONES USANDO CLASES

    Controlador de Sensores de Temperatura
    --------------------------------------
    Un sensor puede fallar al conectarse o al entregar una lectura fuera de 
    rango.
"""
class SensorTemperatura:
    def __init__(self):
        self.conectado = False

    def leer(self):
                                            # Conexión al hardware
        try:
            # Simulamos una falla de conexión
            raise ConnectionError("Falla de voltaje en el puerto")
        except ConnectionError as e:
            print(f"Error de hardware: {e}. Reintentando...")
            self.conectado = True           # Simulamos recuperación

                                            # Lectura de datos
        try:
            lectura = "25.5°C" # Dato crudo
            valor = float(lectura.replace("°C", ""))
            print(f"Temperatura actual: {valor} grados.")
        except ValueError:
            print("Error: El sensor envió datos con formato ilegible.")


sensor = SensorTemperatura()
sensor.leer()
