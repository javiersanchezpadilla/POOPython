""" LECTURA DE ARCHIVOS DE TEXTO

    OPEN:
    -----
    Abrir, leer y cerrar un archivo, la forma más básica de hacerlo.

    El objetivo de este ejemplo es solo aprender a abrir, leer y cerrar un 
    archivo (solamente).
    Para esta práctica vamos a crear un archivo de texto dentro de la carpeta 
    dónde se encuentra el programa para este ejemplo
    datos.txt

    CONCEPTOS BÁSICOS: EL CICLO DE VIDA DE UN ARCHIVO
    -------------------------------------------------

    Todo manejo de archivos sigue tres pasos obligatorios: 

            Abrir → Manipular → Cerrar.

    Por defecto asume la operación de lectura
"""
# podemos indicar solo el nombre del archivo y en automatico buscará dentro
# del proyecto donde estamos                
mi_variable = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt")

print(mi_variable.read())
mi_variable.close()
