""" SERIALIZACIÓN CON PICKLE (BINARIO)

    Deserializar (Recuperar el objeto en un programa nuevo)
    -------------------------------------------------------
    Ahora imaginemos que el programa se cerró, pasaron días, y volvemos a 
    encender la computadora. Queremos recuperar al alumno con todos sus 
    atributos y métodos intactos. Usamos el modo 'rb' (leer binario).

    Al abrir el archivo, nota que usamos el modo 'rb'. 
        'r' significa leer (read) 
        'b' significa binario. 

    Reglas de Seguridad Importantes 
    --------------------------------
    Aunque Pickle es sumamente potente para guardar configuraciones rápidas o 
    estados de juegos, en el desarrollo profesional de software tiene una gran 
    advertencia:

    1)  Exclusivo de Python: Un archivo creado con Pickle solo puede ser leído 
        por Python. Si necesitas que un sistema en Java o un servicio web en 
        JavaScript lea tus datos, debes usar JSON o XML.
    2)  Riesgo de Inyección de Código (Seguridad): Nunca, bajo ninguna 
        circunstancia, debes deserializar (pickle.load()) un archivo que 
        provenga de una fuente en la que no confíes (como un archivo 
        descargado de internet). Un atacante puede manipular los bytes del 
        archivo binario para que, al momento de hacer el load(), Python 
        ejecute comandos maliciosos directamente en el sistema operativo del 
        servidor o de la computadora del usuario.
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


with open(ruta_archivo, "rb") as f:
                                # Reconstruimos el objeto desde el archivo
    alumno_recuperado = pickle.load(f)

print("\nObjeto recuperado de la persistencia:")
print(f"Nombre: {alumno_recuperado.nombre}")
print(f"Matrícula: {alumno_recuperado.numero_control}")
                            # Al ser un objeto real, conserva sus métodos de 
                            # clase
print(f"Promedio calculado desde el objeto: {alumno_recuperado.obtener_promedio():.2f}")
