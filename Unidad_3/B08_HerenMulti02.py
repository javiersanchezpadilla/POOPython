""" HERENCIA MULTINIVEL
    
    La Herencia Multinivel ocurre cuando una clase hereda de otra clase que, 
    a su vez, ya es una clase hija de otra. Es como un árbol genealógico: 
    
        Abuelo → Padre → Hijo.

    Dispositivos Electrónicos
    -------------------------
    En este caso, vamos de lo más general (un dispositivo) a lo más específico
    (un smartphone).

    Como SmartPhone no tiene método __init__() entonces busca en el padre 
    Telefono, pero como tampoco tiene método __init__(), ahora busca en el 
    abuelo y lo ejecuta
"""

class Dispositivo:
    def __init__(self, marca):
        self.marca = marca
        print(f"Dispositivo {self.marca} fabricado.")

class Telefono(Dispositivo):
    def llamar(self):
        print("Realizando llamada de voz...")

class SmartPhone(Telefono):
    def navegar_internet(self):
        print(f"Navegando en internet desde mi {self.marca}.")

# El SmartPhone tiene acceso a TODO lo de arriba
mi_celular = SmartPhone("Samsung")
mi_celular.llamar()            # Heredado de Telefono
mi_celular.navegar_internet()  # Propio de SmartPhone

