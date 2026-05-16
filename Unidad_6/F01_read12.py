""" LECTURA DE ARCHIVOS DE TEXTO

    POP()
    -----
    Eliminar el último elemento de la lista pop()
    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython"
mi_variable = open(ruta_archivo + "/datos.txt")

todas_las_lineas = mi_variable.readlines()
print(todas_las_lineas)             # mostramos la lista completa

todasLasLineas = todas_las_lineas.pop()
print(todas_las_lineas)             # borramos el último elemento de la lista

mi_variable.close()
