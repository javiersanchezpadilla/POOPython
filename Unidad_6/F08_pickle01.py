""" SERIALIZACIÓN CON PICKLE (BINARIO)

    La serialización con Pickle es un concepto fundamental que permite 
    resolver el siguiente problema: la memoria RAM es volátil. Cuando tu 
    programa de Python termina de ejecutarse, todas las variables, 
    diccionarios y objetos de tus clases que creaste en la memoria se borran 
    para siempre.

    Para salvar esa información, necesitas guardarla en el disco duro. Pickle 
    es el módulo nativo de Python que se encarga de tomar un objeto complejo 
    que vive en la memoria RAM y convertirlo en un flujo de bytes (un archivo 
    binario) que se puede almacenar o enviar por red.

    Analogía: Juguetes de bloques (LEGO)
    ------------------------------------
    Imagina que construyes un castillo de LEGO muy complejo en tu escritorio 
    (esta es la memoria RAM). Si necesitas mudarte de casa (apagar el 
    programa), no puedes transportar el castillo completo porque se va a 
    romper.

    **) Serialización (Pickling / Congelar): Es el proceso de desarmar el 
        castillo bloque por bloque, meter las piezas en una caja con un 
        instructivo exacto de cómo iba armado y guardarlo en el armario 
        (el disco duro). El objeto ya no está activo, pero su estructura está 
        respaldada en un archivo binario.
    **) Deserialización (Unpickling / Descongelar): Es el proceso inverso. 
        Sacas la caja del armario, lees el instructivo y reconstruyes el 
        castillo exactamente en el mismo estado en el que estaba antes.

    ¿Cómo funciona en el código?
    ----------------------------
    Para usarlo, Python nos proporciona dos funciones principales dentro del 
    módulo pickle:

    1)  dump(): Toma el objeto y lo vierte (escribe) en un archivo binario.
    2)  load(): Carga el archivo binario y lo reconstruye como objeto en la 
        memoria.

    Imaginemos que tenemos una clase Estudiante y queremos guardar el estado 
    de un alumno de forma permanente:
"""
import pickle
from pathlib import Path

                            # 1. Definimos una clase común y corriente
class Estudiante:
    def __init__(self, nombre, numero_control, calificaciones):
        self.nombre = nombre
        self.numero_control = numero_control
        self.calificaciones = calificaciones
        
    def obtener_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Control: {self.numero_control}, calif. {self.calificaciones}"

                            # 2. Creamos un objeto con datos reales en la 
                            #    memoria RAM
alumno_original = Estudiante("Javier", "20120987", [90, 95, 100])

                            # Definimos la ruta del archivo binario usando 
                            # pathlib
ruta_archivo = Path.cwd() / "alumno.pkl"

print(alumno_original)
print(ruta_archivo)
