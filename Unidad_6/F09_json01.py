""" FORMATO JSON

    JSON significa JavaScript Object Notation (Notación de Objetos de 
    JavaScript). A pesar de su nombre, es un formato de texto completamente 
    independiente del lenguaje y es el estándar absoluto en la industria del 
    software para intercambiar información en internet.

    Si has escuchado de las APIs, de las aplicaciones móviles que se conectan 
    a un servidor, o de cómo se guardan las configuraciones en programas como 
    VS Code, todo eso se hace usando JSON.

    Analogía: El traductor universal
    ---------------------------------
    Imagina que tienes un grupo de ingenieros: uno programa en Python, otro en 
    Java y otro en JavaScript.
    Si el ingeniero de Python intenta mandarle una lista de objetos congelada 
    con pickle al de Java, el de Java no va a entender nada porque pickle solo 
    habla Python.

    Aquí es donde entra JSON: es como el inglés del mundo del software. El 
    programador de Python convierte su diccionario a un texto JSON (que parece 
    un string común y corriente), se lo manda al de Java, y este lo lee 
    perfectamente porque casi todos los lenguajes del mundo tienen 
    herramientas para entender texto JSON.

    JSON contra Diccionarios de Python (Son casi idénticos)
    -------------------------------------------------------
    La gran ventaja es que un archivo JSON se escribe casi exactamente igual 
    que un diccionario de Python. 

    **) En JSON, las cadenas de texto obligatoriamente llevan comillas dobles 
        ("Texto"). Las comillas simples ('Texto') marcan un error.
    **) En JSON, los booleanos van en minúscula (true / false), mientras que 
        en Python van con mayúscula (True / False).
    **) En JSON, el valor vacío es null, en Python es None.

    Funciones Clave en Python (import json)
    ---------------------------------------
    Para trabajar con JSON en Python, usamos el módulo nativo json y dos 
    funciones principales que funcionan idéntico a las de pickle:

    1)  json.dump(): Toma un diccionario de Python y lo guarda como un archivo 
        de texto .json.
    2)  json.load(): Lee un archivo .json y lo transforma en un diccionario de 
        Python listo para usar.

    Ejemplo: Guardar un diccionario a JSON (Serializar)
    Imaginemos que queremos guardar la información de una materia y su lista de 
    alumnos inscritos de forma que cualquier otra aplicación pueda leerla.

    Si abrimos el archivo curso.json resultante en tu editor, se verá así 
    (texto plano 100% legible):

            {
                "materia": "Estructura de Datos",
                "semestre": 3,
                "activo": true,
                "alumnos": [
                    "Carlos",
                    "Ana",
                    "Luis"
                ]
            }
"""
import json
from pathlib import Path

                            # Un diccionario nativo de Python
curso_data = {
    "materia": "Estructura de Datos",
    "semestre": 3,
    "activo": True,
    "alumnos": ["Carlos", "Ana", "Luis"]
}

ruta_json = Path.cwd() / "curso.json"

                            # Guardamos el archivo usando el gestor de contexto
with open(ruta_json, "w", encoding="utf-8") as f:
                            # indent=4 sirve para que el archivo de texto se 
                            # guarde ordenado y bonito (legible)
    json.dump(curso_data, f, indent=4, ensure_ascii=False)

print("Archivo 'curso.json' guardado con éxito.")
