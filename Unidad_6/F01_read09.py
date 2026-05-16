""" LECTURA DE ARCHIVOS DE TEXTO

    Debido a que la variable que usamos para extraer la linea del archivo
    mediante el uso de readline(), pertenece a la clase <class str>, nos
    permite el uso de todos los métodos string, ejemplo upper() lower()
    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""

mi_variable = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt")

una_linea = mi_variable.readline()
print(una_linea.upper())
una_linea = mi_variable.readline()
print(una_linea.upper())
una_linea = mi_variable.readline()
print(una_linea.lower())
una_linea = mi_variable.readline()
print(una_linea.lower())

mi_variable.close()
