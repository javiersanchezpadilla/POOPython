""" MANEJO DE LAS RUTAS PATHLIB()

    Crear carpetas y leer/escribir rápido
    -------------------------------------
    pathlib reduce el código necesario para operaciones comunes. Ya no 
    necesitas el gestor de contexto with open() si lo único que quieres es 
    leer o escribir todo el contenido de un jalón en archivos pequeños o 
    medianos.
"""
from pathlib import Path

                            # Definimos una nueva carpeta
nueva_carpeta = Path.cwd() / "Laboratorio_1"

                            # Crear la carpeta de forma segura. 
                            # exist_ok=True evita que el programa se rompa si 
                            # la carpeta ya existía.
nueva_carpeta.mkdir(exist_ok=True)
print("Carpeta creada o verificada.")

                            # Definimos un archivo dentro de esa carpeta
archivo_notas = nueva_carpeta / "notas.txt"

                            # Escribir texto directamente (Crea el archivo o 
                            # lo sobrescribe)
archivo_notas.write_text("Línea 1: Evaluación de Polimorfismo.\nLínea 2: Nota: 100.", encoding="utf-8")

                            # Leer texto directamente
                            # ruta.read_text() Abre, lee y cierra el archivo 
                            # automáticamente en un solo paso.
contenido = archivo_notas.read_text(encoding="utf-8")
print("\nContenido leído:")
print(contenido)
