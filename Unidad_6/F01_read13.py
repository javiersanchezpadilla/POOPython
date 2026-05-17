""" LECTURA DE ARCHIVOS DE TEXTO

    OBJETO ITERABLE:
    ----------------
    El archivo en sí, es un elemento iterable
    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
mi_variable = open(ruta_archivo)

for linea in mi_variable:
    print(linea)

mi_variable.close()
