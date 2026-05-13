""" LECTURA DE ARCHIVOS DE TEXTO

    Leer todas las líneas y asignarlas a una lista readlines(). 
    usar solo para archivos pequeños
    --------------------------------
    
    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython"
mi_variable = open(ruta_archivo + "/datos.txt")

todasLasLineas = mi_variable.readlines()
print(todasLasLineas)

mi_variable.close()
