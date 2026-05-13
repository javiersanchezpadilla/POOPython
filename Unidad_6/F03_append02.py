""" AGREGAR INFORMACIÓN AL FINAL DEL ARCHIVO DE TEXTO.

    Abre un archivo de texto y cambia su contenido, posteriormente abre
    de nuevo el archivo de texto para su lectura
    pista: Se debe cerrar del modeo escritura y volverlo a abrir en modo 
    lectura.

"""
archivo_ruta = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

mi_archivo = open(archivo_ruta, 'w')
mi_archivo.write('Este sera el contenido del archivo')
mi_archivo.close()

mi_archivo = open(archivo_ruta, 'r')
print(mi_archivo.read())

mi_archivo.close()
