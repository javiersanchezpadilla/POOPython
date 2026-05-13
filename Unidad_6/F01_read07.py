""" LECTURA DE ARCHIVOS DE TEXTO

    POP()
    -----
    Eliminar el último elemento de la lista pop()
    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython"
mi_variable = open(ruta_archivo + "/datos.txt")

todasLasLineas = mi_variable.readlines()
todasLasLineas = todasLasLineas.pop()
print(todasLasLineas)

mi_variable.close()
