""" SERIALIZACIÓN CON PICKLE (BINARIO)

    Recuperar la lista e iterar sobre ella
    ---------------------------------------
    Cuando el programa vuelve a leer el archivo, pickle.load() te devolverá 
    una lista común y corriente de Python. A partir de ahí, puedes usar un 
    ciclo for para interactuar con cada objeto de forma individual.

    Detalle técnico muy valioso:
    ----------------------------
    Cuando recuperas la lista, pickle no solo recrea los datos (strings, 
    enteros), sino que restablece los enlaces de herencia y métodos. Cada 
    elemento dentro de grupo_recuperado vuelve a ser una instancia real de la 
    clase Estudiante, por lo que puedes mandar a llamar a cualquier método que 
    esa clase tenga definido sin necesidad de hacer configuraciones adicionales. 
    Es una solución de persistencia totalmente directa!!!!
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


                            # 1. Creamos la lista
grupo_sistemas = []
print(type(grupo_sistemas))

ruta_grupo = Path.cwd() / "grupo_sistemas.pkl"

with open(ruta_grupo, "rb") as f:
                            # Reconstruimos la lista original en la 
                            # memoria RAM
    grupo_recuperado = pickle.load(f)

print("\nReporte de Alumnos Recuperados:")
print("-" * 40)

                            # Iteramos sobre la lista recuperada como lo 
                            # harías normalmente
for alumno in grupo_recuperado:
    print(f"Matrícula: {alumno.numero_control} | Alumno: {alumno.nombre:<8} | Nota: {alumno.calificacion}")
    grupo_sistemas.append(Estudiante(alumno.nombre, alumno.numero_control, alumno.calificacion))

print("-" * 40)

                            # mostramos la lista de estudiantes
for alumno in grupo_sistemas:
    print(alumno)
