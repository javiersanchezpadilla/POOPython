""" MULTIPLES CONTEXT MANAGER

    ¿Qué pasa si un archivo falla al abrirse?
    -----------------------------------------

    Comportamiento:

    1)  Intenta abrir existe.txt → éxito
    2)  Intenta abrir no_existe.txt → falla
    3)  Inmediatamente cierra existe.txt (el que sí se abrió)
    4)  Lanza la excepción FileNotFoundError
    5)  Entras al bloque except

    Importante: No deja archivos abiertos aunque falle el segundo.
"""
try:
    with open("existe.txt", "r") as f1, open("no_existe.txt", "r") as f2:
        print("Esto no se ejecuta si falla el segundo archivo")
except FileNotFoundError:
    print("El segundo archivo no existe")
    # Los archivos que SÍ se abrieron (f1) se cierran automáticamente
