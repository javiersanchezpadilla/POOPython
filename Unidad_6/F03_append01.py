""" AGREGAR INFORMACIÓN AL FINAL DEL ARCHIVO DE TEXTO.

    Modo append
"""
archivo = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt",'a')
archivo.writelines('Esta es una nueva línea')

archivo.close()
