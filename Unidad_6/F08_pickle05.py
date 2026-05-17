""" SERIALIZACIÓN CON PICKLE (BINARIO)

    Guardar toda la lista de golpe
    ------------------------------
    Al igual que con un solo objeto, usamos pickle.dump(), pero esta vez le 
    pasamos la lista completa grupo_sistemas.
"""
import pickle
from pathlib import Path

class Estudiante:
    def __init__(self, nombre, numero_control, calificacion):
        self.nombre = nombre
        self.numero_control = numero_control
        self.calificacion = calificacion

    def __str__(self):
        return f"[{self.nombre}, {self.numero_control}, {self.calificacion}]"


                            # 1. Creamos la lista con 5 objetos de tipo 
                            # Estudiante
grupo_sistemas = [
    Estudiante("Carlos", "20120001", 85),
    Estudiante("Ana",    "20120002", 92),
    Estudiante("Luis",   "20120003", 78),
    Estudiante("Sofia",  "20120004", 95),
    Estudiante("Javier", "20120005", 100)
]

ruta_grupo = Path.cwd() / "grupo_sistemas.pkl"

with open(ruta_grupo, "wb") as f:
                                # Serializa la lista completa y todos los 
                                # objetos que contiene
    pickle.dump(grupo_sistemas, f)

print("¡Lista de 5 alumnos guardada exitosamente en el archivo binario!")
print(grupo_sistemas)
