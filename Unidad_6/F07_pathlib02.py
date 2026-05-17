""" MANEJO DE LAS RUTAS PATHLIB()

    El operador / (Unir rutas de forma elegante)
    --------------------------------------------
    Ya no es necesario concatenar strings con el símbolo + o usar comas. 
    pathlib redefine el operador de división matemática / para que sirva como 
    separador de carpetas. Es sumamente intuitivo:
"""
from pathlib import Path

                            # Definimos la base
base = Path("/home/javier/Documentos")

                            # Unimos subcarpetas y el archivo usando el 
                            # operador /
archivo_poo = base / "Programas" / "Python" / "datos.txt"

                            # Python detectará automáticamente tu sistema 
                            # operativo y usará las barras correctas.
print(f"Ruta construida: {archivo_poo}")
