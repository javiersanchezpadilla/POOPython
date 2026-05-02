""" PATRONES DE DISEÑO ESTRUCTURALES (ADAPTER)

    Ejemplo 2: Adaptador de Sensores (Hardware)
    -------------------------------------------
    Imagina que compran un sensor de temperatura que entrega los datos en 
    Fahrenheit, pero todo su software está diseñado para recibir Celsius.

    Resumen:
    --------
    *)  Adaptador: Es como un convertidor de corriente (de enchufe europeo a 
        americano).
    *)  Ventaja: Permite la reutilización de código antiguo.
    *)  Principio Solid: Cumple con el principio de Abierto/Cerrado (Abierto 
        a extensión, cerrado a modificación).
"""
class SensorFahrenheit:
    def obtener_temperatura_f(self):
        return 98.6

class AdaptadorCelsius:
    def __init__(self, sensor_f):
        self.sensor = sensor_f

    def obtener_temperatura_c(self):
        temp_f = self.sensor.obtener_temperatura_f()
        return (temp_f - 32) * 5 / 9

# El software principal solo llama a 'obtener_temperatura_c'
sensor_viejo = SensorFahrenheit()
sensor_adaptado = AdaptadorCelsius(sensor_viejo)

print(f"Temperatura en Celsius: {sensor_adaptado.obtener_temperatura_c():.2f}°C")
