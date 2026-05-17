""" MANEJO DE LAS RUTAS PATHLIB()

    Validaciones útiles (¿Existe el archivo?)
    -----------------------------------------
    Antes de abrir un archivo o crear una carpeta, es una buena práctica 
    verificar su estado actual. pathlib tiene métodos booleanos directos para 
    esto
"""
from pathlib import Path

mi_archivo = Path("configuracion.json")

                            # Comprobar si la ruta existe en el disco real
if mi_archivo.exists():
    print("El recurso existe.")
    
                            # Comprobar si es un archivo o una carpeta
    if mi_archivo.is_file():
        print("Es un archivo regular.")
    elif mi_archivo.is_dir():
        print("Es un directorio/carpeta.")
else:
    print("El archivo o carpeta no existe en esa ruta.")
