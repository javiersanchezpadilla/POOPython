""" HERENCIA 

    Herencia sin constructor en la subclase (Ejemplo con Vehículo)
    En este ejemplo, la clase Coche hereda de la clase Vehiculo sin definir 
    su propio constructor (__init__).
    Al crear una instancia de Coche, se llama automáticamente al constructor 
    de Vehiculo, lo que permite inicializar el atributo marca sin necesidad 
    de definir un constructor específico en Coche.
    Esto demuestra que la herencia en Python permite que las subclases 
    utilicen el constructor de la clase padre si no definen el suyo propio.

    El Sistema de Vehículos
    -----------------------
    Aquí la clase Vehiculo define la marca. La clase Coche hereda esa 
    propiedad sin necesidad de repetir el código de inicialización.
"""

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        print(f"Vehículo marca {self.marca} inicializado.")

class Coche(Vehiculo):
    # No hay __init__ aquí
    def encender(self):
        print(f"El coche {self.marca} ha encendido el motor.")

# Python busca el __init__ de Vehiculo automáticamente
mi_auto = Coche("Toyota")
mi_auto.encender()
