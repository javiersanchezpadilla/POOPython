""" LECTURA DE ARCHIVOS DE TEXTO

    Leer el contenido liena por linea (eliminar el \n)
    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""

ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
mi_variable = open(ruta_archivo)

una_linea = mi_variable.readline()
print(una_linea)
una_linea = mi_variable.readline()
print(una_linea)
una_linea = mi_variable.readline()
print(una_linea)
una_linea = mi_variable.readline()
print(una_linea)

mi_variable.close()
