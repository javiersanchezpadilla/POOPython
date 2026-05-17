""" SERIALIZACIÓN CON PICKLE (BINARIO)

    Paso A: Serializar (Guardar el objeto en el disco)
    --------------------------------------------------
    Al abrir el archivo, nota que usamos el modo 'wb'. 
        'w' significa escribir (write) 
        'b' significa binario. 
    
    Esto es obligatorio porque Pickle no escribe texto legible, escribe bytes.

    Si intentas abrir el archivo alumno.pkl con un editor de texto como 
    VS Code, no verías código normal; verías símbolos extraños o código 
    hexadecimal. El sistema operativo lo ve como un archivo de datos puro.
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

with open(ruta_archivo, "wb") as f:
                            # Guardamos el objeto completo dentro del archivo f
    pickle.dump(alumno_original, f)

print("El objeto 'alumno_original' ha sido serializado y guardado en alumno.pkl")