""" LECTURA DE ARCHIVOS DE TEXTO

    READLINES()
    -----------
    Leer todas las líneas y asignarlas a una lista readlines(). 

    NOTA: usar solo para archivos pequeños
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython"
mi_variable = open(ruta_archivo + "/datos.txt")

todasLasLineas = mi_variable.readlines()
print(todasLasLineas)

mi_variable.close()
