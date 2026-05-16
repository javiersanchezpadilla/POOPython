""" LECTURA DE ARCHIVOS DE TEXTO

    STRIP(), RSTRIP()
    -----------------
    Elimina la linea en blanco al final de la linea, elimina el carácter \n

    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
mi_variable = open(ruta_archivo)

una_linea = mi_variable.readline()
print(una_linea.rstrip())           # <-- Elimina el carácter \n (new line)
una_linea = mi_variable.readline()
print(una_linea.rstrip())
una_linea = mi_variable.readline()
print(una_linea.strip())
una_linea = mi_variable.readline()
print(una_linea.strip())

mi_variable.close()

