""" LECTURA DE ARCHIVOS DE TEXTO

    RSTRIP()
    ----------
    Leer línea por línea, y eliminar esa línea en blanco usamos

    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
mi_variable = open(ruta_archivo)

una_linea = mi_variable.readline()
print(una_linea.rstrip())
una_linea = mi_variable.readline()
print(una_linea.rstrip())
una_linea = mi_variable.readline()
print(una_linea.rstrip())
una_linea = mi_variable.readline()
print(una_linea.rstrip())

mi_variable.close()

