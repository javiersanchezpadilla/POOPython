""" PATRÓN OBSERVER (COMPORTAMIENTO)

    Actualización de Precios (Bolsa de Valores)
    -------------------------------------------
    Cuando el precio de una acción cambia, todos los inversionistas interesados 
    reciben una alerta.
"""
class AccionApple:
    def __init__(self):
        self.inversionistas = []

    def cambiar_precio(self, nuevo_precio):
        print(f"El precio de Apple subió a ${nuevo_precio}")
        for inv in self.inversionistas:
            inv.notificar(nuevo_precio)

class Inversionista:
    def __init__(self, nombre): self.nombre = nombre
    def notificar(self, precio): print(f"{self.nombre} dice: 'Revisaré mi cartera por el precio de ${precio}'")

# Uso
apple = AccionApple()
apple.inversionistas = [Inversionista("Javier"), Inversionista("Pedro")]
apple.cambiar_precio(150.50)
