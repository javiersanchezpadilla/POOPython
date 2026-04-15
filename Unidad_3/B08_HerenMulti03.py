""" HERENCIA Herencia en múltiples niveles

    Jerarquía de Vehículos de Transporte.
    -------------------------------------
    Aquí vemos cómo se van sumando características en cada nivel de la cadena.
"""

class Vehiculo:
    def __init__(self):
        print("Vehículo motorizado listo.")

class Terrestre(Vehiculo):
    def rodar(self):
        print("El vehículo está avanzando sobre el pavimento.")

class AutoCarreras(Terrestre):
    def __init__(self, velocidad_max):
        super().__init__() # Llama a Terrestre, que llama a Vehiculo
        self.velocidad_max = velocidad_max
        print(f"Auto de carreras preparado para {self.velocidad_max} km/h.")

# Instanciación
mi_f1 = AutoCarreras(350)
mi_f1.rodar() # Heredado del nivel intermedio (Terrestre)
