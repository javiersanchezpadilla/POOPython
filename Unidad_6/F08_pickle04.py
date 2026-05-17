""" SERIALIZACIÓN CON PICKLE (BINARIO)

    Guardar colecciones completas.
    ------------------------------
    una de las mayores ventajas de pickle. No estás limitado a guardar objetos 
    individuales; puedes guardar colecciones completas (listas, diccionarios o 
    tuplas) que contengan múltiples objetos adentro.
    Cuando le pasas una lista a pickle.dump(), este procesa la lista como un 
    súper objeto y congela todo lo que tiene adentro de un solo jalón, 
    manteniendo intactas las relaciones y los datos de cada alumno.

    Ejemplo Práctico: Guardar y Recuperar una Lista de Alumnos
    Siguiendo con la estructura de la clase Estudiante, observemos cómo gestionar
    un grupo completo de 5 alumnos.
"""
import pickle
from pathlib import Path

class Estudiante:
    def __init__(self, nombre, numero_control, calificacion):
        self.nombre = nombre
        self.numero_control = numero_control
        self.calificacion = calificacion

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