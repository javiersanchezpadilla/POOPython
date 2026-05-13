""" ESCRITURA DE ARCHIVOS DE TEXTO

    Crear un archivo modo de escritura 'w' si el archivo existe lo elimina 
    reemplazando por el nuevo archivo y si no existe lo crea.
    La escritura será de todas las lienas en una sola linea dentro del archivo
        Linea 1Linea 2Linea 3Linea 4
"""

archivo = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt",'w')

archivo.write('Linea 1')
archivo.write('Linea 2')
archivo.write('Linea 3')
archivo.write('Linea 4')

archivo.close()
