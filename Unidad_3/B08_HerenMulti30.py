""" 

    la 'Composición' puede ser más limpia que la herencia múltiple

    1. El concepto: "Tiene un" (Has-a)
    ----------------------------------
    En lugar de heredar de tres clases distintas para crear un 
    GuerreroMago, creamos una clase Personaje y le añadimos (componemos) 
    componentes de ataque.

    2. Ejemplo Práctico: El SmartWatch (Composición)
    ------------------------------------------------
    En lugar de heredar de Reloj y Telefono, el SmartWatch contiene instancias de esas clases.
"""
class ModuloReloj:
    def dar_hora(self):
        return "10:30 AM"

class ModuloTelefono:
    def llamar(self, numero):
        print(f"Llamando al {numero}...")

class SmartWatch:
    def __init__(self):
        # El objeto se compone de otras clases
        self.reloj = ModuloReloj()
        self.telefono = ModuloTelefono()

    def mostrar_estado(self):
        print(f"Hora: {self.reloj.dar_hora()}")
        self.telefono.llamar("911")

# Uso
mi_gadget = SmartWatch()
mi_gadget.mostrar_estado()
