""" Método __str__()

    Personalización de la clase estudiante
"""

class Estudiante:

    def __init__(self, numero_control, nombre, edad, carrera):
        self.numero_control = numero_control
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def __str__(self):
        return f"Estudiante {self.numero_control}"\
               f" | Control {self.numero_control}"\
               f" | Edad {self.edad}"\
               f" | carrera {self.carrera}"
    
estudiante = Estudiante("25320109", "Pedor Perez", 21, "Contador Público")
print(estudiante)
