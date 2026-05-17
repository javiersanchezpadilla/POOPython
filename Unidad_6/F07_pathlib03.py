""" MANEJO DE LAS RUTAS PATHLIB()

    Extraer partes de una ruta (Atributos del Objeto)
    -------------------------------------------------
    Imagina que tienes la ruta completa de un archivo y necesitas saber sólo 
    su extensión, sólo su nombre o la carpeta que lo contiene. Con un string 
    tendrías que cortar el texto; con pathlib son simples propiedades del 
    objeto
"""
from pathlib import Path

ruta = Path("/home/javier/Documentos/Python/POOPython/examen.pdf")

print(f"Ruta completa: {ruta}")
print(f"Carpeta contenedora (parent): {ruta.parent}")
print(f"Nombre del archivo completo (name): {ruta.name}")
print(f"Nombre sin extensión (stem): {ruta.stem}")
print(f"Solo la extensión (suffix): {ruta.suffix}")
