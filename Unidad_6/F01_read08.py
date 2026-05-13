""" LECTURA DE ARCHIVOS DE TEXTO

    Abre el archivo datos.txt e imprime todo su contenido.
    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
miVariable = open(ruta_archivo)

contenido = miVariable.read()
print(contenido)
miVariable.close()

