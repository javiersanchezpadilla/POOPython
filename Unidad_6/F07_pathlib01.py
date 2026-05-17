""" MANEJO DE LAS RUTAS PATHLIB()

    uso de la libreria pathlib.
    ---------------------------

    Mediante el uso de pathlib ya no importa el sistema operativo a usar, 
    simplemente asume rutas iguales.
    pathlib ya no requiere que se tenga que cerrar el archivo, lo hace de 
    forma automática, poder referenciar rutas de archivos sin importar el 
    sistema operativo

    Dominar pathlib es un cambio de juego en Python. Históricamente, las rutas 
    de archivos se manejaban como si fueran simples cadenas de texto (strings) 
    usando el módulo os.path. Sin embargo, tratar una ruta como texto causa 
    muchos dolores de cabeza porque Windows usa la barra invertida (\) y Linux 
    (como Ubuntu o Mint) usa la barra diagonal (/).

    pathlib llegó para solucionar esto tratando las rutas no como texto, sino 
    como objetos. Al ser objetos, tienen propiedades y métodos muy potentes 
    que hacen que tu código funcione en cualquier sistema operativo sin 
    modificar una sola línea.

    1. Concepto Básico: Crear una Ruta
    ----------------------------------
    Para empezar a usarlo, importamos la clase Path. Lo más común es apuntar 
    al directorio actual de trabajo o construir una ruta desde cero.
"""
from pathlib import Path

                        # 1. Obtener el directorio actual donde se ejecuta el 
                        # script (cwd = Current Working Directory)
ruta_actual = Path.cwd()
print(f"Estás trabajando en: {ruta_actual}")

                        # 2. Obtener la carpeta "Home" del usuario 
                        # (ej. /home/javier o C:\Users\javier)
home_usuario = Path.home()
print(f"Tu carpeta de usuario principal es: {home_usuario}")

