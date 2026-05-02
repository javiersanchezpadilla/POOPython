""" PATRÓN OBSERVER (COMPORTAMIENTO)

    El objetivo es que un objeto avise a otros cuando algo cambia, sin estar 
    amarrados.

    1. Sistema de Alarma de Incendios
    ---------------------------------
    Cuando el sensor detecta humo, avisa a los bomberos y activa los aspersores.
"""
class SensorHumo:
    def __init__(self):
        self.observadores = []

    def avisar(self):
        print("¡HUMO DETECTADO!")
        for obs in self.observadores:
            obs.reaccionar()

class Bomberos:
    def reaccionar(self): print("Bomberos en camino...")

class Aspersores:
    def reaccionar(self): print("Aspersores activados...")

# Uso
alarma = SensorHumo()
alarma.observadores = [Bomberos(), Aspersores()]
alarma.avisar()
