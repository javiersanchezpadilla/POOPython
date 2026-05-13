""" LECTURA DE ARCHIVOS DE TEXTO

    OPEN:
    -----
    Abrir, leer y cerrar un archivo, la forma más básica de hacerlo.

    El objetivo de este ejemplo es solo aprender a abrir, leer y cerrar un 
    archivo (solamente).
    Para esta práctica vamos a crear un archivo de texto dentro de la carpeta 
    dónde se encuentra el programa para este ejemplo
    datos.txt
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
mi_variable = open(ruta_archivo, 'r')

print(mi_variable.read())
mi_variable.close()
