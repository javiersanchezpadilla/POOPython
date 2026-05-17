""" FORMATO JSON

    Leer el archivo JSON (Deserializar)
    -----------------------------------
    Ahora hagamos el proceso inverso. Leemos el archivo de texto y dejamos que 
    Python lo reconstruya en un diccionario dinámico.

    El gran límite de JSON (A diferencia de Pickle)
    -----------------------------------------------
    ¿Por qué no usamos siempre JSON si es tan estándar?
    La respuesta es que JSON solo soporta tipos de datos básicos (números, 
    textos, booleanos, listas y diccionarios). 
    JSON NO puede guardar objetos personalizados de tus clases directamente.

    Si intentas pasarle una lista de objetos de tu clase Estudiante a 
    json.dump(), Python lanzará un error de inmediato (TypeError: Object of 
    type Estudiante is not JSON serializable). Para lograr guardar objetos en 
    JSON, primero tendrías que mapear el objeto convirtiéndolo manualmente a 
    un diccionario (extrayendo sus atributos), mientras que pickle lo hacía de 
    forma automática.
"""
import json
from pathlib import Path

ruta_json = Path.cwd() / "curso.json"

                            # Abrimos el archivo en modo lectura ('r')
with open(ruta_json, "r", encoding="utf-8") as f:
                            # Transformamos el texto JSON en un diccionario 
                            # de Python
    datos_recuperados = json.load(f)

print("Datos cargados desde el archivo JSON:")
print("-" * 40)
print(f"Materia: {datos_recuperados['materia']}")
print(f"Total de alumnos inscritos: {len(datos_recuperados['alumnos'])}")
print(f"Primer alumno de la lista: {datos_recuperados['alumnos'][0]}")
print("-" * 40)
